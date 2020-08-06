# 中文Minecraft Wiki梗体中文资源附加包-基岩版 · Unofficial

[![GitHub issues](https://img.shields.io/github/issues/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?logo=github&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/issues)    [![GitHub pull requests](https://img.shields.io/github/issues-pr/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?logo=github&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/pulls)    [![License](https://img.shields.io/static/v1?label=License&message=CC%20BY-NC-SA%204.0&color=db2331&style=flat-square&logo=creative%20commons)](https://creativecommons.org/licenses/by-nc-sa/4.0/)    [![License](https://img.shields.io/static/v1?label=License+for+script&message=Apache-2.0&color=db2331&style=flat-square&logo=apache)](http://www.apache.org/licenses/LICENSE-2.0)    [![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?label=latest%20version&style=flat-square)](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/releases)    [![Minecraft ver](https://img.shields.io/static/v1?label=Minecraft%20version&message=1.13.0%2B&color=db2331&style=flat-square&logo=)](https://minecraft.net)

[![BannerJava](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack/blob/master/materials/zh_meme_banner.png?raw=true)](https://www.mcbbs.net/thread-1004643-1-1.html)

此资源包仅适用于**Minecraft 基岩版**。

* 关于适用于Minecraft Java版的资源包，参见[Java版梗体中文](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)。

* 关于Minecraft 基岩版的译名修正，参见Ff98sha的[基岩版译名修正](https://github.com/ff98sha/mclangcn)。

**若发现自身可能存在该资源包上头的情况，请立刻~~食用~~阅读[译名标准化](https://minecraft-zh.gamepedia.com/MCW:译名标准化)。**

## 注意

* 该资源包的内容完全参照于其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)，另外加入了一些适配于基岩版的内容。
* 以下若无特殊说明，“Minecraft”皆指Minecraft基岩版，“资源包”皆指资源附加包。

## 作用

* 将一部分译名或其他游戏内字符串替换成了一些知名/不知名的梗或笑话，或将其用诙谐的语言重写了一遍。
* 同时使用了Ff98sha的[译名修正](https://github.com/ff98sha/mclangcn)，以保证未被替换的字符串的翻译正确。

## 用法

* 在[Releases](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock/releases)中下载此资源包。
  * 唱片替换的移植资源包由于版权等问题，请至至[此处](https://files.lakejason0.ml/images/0/02/Meme_resourcepack_records.mcpack)或[此处](https://dianliang-oss-1301161188.cos.ap-shanghai.myqcloud.com/zh-meme-respack/Meme_resourcepack_records.mcpack)下载。

### 自动导入

* 下载 `meme-resourcepack.mcpack` ，使用Minecraft打开即可。
* 唱片替换资源包的导入方法同理。

### 手动导入

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

想要**抢先体验**最前沿~~整活~~版本，请按以下方法操作：

#### 先决条件

请确保已经安装了Python 3.6+和Git。如果没有，请到[Python官网](https://www.python.org)和[Git官网](https://www.git-scm.com)下载。

#### 步骤

1. 下载源码：

``` bash
git clone https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock.git
```

2. 进入文件夹：

``` bash
cd mcwzh-meme-resourcepack-bedrock
```

3. 运行Python命令：

``` bash
python preset_build.py
```

在文件夹中会出现 `meme-resourcepack.zip` 、 `meme-resourcepack_noresource.zip` 、 `meme-resourcepack.mcpack` 和 `meme-resourcepack_noresource.mcpack` 等资源包，名称和作用如上所述。

如果只需要zip格式的资源包，运行：

``` bash
python build.py zip
```

如果只需要mcpack格式的资源包，运行：

``` bash
python build.py mcpack
```

如果不需要自定义材质，添加 `-r none` 选项。

更详细的用法请运行以下命令来获取：

``` bash
python build.py -h
```

## 声明

* 本资源包**仅供娱乐**，请勿将其可能存在的误导性内容当真。
* 本资源包基于Ff98sha的[基岩版译名修正](https://github.com/ff98sha/mclangcn)和其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)。
* 本资源包与其[Java版的版本](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)相比可能更新较慢并且缺少一些内容。
  * 缺少的内容可能是由于基岩版本身就缺少这些字符串，也可能是移植时的疏忽造成的。
  * 同理，Java版的内容也可能缺少基岩版的内容。
* 本资源包与Mojang、Minecraft Wiki和Gamepedia无关，原中文翻译版权为Mojang和翻译者所有。
  * 关于正确的译名，请参见[中文Minecraft Wiki的译名标准化](https://minecraft-zh.gamepedia.com/MCW:译名标准化)。
* 本资源包以 ***CC BY-NC-SA 4.0*** 协议授权。
  * 这意味着，你可在署名的情况下自由修改本资源包，但是你再创作的作品必须以本协议发布。
  * 这不是法律建议。
* 本项目的自动构建脚本以 ***Apache 2.0*** 协议发布。

[![Banner](https://s1.ax1x.com/2020/05/29/tnn9qs.png)](https://www.mcbbs.net/thread-1005191-1-1.html)

![GitHub forks](https://img.shields.io/github/forks/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)    ![GitHub stars](https://img.shields.io/github/stars/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)    ![GitHub watchers](https://img.shields.io/github/watchers/Teahouse-Studios/mcwzh-meme-resourcepack-bedrock?style=social)
