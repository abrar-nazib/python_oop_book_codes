import abc


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @property
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls in MediaLoader:
            attrs = set(dir(subclass))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
