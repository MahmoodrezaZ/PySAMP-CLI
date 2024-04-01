from pysamp_cli.models.server import ServerVersion, ServerFile
from pysamp_cli import __omp_server__, __samp_server__, __os__


class InvalidServer(Exception):
    pass


class Server:
    @classmethod
    def get_server(
            cls,
            server: ServerVersion
    ) -> ServerVersion | None:
        if server.tag == 'sa-mp':
            server.source = ServerFile(__samp_server__[__os__])
            return server

        elif server.tag == 'openmp':
            server.source = ServerFile(__omp_server__[__os__])
            return server

        else:
            raise InvalidServer

