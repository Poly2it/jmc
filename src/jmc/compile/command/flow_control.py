from typing import Callable
from ._flow_control import (
    if_,
    else_,
    while_,
    do,
    switch,
    for_
)

from ..tokenizer import Token, Tokenizer
from ..datapack import DataPack

FLOW_CONTROL_COMMANDS: dict[str, Callable[
    [
        list[Token],
        DataPack,
        Tokenizer,
    ], str | None]] = {
    'while': while_,
    'do': do,
    'if': if_,
    'else': else_,
    'switch': switch,
    'for': for_,
}
