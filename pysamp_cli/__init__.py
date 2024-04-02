from pathlib import Path
import platform

# Package Data
__package__ = 'MahmoodrezaZ/PySAMP-CLI'
__app_name__ = 'pysamp_cli'
__version__ = '0.1.0'
__base_repository__ = f'https://github.com/{__package__}'

# User Storage
__user_storage__ = Path.home() / '.pysamp_cli'
__user_config__ = __user_storage__ / '.config.json'

# Release Storage
__releases__ = __user_storage__ / 'releases'
__releases_config__ = __releases__ / '.config.json'

# Server Storage
__servers__ = __user_storage__ / 'servers'


# General Data
__os__ = platform.system()
__pysamp_package__ = 'PySAMP/PySAMP'
__pysamp_latest__ = 'v2.0.1'
__github_releases__ = f'https://raw.githubusercontent.com/{__package__}/master/releases.json'
__omp_server__ = {
    'Windows': 'https://github.com/openmultiplayer/open.mp/releases/download/v1.2.0.2670/open.mp-win-x86.zip',
    'Linux': 'https://github.com/openmultiplayer/open.mp/releases/download/v1.2.0.2670/open.mp-linux-x86.tar.gz'
}
__samp_server__ = {
    'Windows': 'https://raw.githubusercontent.com/KrustyKoyle/files.sa-mp.com-Archive/master/samp037_svr_R2-2-1_win32.zip',
    'Linux': 'https://raw.githubusercontent.com/KrustyKoyle/files.sa-mp.com-Archive/master/samp037svr_R2-2-1.tar.gz'
}
__python_version__ = '3.12'
__python_versions__ = ['3.8', '3.9', '3.10', '3.11', '3.12']
