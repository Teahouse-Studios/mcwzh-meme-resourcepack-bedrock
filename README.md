# 中文Minecraft Wiki梗体中文资源附加包-基岩版 · Unofficial

[![Tencent QQ](https://img.shields.io/static/v1?label=QQ&message=657876815&color=eb1923&style=flat-square&logo=tencent%20qq)](https://jq.qq.com/?_wv=1027&k=5tqdTeR)    [![GitHub issues](https://img.shields.io/github/issues/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock?logo=github&style=flat-square)](https://github.com/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock/issues)    [![GitHub pull requests](https://img.shields.io/github/issues-pr/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock?logo=github&style=flat-square)](https://github.com/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock/pulls)    [![License](https://img.shields.io/static/v1?label=License&message=CC%20BY-NC-SA%204.0&color=db2331&style=flat-square&logo=creative%20commons)](https://creativecommons.org/licenses/by-nc-sa/4.0/)    [![License](https://img.shields.io/static/v1?label=License+for+script&message=Apache+2.0&color=db2331&style=flat-square&logo=apache)](http://www.apache.org/licenses/)    [![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock?label=latest%20version&style=flat-square)](https://github.com/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock/releases)    [![Minecraft ver](https://img.shields.io/static/v1?label=Minecraft%20version&message=1.13.0%2B&color=db2331&style=flat-square&logo=)](https://minecraft.net)

[![Banner](https://s1.ax1x.com/2020/05/29/tnn9qs.png)](https://www.mcbbs.net/thread-1005191-1-1.html)    [![BannerJava](https://github.com/lakejason0/mcwzh-meme-resourcepack/blob/master/materials/zh_meme_banner.png?raw=true)](https://www.mcbbs.net/thread-1004643-1-1.html)

注：此资源包仅适用于基岩版。有关其Java版的原版，参见[LakeJason0的Java版原版Repository](https://github.com/lakejason0/mcwzh-meme-resourcepack)。

**注：若发现自身可能存在该资源包上头的情况，请立刻~~食用~~阅读[译名标准化](https://minecraft-zh.gamepedia.com/Minecraft_Wiki:译名标准化)。**

## 注意

* 该资源包仅适用于Minecraft基岩版，其内容完全参照于其[Java版的版本](https://github.com/lakejason0/mcwzh-meme-resourcepack)，另外加入了一些适配于基岩版的内容。
* 以下若无特殊说明，“Minecraft”皆指Minecraft基岩版，“资源包”皆指资源附加包。

## 作用

* 该资源包将一部分译名或其他游戏内字符串替换成了一些知名/不知名的梗或笑话，或将其用诙谐的语言重写了一遍。

## 用法

* 在[Releases](https://github.com/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock/releases)中下载此资源包。
  * 唱片的移植包由于版权等问题，请至至[此处](https://files.lakejason0.ml/images/0/02/Meme_resourcepack_records.mcpack)或[此处](https://dianliang-oss-1301161188.cos.ap-shanghai.myqcloud.com/zh-meme-respack/Meme_resourcepack_records.mcpack)下载mcpack文件。

### 自动导入

* 下载 `meme_resourcepack.mcpack` ，使用Minecraft打开即可。
* 唱片包的导入方法同理。

### 手动导入

* 下载 `meme_resourcepack.zip` 并解压。
* 将解压后得到的文件中的 `meme_resourcepack` 文件夹移至Minecraft的 `resource_pack` 文件夹中。
  * Windows 10及Windows 10 Mobile路径： `%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\resource_pack`
  * Android及Fire OS路径： `sdcard/games/com.mojang/resource_pack`
  * iOS路径： `Apps/com.mojang.minecraftpe/Documents/games/com.mojang/resource_pack`
* 唱片包的导入方法同理。

### 使用

* 打开Minecraft，打开设置-全局资源，启用该资源包并置顶。
* 转到设置-语言，选择“梗体中文”。
* 开始游戏。

## 鹦鹉通道

### 体验最新内容

想要**抢先体验**最前沿~~整活~~版本，请按以下方法操作：

#### 先决条件

请确保已经安装了Python 3.x和Git。如果没有，请到[Python官网](https://www.python.org)和[Git官网](https://www.git-scm.com)下载。

#### 步骤

1. 下载源码：

``` bash
git clone https://github.com/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock.git
```

2. 进入文件夹：

``` bash
cd mcwzh-meme-resourcepack-bedrock
```

3. 运行Python命令：

``` bash
python build.py all
```

在文件夹中会出现 `meme_resourcepack.zip` 、 `meme_resourcepack_notexture.zip` 、 `meme_resourcepack.mcpack` 和 `meme_resourcepack_notexture.mcpack` 等资源包，名称和作用如上所述。

如果只需要zip格式的资源包，运行：

``` bash
python build.py zip
```

如果只需要mcpack格式的资源包，运行：

``` bash
python build.py mcpack
```

如果不需要自定义材质，添加 `-n` 选项。

更详细的用法请运行以下命令来获取：

``` bash
python build.py -h
```

## 声明

* 本资源包**仅供娱乐**，请勿将其可能存在的误导性内容当真。
* 本资源包基于Ff98sha的[基岩版译名修正项目](https://github.com/ff98sha/mclangcn)和其[Java版的版本](https://github.com/lakejason0/mcwzh-meme-resourcepack)。
* 本资源包与其[Java版的版本](https://github.com/lakejason0/mcwzh-meme-resourcepack)相比可能更新较慢并且缺少一些内容。
  * 缺少的内容可能是由于基岩版本身就缺少这些字符串，也可能是移植时的疏忽造成的。
  * 同理，Java版的内容也可能缺少基岩版的内容。
* 本资源包与Mojang、Minecraft Wiki和Gamepedia无关，原中文翻译版权为Mojang和翻译者所有。
  * 关于正确的译名，请参见[中文Minecraft Wiki的译名标准化](https://minecraft-zh.gamepedia.com/Minecraft_Wiki:译名标准化)。
* 本资源包以 ***CC BY-NC-SA 4.0*** 协议授权。
  * 这意味着，你可在署名的情况下自由修改本资源包，但是你再创作的作品必须以本协议发布。
  * 这不是法律建议。
* 本项目的自动构建脚本以 ***Apache 2.0*** 协议发布。

![GitHub forks](https://img.shields.io/github/forks/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock?style=social)    ![GitHub stars](https://img.shields.io/github/stars/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock?style=social)    ![GitHub watchers](https://img.shields.io/github/watchers/SkyEye-FAST/mcwzh-meme-resourcepack-bedrock?style=social)
