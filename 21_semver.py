"""
Semver is a system of versioning software in 3 parts.
Read more: https://semver.org/
"""

import re
from typing import Literal

class Semver:
    def __init__(self, version_string: str):
        assert re.match(r"\d+\.\d+\.\d+", version_string) is not None

        self.major, self.minor, self.patch = map(int, version_string.split("."))
    
    def bump(self, part: Literal["major", "minor", "patch"]):
        setattr(self, part, getattr(self, part) + 1)

    def get(self):
        return ".".join(map(str, [self.major, self.minor, self.patch]))
    
    def __str__(self):
        return self.get()
