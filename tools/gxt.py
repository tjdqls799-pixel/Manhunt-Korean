"""
Manhunt GXT Toolkit
Author: Manhunt Korean Project

GXT Parser (Work in Progress)
"""

import struct
from dataclasses import dataclass


@dataclass
class GXTEntry:
    key: str
    offset: int
    text: str = ""


class GXT:
    def __init__(self):
        self.entries = []

    def load(self, filename):
        with open(filename, "rb") as f:
            self.data = f.read()

        if self.data[:4] != b"TKEY":
            raise ValueError("Invalid GXT file.")

        print("TKEY header OK")

    def save(self, filename):
        raise NotImplementedError()
