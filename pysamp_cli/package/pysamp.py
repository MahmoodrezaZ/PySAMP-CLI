from pysamp_cli.models.release import ReleaseVersion, SourceFile, ReleaseFile
from pysamp_cli import __github_releases__
import requests


class PySAMP:
    def __init__(self):
        pass

    @staticmethod
    def __read() -> list[ReleaseVersion]:
        request = requests.get(
            __github_releases__
        )
        response = request.json()

        return [
            ReleaseVersion(
                tag=release.get('tag_name'),
                releases=[ReleaseFile(url=asset.get('browser_download_url')) for asset in release.get('assets')] ,
                source=SourceFile(name=f'PySAMP{release.get('tag_name')}', url=release.get('zipball_url'))
            ) for release in response
        ]

    @classmethod
    def all_releases(cls) -> list[ReleaseVersion]:
        return [r for r in cls.__read() if len(r.releases) > 0]

    @classmethod
    def get_release(cls, tag: str) -> ReleaseVersion | None:
        release_list = [release_version for release_version in cls.__read() if release_version.tag == tag]

        if len(release_list) > 0:
            return release_list
