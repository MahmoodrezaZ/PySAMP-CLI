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
            url: str
    ):
        super().__init__(url=url)


class SourceFile(BaseFile):
    _allowed_extensions = {
        'Linux': ['zip'],
        'Windows': ['zip']
    }

    def __init__(
            self,
            *,
            url: str
    ):
        super().__init__(url=url)


class ReleaseVersion(BaseVersion):
    release: ReleaseFile
    source: SourceFile

    def __init__(
            self,
            *,
            tag: str,
            release: ReleaseFile,
            source: SourceFile
    ):
        super().__init__(tag)
        self.release = release
        self.source = source


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
