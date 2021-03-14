# 中文Minecraft Wiki梗体中文资源附加包-基岩版 · Unofficial

[![GitHub issues](https://img.shields.io/github/issues/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?logo=github&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/issues)    [![GitHub pull requests](https://img.shields.io/github/issues-pr/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?logo=github&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/pulls)    [![License](https://img.shields.io/static/v1?label=License&message=CC%20BY-SA%204.0&color=db2331&style=flat-square&logo=creative%20commons)](https://creativecommons.org/licenses/by-sa/4.0/)    [![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?label=latest%20version&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/releases)    [![Minecraft ver](https://img.shields.io/static/v1?label=Minecraft%20version&message=1.13.0%2B&color=db2331&style=flat-square&logo=)](https://minecraft.net)

[![Banner](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack/blob/master/materials/zh_meme_banner.png?raw=true)](https://www.mcbbs.net/thread-1005191-1-1.html)

此资源包仅适用于**Minecraft基岩版**。

* 关于适用于Minecraft Java版的资源包，参见[Java版梗体中文](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)。
* 关于Minecraft基岩版的翻译问题，详见[译名标准化/基岩版](https://minecraft-zh.gamepedia.com/MCW:译名标准化/基岩版)。
  * 关于Minecraft基岩版的简体中文修正，参见中文Minecraft Wiki行政员Ff98sha制作的[基岩版译名修正](https://github.com/ff98sha/mclangcn)。
  * 关于Minecraft基岩版的繁体中文修正，参见小俊AUA制作的[此资源附加包](https://forum.gamer.com.tw/C.php?bsn=18673&snA=183269)。
  * 关于Minecraft基岩版的全语言修正，参见俄语Crowdin校对员fromgate制作的[Translations for Minecraft (Bedrock)](https://www.curseforge.com/minecraft/mc-addons/translations-for-minecraft)。

**若发现自身可能存在该资源包上头的情况，请立刻~~食用~~阅读[译名标准化](https://minecraft-zh.gamepedia.com/MCW:译名标准化)。**

## 注意

* 该资源包的内容完全参照于其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)，另外加入了一些适配于基岩版的内容。
* 以下若无特殊说明，“Minecraft”皆指Minecraft基岩版，“资源包”皆指资源附加包。

## 作用

* 将一部分译名或其他游戏内字符串替换成了一些知名/不知名的梗或笑话，或将其用诙谐的语言重写了一遍。
* 同时使用了Ff98sha制作的[基岩版译名修正](https://github.com/ff98sha/mclangcn)中的内容，以保证未被替换的字符串的翻译正确。
  * 也使用此资源包的内容修正了简体中文的翻译。

## 用法

### 常规

在[Releases](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/releases)中下载此资源包，或在[网页构建](https://dl.meme.teahou.se/)中选择自定义选项下载。

### 加载附加包时

当加载了其他新增了内容（如新的方块、物品等）的附加包时，普通版本的资源包**无法**覆盖附加包新增的字符串，会导致附加包新增的内容**全部变为本地化键名**（对，比Java版还惨）。为此，请下载 `compatible` 版本以保证体验。安装流程几乎相同，但选择的语言应该是普通的**简体中文（中国）**。

### 唱片替换

该资源包将唱片信息修改成了非Minecraft歌曲。由于版权原因，这里有一份不受支持的预制版唱片替换包（不允许二次分发），可在[此处](https://files.lakejason0.ml/images/0/02/Meme_resourcepack_records.mcpack)或[此处](https://dianliang-oss-1301161188.cos.ap-shanghai.myqcloud.com/zh-meme-respack/Meme_resourcepack_records.mcpack)获取。

### 导入

#### 自动导入

* 下载 `meme-resourcepack.mcpack` ，使用Minecraft打开即可。
* 唱片替换资源包的导入方法同理。

#### 手动导入

* 下载 `meme-resourcepack.zip` 并解压。
* 将解压后得到的文件中的 `meme-resourcepack` 文件夹移至Minecraft的 `resource_pack` 文件夹中，路径见下：
  * Windows 10及Windows 10 Mobile： `%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\resource_pack`
  * Android及Fire OS： `sdcard/games/com.mojang/resource_pack`
  * iOS： `Apps/com.mojang.minecraftpe/Documents/games/com.mojang/resource_pack`
* 唱片替换资源包的导入方法同理。

### 使用

* 打开Minecraft，转到设置-全局资源，启用该资源包并置顶。
* 转到设置-语言，选择“梗体中文（天朝）”。
* 开始游戏。

## 鹦鹉通道

### 体验最新内容

想要**抢先体验**最前沿~~整活~~版本，我们强烈建议您前往[网页打包](https://dl.meme.teahou.se/)，那里可以更直观地选择您需要的内容。

若您仍想自己尝试从命令行打包（并不推荐，比较繁琐），可按以下步骤进行：

#### 先决条件

请确保已经安装了Python 3.9+和Git。如果没有，请到[Python官网](https://www.python.org)和[Git官网](https://www.git-scm.com)下载。

#### 步骤

1. 下载源码；
2. 进入文件夹；
3. 安装相关pip依赖；
4. 运行预设打包命令。

``` sh
git clone https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock.git
cd mcwzh-meme-resourcepack-bedrock
pip install -r requirements.txt
python preset_build.py
```

在文件夹中会出现 `meme-resourcepack.zip` 、 `meme-resourcepack_noresource.zip` 、 `meme-resourcepack.mcpack` 和 `meme-resourcepack_noresource.mcpack` 等资源包，名称和作用如上所述。

如果需要预设以外的资源包，可输入需要的参数：

``` bash
python -m memepack_builder ...
```

具体用法可见[此处](https://github.com/Teahouse-Studios/memepack-builder/blob/main/doc/CLI_Manual.zh-hans.md)。

## 贡献

我们欢迎你为这个资源包贡献自己的想法。请参阅[`CONTRIBUTING.md`](./CONTRIBUTING.md)以获取一些建议。

## 声明

* 本资源包**仅供娱乐**，请勿将其可能存在的误导性内容当真。
* 本资源包基于Ff98sha的[基岩版译名修正](https://github.com/ff98sha/mclangcn)和其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)。
* 本资源包与其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)相比可能更新较慢并且缺少一些内容。
  * 缺少的内容可能是由于基岩版本身就缺少这些字符串，也可能是移植时的疏忽造成的。
  * 同理，Java版的内容也可能缺少基岩版的内容。
* 本资源包与Mojang、Minecraft Wiki和Gamepedia无关，原中文翻译版权为Mojang和翻译者所有。
  * 关于正确的译名，请参见[中文Minecraft Wiki的译名标准化](https://minecraft-zh.gamepedia.com/MCW:译名标准化)。
* 本项目文件除另有声明外，均以 ***CC BY-SA 4.0*** 协议授权。
  * 这意味着，你可在署名的情况下自由修改本资源包，但是你再创作的作品必须以本协议发布。
  * 这不是法律建议。
* 本项目未经梗体中文修改过的部分，按照 ***原作品的协议*** 发布。
  * 根据[此Issue](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/issues/11)，本资源包中附带的简体中文语言修正文件不按原协议发布，仍按 ***CC BY-SA 4.0*** 协议授权。
* 本项目 `tools` 目录下的脚本和根目录下的 `preset_build.py` 文件，可选择 ***CC BY-SA 4.0*** 或 ***Apache License 2.0*** 协议之一授权。

![GitHub forks](https://img.shields.io/github/forks/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)    ![GitHub stars](https://img.shields.io/github/stars/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)    ![GitHub watchers](https://img.shields.io/github/watchers/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)
