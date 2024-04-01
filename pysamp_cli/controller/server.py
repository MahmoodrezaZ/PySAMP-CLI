import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def pull(server: str):
    pass


@app.command()
def create(server: str):
    pass


@app.command()
def servers(server: str):
    pass


@app.command('list')
def list_servers(server: str):
    pass


if __name__ == '__main__':
    app()
