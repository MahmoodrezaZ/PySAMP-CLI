from pathlib import Path

from .config import BaseConfig
from .version import BaseVersion
from .file import BaseFile


class ServerFile(BaseFile):
    _allowed_extensions = {
        'Linux': ['gz'],
        'Windows': ['zip']
    }

    def __init__(
            self,
            *,
            url: str,
            path: str | Path = None
    ):
        super().__init__(url=url, path=path)


class ServerVersion(BaseVersion):
    source: ServerFile

    def __init__(
            self,
            *,
            tag: str
    ):
        super().__init__(tag)


class ServerConfig(BaseConfig):
    location: str

    def __init__(self, *, path: Path):
        super().__init__(path=path)
