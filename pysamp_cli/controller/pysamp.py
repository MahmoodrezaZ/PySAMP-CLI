import typer
from pysamp_cli import __releases_config__
from pysamp_cli.models.release import ReleaseListConfig
from pysamp_cli.package.pysamp import PySAMP

app = typer.Typer(no_args_is_help=True)


@app.command()
def pull(version: str):
    pass


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
