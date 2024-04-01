import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def pull(version: str):
    pass


@app.command()
def versions():
    pass


@app.command('list')
def list_versions():
    pass


if __name__ == '__main__':
    app()
