from pathlib import Path

__package__ = 'MahmoodrezaZ/PySAMP-CLI'
__app_name__ = 'pysamp_cli'
__version__ = '0.1.0'
__pysamp_package__ = 'PySAMP/PySAMP'
__pysamp_latest__ = 'v2.0.1'
__base_repository__ = f'https://github.com/{__package__}'
__github_releases__ = f'https://raw.githubusercontent.com/{__package__}/master/releases.json'
__user_storage__ = Path.home() / '.pysamp_cli'
__releases__ = __user_storage__ / 'releases'
__servers__ = __user_storage__ / 'servers'
__user_config__ = __user_storage__ / '.config.json'
__omp_server__ = 'https://github.com/openmultiplayer/open.mp/releases/download/v1.2.0.2670/open.mp-win-x86.zip'
__samp_server__ = ''
__python_version__ = '3.12'
__python_versions__ = ['3.8', '3.9', '3.10', '3.11', '3.12']
