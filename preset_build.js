const { ModuleParser, Logger, BedrockPackBuilder } = require('memepack-builder')
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
      resource: ['all'],
      collection: [],
    },
  },
  {
    platform: 'bedrock',
    type: 'mcpack',
    compatible: false,
    modules: {
      resource: [],
      collection: [],
    },
  },
  {
    platform: 'bedrock',
    type: 'mcpack',
    compatible: true,
    modules: {
      resource: ['all'],
      collection: [],
    },
  },
  {
    platform: 'bedrock',
    type: 'mcpack',
    compatible: true,
    modules: {
      resource: [],
      collection: [],
    },
  },
  {
    platform: 'bedrock',
    type: 'zip',
    compatible: false,
    modules: {
      resource: ['all'],
      collection: [],
    },
  },
  {
    platform: 'bedrock',
    type: 'zip',
    compatible: true,
    modules: {
      resource: [],
      collection: [],
    },
  },
]
const preset_name = [
  `meme-resourcepack_v${PACK_VERSION}.mcpack`,
  `meme-resourcepack_noresource_v${PACK_VERSION}.mcpack`,
  `meme-resourcepack_compatible_v${PACK_VERSION}.mcpack`,
  `meme-resourcepack_compatible_noresource_v${PACK_VERSION}.mcpack`,
  `meme-resourcepack_v${PACK_VERSION}.zip`,
  `meme-resourcepack_compatible_noresource_v${PACK_VERSION}.zip`,
]

async function start() {
  const beModules = new ModuleParser(resolve(__dirname, './modules'))
  const be = new BedrockPackBuilder(
    await beModules.moduleInfo(),
    resolve(__dirname, './meme_resourcepack'),
    {
      modFiles: glob.sync('./mods/*.json'),
    },
  )

  if (!existsSync('./builds')) {
    mkdirSync('./builds')
  }

  for (const [i, arg] of preset_args.entries()) {
    try {
      let r = await be.build(arg)
      console.log(arg, preset_name[i])
      writeFileSync(resolve(__dirname, `./builds/${preset_name[i]}`), r.content)
    } catch (e) {
      console.error(Logger.log, e)
      Logger.clearLog()
      process.exit(1)
    }
  }
  process.exit(0)
}

start()
