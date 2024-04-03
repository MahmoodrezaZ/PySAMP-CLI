import os

import typer
from pysamp_cli import __releases_config__, __pysamp_latest__, __releases__
from pysamp_cli.models import ConfigurationNotFound
from pysamp_cli.models.release import ReleaseListConfig
from pysamp_cli.package.pysamp import PySAMP

app = typer.Typer(no_args_is_help=True)


@app.command()
def pull(tag=typer.Option(
    None,
    '-t',
    '--tag',
    help='Specify pysamp release tag to pull.'
)):
    tag = tag if tag else __pysamp_latest__
    if tag:
        if tag in ReleaseListConfig.load(__releases_config__).release_versions.keys():
            typer.echo(f"{tag} already exists")
            raise typer.Exit()

        release_version = PySAMP.get_release(tag)

        if release_version:
            if not os.path.exists(__releases__ / release_version.tag):
                os.mkdir(__releases__ / release_version.tag)

            store_path = __releases__ / release_version.tag

            for release in release_version.releases:
                release.path = str(release.download(path=store_path))

            release_version.source.path = str(release_version.source.download(path=store_path))

            try:
                r = ReleaseListConfig.load(__releases_config__)
                ReleaseListConfig(
                    path=__releases_config__,
                    release_version=release_version,
                    release_versions=r.release_versions
                ).save()

            except ConfigurationNotFound:
                r = ReleaseListConfig(
                    path=__releases_config__,
                    release_version=release_version
                )
                r.save()

        else:
            typer.echo("No release for given tag.")


@app.command()
def versions():
    typer.echo(
        '\n'.join(
            [release.tag for release in PySAMP.all_releases()]
        )
    )


@app.command('list')
def list_versions():
    release_list_config = ReleaseListConfig.load(path=__releases_config__)

    for release_version in release_list_config.release_versions.keys():
        typer.echo(release_version)


if __name__ == '__main__':
    app()
