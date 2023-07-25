import asyncio
from pathlib import Path

from nonebot import get_driver, on_fullmatch
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot.plugin import PluginMetadata
from pydantic import BaseModel


class Config(BaseModel):
    theworld_only_admin: bool = True


__plugin_meta__ = PluginMetadata(
    name="The World",
    description="「ザ・ワールド」ッ！ 時よ止まれ！",
    usage="""
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| the world/世界/咋瓦鲁多/时间停止 | 否 | 群聊 | 启用全群禁言，持续9秒 |
| 然后时间开始流动/时间流动/解除时停 | 否 | 群聊 | 关闭全群禁言 |
| roadroller/泷泽萝拉哒/食我压路机/压路机 | 否 | 群聊 | 播放动画（ |
    """,
    type="application",
    homepage="https://github.com/A-kirami/nonebot-plugin-theworld",
    supported_adapters={"~onebot.v11"},
)

RES_PATH = Path(__file__).parent / "resources"

config = Config.parse_obj(get_driver().config)


async def check_admin(event: GroupMessageEvent) -> bool:
    return not config.theworld_only_admin or event.sender.role != "member"


theworld = on_fullmatch(
    ("the world", "世界", "咋瓦鲁多", "时间停止"), check_admin, ignorecase=True
)


@theworld.handle()
async def the_world(bot: Bot, event: GroupMessageEvent) -> None:
    await bot.set_group_whole_ban(group_id=event.group_id, enable=True)
    await asyncio.sleep(9)
    await bot.set_group_whole_ban(group_id=event.group_id, enable=False)


timeflow = on_fullmatch(("然后时间开始流动", "时间流动", "解除时停"), check_admin)


@timeflow.handle()
async def time_flow(bot: Bot, event: GroupMessageEvent) -> None:
    await bot.set_group_whole_ban(group_id=event.group_id, enable=False)


roadroller = on_fullmatch(("roadroller", "泷泽萝拉哒", "食我压路机", "压路机"), ignorecase=True)


@roadroller.handle()
async def roadrollerda(bot: Bot, event: GroupMessageEvent) -> None:
    files = [
        ("record", "声音1.mp3"),
        ("record", "声音2.mp3"),
        ("record", "声音3.mp3"),
        ("image", "图片1.png"),
        ("image", "图片2.png"),
        ("image", "图片3.png"),
        ("image", "图片4.png"),
        ("image", "图片5.png"),
        ("record", "声音4.mp3"),
        ("record", "声音5.mp3"),
        ("image", "图片6.png"),
        ("image", "图片7.png"),
        ("image", "图片8.png"),
        ("record", "声音6.mp3"),
        ("record", "声音7.mp3"),
        ("record", "声音8.mp3"),
        ("record", "声音9.mp3"),
        ("record", "声音10.mp3"),
        ("record", "声音11.mp3"),
        ("image", "图片9.png"),
        ("record", "声音12.mp3"),
    ]
    silence_begin = 2
    silence_end = 19
    for index, (file_type, file_name) in enumerate(files):
        await roadroller.send(getattr(MessageSegment, file_type)(RES_PATH / file_name))
        await asyncio.sleep(0.5)
        if index == silence_begin:
            await bot.set_group_whole_ban(group_id=event.group_id, enable=True)
        if index == silence_end:
            await bot.set_group_whole_ban(group_id=event.group_id, enable=False)
