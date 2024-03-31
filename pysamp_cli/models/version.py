from abc import ABC


class BaseVersion(ABC):
    """
    BaseVersion is a base-class for version of a resource

    its
    """
    tag: str

    def __init__(
            self,
            *,
            tag: str
    ):
        self.tag = tag
