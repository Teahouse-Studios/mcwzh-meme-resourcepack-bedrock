from argparse import ArgumentParser
from io import TextIOWrapper
from json import load, dump
from sys import stdout


def generate_parser():
    parser = ArgumentParser(
        description='A tool for converting .lang from/to .json.')
    parser.add_argument(
        "type", help="Specify conversion destination file type. Must be 'lang' or 'json'.", choices=['lang', 'json'])
    parser.add_argument("input", help="Path to source file.")
    parser.add_argument(
        "-o", "--output", help="Path to destination file. If omitted, will write to stdout.")
    return parser


def json_to_lang(source: str, dest: TextIOWrapper):
    content = load(open(source, 'r', encoding='utf8'))
    dest.writelines(f'{k}={v}\n' for k, v in content.items())


def lang_to_json(source: str, dest: TextIOWrapper):
    with open(source, 'r', encoding='utf8') as f:
        content = dict(line[:line.find('#') - 1].strip().split("=", 1)
                       for line in f if line.strip() != '' and not line.startswith('#'))
    dump(content, dest, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    args = generate_parser().parse_args()
    f = args.output and open(args.output, 'w', encoding='utf8') or stdout
    if args.type == 'lang':
        json_to_lang(args.input, f)
    elif args.type == 'json':
        lang_to_json(args.input, f)
    if f != stdout:
        f.close()
