from pysamp_cli import __python_version__, __python_versions__, __user_config__
from .config import BaseConfig


class UserConfig(BaseConfig):
    python: str
    pysamp: str
    server: str

    def __init__(self, *, python: str, pysamp: str, server: str):
        super().__init__(path=__user_config__)
        self.python = python
        self.pysamp = pysamp
        self.server = server

    @property
    def python(self):
        return self._python

    @python.setter
    def python(self, value):
        if value in __python_versions__:
            self._python = value

        else:
            self._python = __python_version__

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        if value in ['samp', 'sa-mp']:
            self._server = 'sa-mp'

        elif value in ['omp', 'open.mp', 'open-mp']:
            self._server = 'open-mp'

        else:
            self._server = 'open-mp'
