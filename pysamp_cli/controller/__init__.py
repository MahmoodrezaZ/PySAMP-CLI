from . import pysamp, server
from pysamp_cli.cli import app


app.add_typer(pysamp.app, name='pysamp')
app.add_typer(pysamp.app, name='server')
