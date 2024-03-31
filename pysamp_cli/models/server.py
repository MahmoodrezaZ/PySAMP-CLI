from pathlib import Path

from .config import BaseConfig
from .version import BaseVersion
from .file import BaseFile


class ServerFile(BaseFile):
    def __init__(
            self,
            *,
            url: str
    ):
        super().__init__(url=url)


class ServerVersion(BaseVersion):
    source: ServerFile

    def __init__(
            self,
            *,
            tag: str,
            source: ServerFile
    ):
        super().__init__(tag)
        self.source = source


class ServerConfig(BaseConfig):
    def __init__(self, *, path: Path):
        super().__init__(path=path)
