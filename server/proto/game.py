# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: server/proto/game.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class Gender(betterproto.Enum):
    MALE = 0
    FEMALE = 1


@dataclass
class Record(betterproto.Message):
    player_info: "PlayerBasicInfo" = betterproto.message_field(1)


@dataclass
class PlayerBasicInfo(betterproto.Message):
    pid: str = betterproto.string_field(1)
    name: str = betterproto.string_field(2)
    create_time: int = betterproto.int64_field(3)
    gender: "Gender" = betterproto.enum_field(4)