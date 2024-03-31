from .version import BaseVersion
from .file import BaseFile
from .config import BaseConfig
from pathlib import Path


class ReleaseFile(BaseFile):
    def __init__(
            self,
            *,
            url: str
    ):
        super().__init__(url=url)


class ReleaseVersion(BaseVersion):
    releases: list[ReleaseFile]
    source: ReleaseFile

    def __init__(
            self,
            *,
            tag: str,
            releases: list[ReleaseFile],
            source: ReleaseFile
    ):
        super().__init__(tag)
        self.releases = releases
        self.source = source


class ReleaseConfig(BaseConfig):
    release: ReleaseFile

    def __init__(
            self,
            *,
            path: Path,
            release: ReleaseFile
    ):
        super().__init__(path=path)
        self.release = release
