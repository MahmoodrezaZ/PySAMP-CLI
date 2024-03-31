from abc import ABC
from pathlib import Path
from typing import Any, Dict, Self
import json


class BaseConfig(ABC):
    default_values: dict[str, Any]

    def __init__(
            self,
            *,
            path: Path
    ):
        self.__path = path

    def __export(self) -> Dict[str, Any]:
        export = {}
        for key, value in self.__dict__.items():
            if key.startswith(f'_{self.__class__.__name__}'):
                continue

            elif key.startswith('_'):
                export[key.replace('_', '')] = value

            else:
                export[key] = value

        return export

    @classmethod
    def create(cls) -> Self:
        config = cls(
            **cls.default_values
        )
        config.save()
        return config

    def save(self) -> None:
        try:
            with open(self.__path, 'w', encoding='utf-8') as f:
                json_content: dict = json.dumps(self.__export())
                f.write(json_content)

        except json.JSONDecodeError:
            raise WrongConfiguration(self.__path)

        except FileNotFoundError:
            raise ConfigurationNotFound(self.__path)

    @classmethod
    def load(cls, path) -> Self:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                json_content: dict = json.loads(content)

                kwargs = {}

                for key, value in json_content.items():
                    if key in cls.__dict__:
                        kwargs[key] = value

                return cls(
                    **kwargs
                )

        except json.JSONDecodeError:
            raise WrongConfiguration(path)

        except FileNotFoundError:
            return ConfigurationNotFound(path)


class ConfigBaseException(json.JSONDecodeError):
    def __init__(
            self,
            path
    ):
        self.path = path


class WrongConfiguration(ConfigBaseException):
    def __init__(
            self
    ):
        self.msg = f'Wrong configuration file at {self.path}'


class ConfigurationNotFound(ConfigBaseException):
    def __init__(
            self
    ):
        self.msg = f'Configuration file does not exists at {self.path}'
