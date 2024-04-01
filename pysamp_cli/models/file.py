from abc import ABC
from typing import Optional
from furl import furl
from pathlib import Path


class BaseFile(ABC):
    url: furl
    name: Optional[str]
    extension: Optional[str]

    def __init__(
            self,
            *,
            url: str,
            name: Optional[str] = None,
            extension: Optional[str] = None,
            path: str | Path = None
    ):
        self.url = furl(url)
        self.name = name
        self.extension = extension
        self.path = path

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value

        else:
            self._name = self.url.path.segments[-1]

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        if value:
            self._extension = value

        else:
            self._extension = self.name.split('.')[-1]

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value: str | Path):
        if isinstance(value, str):
            self._path = Path(value)

        elif isinstance(value, Path):
            self._path = value
