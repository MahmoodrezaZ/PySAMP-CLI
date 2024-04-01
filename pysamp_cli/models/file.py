from abc import ABC
from typing import Optional
from furl import furl
from pathlib import Path
from pysamp_cli import __os__


class PathIsNotGiven(Exception):
    pass


class BaseFile(ABC):
    url: furl
    name: Optional[str]
    extension: Optional[str]

    def __new__(
            cls,
            url: str,
            name: Optional[str] = None,
            extension: Optional[str] = None,
            path: str | Path = None,
            **kwargs
    ):
        if hasattr(cls, '_allowed_extensions'):
            parsed_url = furl(url)
            if not name:
                name = parsed_url.path.segments[-1]

            if not extension:
                extension = name.split('.')[-1]

            if extension in getattr(cls, '_allowed_extensions')[__os__]:
                return super().__new__(cls)

        else:
            return super().__new__(cls)

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

    def download(self, path: str | Path = None) -> None:
        if path:
            pass

        else:
            if self.path:
                pass

            else:
                raise PathIsNotGiven

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
