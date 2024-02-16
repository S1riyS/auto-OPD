import os
from pathlib import Path
import typing as t

SRC_DIR = Path(__file__).resolve().parent
ROOT_DIR = SRC_DIR.parent
DATA_DIR = ROOT_DIR / 'data'

KEYBOARD_KEYS: t.Dict[str, int] = {
    '0': 96,
    '1': 97,
    'F4': 115,
    'F5': 116,
    'F6': 117
}
