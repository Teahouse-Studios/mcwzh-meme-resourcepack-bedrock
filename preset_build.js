const { ModuleParser, BedrockPackBuilder } = require('memepack-builder')
const { writeFileSync, existsSync, mkdirSync } = require('fs')
const { resolve } = require('path')
const glob = require('glob')
const PACK_VERSION = '1.6.1'

const preset_args = [
  {
    platform: 'bedrock',
    type: 'mcpack',
    compatible: false,
    modules: {
      resource: ['meme_resourcepack'],
      collection: [],
    },
  },
  {
    platform: 'bedrock',
    type: 'mcpack',
    compatible: true,
    modules: {
      resource: ['meme_resourcepack'],
      collection: [],
    },
  },
  {
    platform: 'bedrock',
    type: 'zip',
    compatible: false,
    modules: {
      resource: ['meme_resourcepack'],
      collection: [],
    },
  },
  {
    platform: 'bedrock',
    type: 'zip',
    compatible: true,
    modules: {
      resource: ['meme_resourcepack'],
      collection: [],
    },
  },
]
const preset_name = [
  `meme-resourcepack_v${PACK_VERSION}.mcpack`,
  `meme-resourcepack_compatible_v${PACK_VERSION}.mcpack`,
  `meme-resourcepack_v${PACK_VERSION}.zip`,
  `meme-resourcepack_compatible_v${PACK_VERSION}.zip`,
]

async function start() {
  const beModules = new ModuleParser()
  beModules.addSearchPaths(resolve(__dirname, './modules'))
  const be = new BedrockPackBuilder(
    await beModules.searchModules(),
    resolve(__dirname, './modules/prioroty.txt'),
  )

  if (!existsSync('./builds')) {
    mkdirSync('./builds')
  }

  for (const [i, arg] of preset_args.entries()) {
    try {
      let r = await be.build(arg)
      console.log(arg, preset_name[i])
      writeFileSync(resolve(__dirname, `./builds/${preset_name[i]}`), r)
    } catch (e) {
      console.error(e)
      process.exit(1)
    }
  }
  process.exit(0)
}

start()
