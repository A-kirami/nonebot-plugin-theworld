<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-theworld

_✨ 「ザ・ワールド」ッ！ 時よ止まれ！ ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/A-kirami/nonebot-plugin-theworld.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-theworld">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-theworld.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

> 「ザ・ワールド」ッ！ 時よ止まれ！

![theworld](https://img.moegirl.org.cn/common/2/26/%E4%B8%96%E7%95%8C%E5%8D%A1%E4%BD%8F%E6%97%B6%E9%97%B4%E9%BD%BF%E8%BD%AE.png)

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-theworld

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-theworld
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-theworld
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-theworld
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-theworld
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_theworld"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| THEWORLD_ONLY_ADMIN | 否 | true | 是否仅管理员可使用 |

## 🎉 使用

### 指令表

| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| the world/世界/咋瓦鲁多/时间停止 | 否 | 群聊 | 启用全群禁言，持续9秒 |
| 然后时间开始流动/时间流动/解除时停 | 否 | 群聊 | 关闭全群禁言 |
| roadroller/泷泽萝拉哒/食我压路机/压路机 | 否 | 群聊 | 播放动画（ |
