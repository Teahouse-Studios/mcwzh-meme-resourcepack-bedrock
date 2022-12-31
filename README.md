# 中文Minecraft Wiki梗体中文资源附加包-基岩版 · Unofficial

[![GitHub issues](https://img.shields.io/github/issues/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?logo=github&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/issues)    [![GitHub pull requests](https://img.shields.io/github/issues-pr/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?logo=github&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/pulls)    [![License](https://img.shields.io/static/v1?label=License&message=CC%20BY-SA%204.0&color=db2331&style=flat-square&logo=creative%20commons)](https://creativecommons.org/licenses/by-sa/4.0/)    [![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?label=latest%20version&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/releases)    [![Minecraft ver](https://img.shields.io/static/v1?label=Minecraft%20version&message=1.13.0%2B&color=db2331&style=flat-square&logo=)](https://minecraft.net)

[![Banner](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack/blob/master/materials/zh_meme_banner.png?raw=true)](https://www.mcbbs.net/thread-1005191-1-1.html)

此资源包仅适用于**Minecraft基岩版**。

* 关于适用于Minecraft Java版的资源包，参见[Java版梗体中文](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)。
* 关于Minecraft基岩版的翻译问题，详见[译名标准化/基岩版](https://minecraft-zh.gamepedia.com/MCW:译名标准化/基岩版)。
  * 关于Minecraft基岩版的简体中文修正，参见中文Minecraft Wiki行政员Ff98sha制作的[基岩版译名修正](https://github.com/ff98sha/mclangcn)。
  * 关于Minecraft基岩版的繁体中文修正，参见小俊AUA制作的[此资源附加包](https://forum.gamer.com.tw/C.php?bsn=18673&snA=183269)。
  * 关于Minecraft基岩版的全语言修正，参见俄语Crowdin校对员fromgate制作的[Translations for Minecraft (Bedrock)](https://www.curseforge.com/minecraft-bedrock/addons/translations-for-minecraft)。

## 赞助者
<p align="center">
  <a href="https://afdian.net/@teahouse">
    <img src='https://fe.wd-ljt.com/m3me/sP0ns0r5/sP0ns0r5.svg'>
  </a>
</p>

## 注意

* 本资源包**仅供娱乐**，请勿将其可能存在的误导性内容当真。
  * 若发现自身可能存在该资源包上头的情况，**请立刻~~食用~~阅读[译名标准化](https://minecraft.fandom.com/zh/wiki/MCW:译名标准化)**。
  * 在使用本资源包的过程中，若难以理解被修改后的内容，**请及时在设置中将语言改回简体中文**。
* 本资源包的内容大部分参照于其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)，另外加入了一些适配于基岩版的内容。
* 若无特殊说明，下文中“Minecraft”皆指**Minecraft基岩版**，“资源包”皆指附加包中的类型之一。

### 加载其他附加包时

常规版本的资源包加入了新的语言“梗体中文（天朝）”，存储于文件 `zh_ME.lang` 中；而当加载了其他新增自定义内容（如新的方块、物品等）的附加包时，由于其新增的字符串储存于简体中文语言文件 `zh_CN.lang` 中，梗体中文**无法**覆盖这些字符串。

这会导致附加包新增的内容**全部变为本地化键名**，像是 `item.netherite_ingot.name` 一类的东西（对，比Java版还惨），同时市场（Marketplace）等中的内容会全部变为英语，~~虽然本来基翻也很烂~~。为此，请下载 `compatible` 版本以保证体验。资源包的安装流程完全相同，但在设置中选择的语言应该是普通的**简体中文**。

如果选择 `compatible` 版本的梗体中文后，在游戏中依旧显示本地化键名，很有可能是您加载的其他附加包制作时仅有英语或其他语言，本身就没有简体中文的语言文件。这与梗体中文没有关系，请您联系该附加包作者或自行进行汉化。

### 较旧的Minecraft版本

虽然我们写明了支持1.13.0及以上的所有版本，但那是由于清单文件 `manifest.json` 中的 `format_version` 字段自版本1.13.0.9起更改为 `2` 。而目前版本的Minecraft要求资源包的清单文件中 `min_engine_version` 字段为必填项（此字段用于限制此附加包为之编写的最低游戏版本，可以帮助游戏确定此附加包是否需要向后兼容）；若不填写，游戏会报错无法读取，我们只能填写为1.13.0。

由于基岩版的语言文件不同版本间改动过为繁杂，如果要理清这些改动并适配，工作量实在过大，恕我们只能维持最新版Minecraft的游戏体验。

理论上，我们最低可以支持到1.0.4版本的Minecraft，但1.13.0.9前的 `format_version` 字段必须为 `1` ；同时，版本越早，语言文件与目前版本的差别越大，故我们放弃支持了1.0.4－1.13.0间的Minecraft版本。

综上所述，梗体中文无法在旧版Minecraft覆盖所有字符串，若您仍然使用旧版Minecraft，您可能会在游玩过程中发现显示错误。同时，模块内容可能在旧版不受支持。我们推荐您保持更新到最新版本的Minecraft以获得完整的游戏体验。

## 作用

* 将一部分译名或其他游戏内字符串替换成了一些知名/不知名的梗或笑话，或将其用诙谐的语言重写了一遍。
* 使用了Ff98sha制作的[基岩版译名修正](https://github.com/ff98sha/mclangcn)，以保证梗体中文中未被替换的字符串的翻译正确。
  * 同时也使用此资源包的内容修正了简体中文的翻译，即安装本资源包后不需要再次安装译名修正。

## 用法

### 获取

可以在[Releases](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/releases)中选择默认选项下载，亦可于[在线构建](https://dl.meme.teahou.se/)中选择自定义选项下载。

若想要抢先体验最前沿的~~整活~~版本，请参见“鹦鹉通道”段落。

#### 唱片替换

本资源包将唱片信息修改成了非Minecraft歌曲。由于版权原因，这里有一份不受支持的预制版唱片替换包（不允许二次分发），可在[此处](https://lakeus.xyz/images/0/02/Meme_resourcepack_records.mcpack)或[此处](https://wdf.ink/record-bedrock)获取。

### 导入

#### 自动导入

* 下载文件后缀为 `.mcpack` 的资源包，在打开方式中选择使用Minecraft打开即可。

#### 手动导入

* 下载文件后缀为 `.zip` 的资源包。
* 将资源包文件移至Minecraft的数据路径下存放资源包处，路径见下：
  * Windows 10： `%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\resource_pack`
    * 预览版（Preview）： `%LOCALAPPDATA%\Packages\Microsoft.MinecraftWindowsBeta_8wekyb3d8bbwe\LocalState\games\com.mojang\resource_pack`
  * Android/Fire OS： `/sdcard/Android/data/com.mojang.minecraftpe/files/games/com.mojang/resource_packs`
    * 1.18.0.21前（见[此处](https://help.minecraft.net/hc/en-us/articles/4414144725389-Minecraft-External-Storage-Update-on-Android): `/sdcard/games/com.mojang/resource_pack`
  * iOS/iPadOS： `Apps/com.mojang.minecraftpe/Documents/games/com.mojang/resource_pack`
* 解压资源包文件（可选，不解压游戏亦能读取）。

### 使用

1. 打开Minecraft，转到设置-全局资源，启用该资源包并置顶；
2. 转到设置-语言，选择“梗体中文（天朝）”；
3. 开始游戏。

## 鹦鹉通道

### 在线构建

梗体中文处于不断更新中，欢迎常回来看看。鉴于本资源包采用模块化，我们强烈建议您前往[在线构建](https://dl.meme.teahou.se/)获取最新的自定义版本，那里可以更直观地选择您需要的内容。

### 命令行操作

若您仍想自己尝试从命令行打包（并不推荐，比较繁琐），可按以下步骤进行：

#### 先决条件

请确保已经安装了NodeJS主流版本和Git。如果没有，请到[NodeJS官网](https://nodejs.org/zh-cn/)和[Git官网](https://www.git-scm.com)下载。

#### 步骤

1. 下载源码；
2. 进入文件夹；
3. 安装相关依赖；
4. 运行预设打包命令。

``` sh
git clone https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack.git
cd mcwzh-meme-resourcepack
npm install
node preset_build.js
```

在文件夹中会出现 `meme-resourcepack.zip` 、 `meme-resourcepack_noresource.zip` 、 `meme-resourcepack.mcpack` 和 `meme-resourcepack_noresource.mcpack` 等资源包，名称和作用如上所述。

## 贡献

我们欢迎您为这个资源包贡献自己的想法。请参阅[`CONTRIBUTING.md`](./CONTRIBUTING.md)以获取一些建议。

## 声明

* 本资源包基于Ff98sha的[基岩版译名修正](https://github.com/ff98sha/mclangcn)和其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)制作。
* 本资源包与其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)相比可能更新较慢并且缺少一些内容。
  * 缺少的内容可能是由于基岩版本身就缺少这些字符串，也可能是移植时的疏忽造成的，如果遇到这些情况请您积极提交议题反馈。
  * 同理，Java版的内容也可能缺少基岩版的内容。
* 本资源包与Mojang、Minecraft Wiki、Gamepedia和Fandom无关，原中文翻译版权为Mojang和翻译者所有。
  * 关于正确的译名，请参见[中文Minecraft Wiki的译名标准化](https://minecraft-zh.gamepedia.com/MCW:译名标准化)。
* 本项目文件除另有声明外，均以 ***CC BY-SA 4.0*** 协议授权。
  * 这意味着，您可在署名的情况下自由修改本资源包，但是您再创作的作品必须以本协议发布。
  * 这不是法律建议。
* 本项目未经梗体中文修改过的部分，按照 ***原作品的协议*** 发布。
  * 根据[此议题](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/issues/11)，本资源包中附带的简体中文语言修正文件不按原协议发布，仍按 ***CC BY-SA 4.0*** 协议授权。
* 本项目 `tools` 目录下的脚本和根目录下的 `preset_build.py` 文件，可选择 ***CC BY-SA 4.0*** 或 ***Apache License 2.0*** 协议之一授权。

![GitHub forks](https://img.shields.io/github/forks/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)    ![GitHub stars](https://img.shields.io/github/stars/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)    ![GitHub watchers](https://img.shields.io/github/watchers/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)
