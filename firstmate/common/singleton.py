from typing import Any


class SingletonMeta(type):
    """
    Metaclass for Singletons
    """

    __instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:

        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwds)
            cls.__instances[cls] = instance

        return cls.__instances[cls]
