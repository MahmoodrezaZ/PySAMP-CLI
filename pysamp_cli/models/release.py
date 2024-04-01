from .version import BaseVersion
from .file import BaseFile
from .config import BaseConfig
from pathlib import Path


class ReleaseFile(BaseFile):
    _allowed_extensions = {
        'Linux': ['so'],
        'Windows': ['dll']
    }

    def __init__(
            self,
            *,
            url: str,
            path: str | Path = None
    ):
        super().__init__(url=url, path=path)


class SourceFile(BaseFile):
    _save_extension: str = 'zip'

    def __init__(
            self,
            *,
            url: str,
            name: str,
            path: str | Path = None
    ):
        super().__init__(url=url, path=path)
        self.name = name
        self.extension = self._save_extension

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            if not self._name.endswith(f'.{self._save_extension}'):
                self._name = f'{value}.{self._save_extension}'

            else:
                self._name = value

        else:
            self._name = self.url.path.segments[-1]


class ReleaseVersion(BaseVersion):
    releases: list[ReleaseFile]
    source: SourceFile

    def __init__(
            self,
            *,
            tag: str,
            releases: list[ReleaseFile],
            source: SourceFile
    ):
        super().__init__(tag=tag)
        self.releases = releases
        self.source = source

    @property
    def releases(self):
        return self._releases

    @releases.setter
    def releases(self, value: list[ReleaseFile]):
        self._releases = [r for r in value if isinstance(r, ReleaseFile)]


class ReleaseConfig(BaseConfig):
    release: str
    source: str

    def __init__(
            self,
            *,
            path: Path,
            release: ReleaseFile,
            source: SourceFile,
    ):
        super().__init__(path=path)
        self.release = str(release.path)
        self.source = str(source.path)
