from abc import ABCMeta, abstractmethod
from collections.abc import Iterable

class DeadlinedMetaReminder(Iterable,ABCMeta=metaclass):

    @abstractmethod
    def is_due():
        pass

    
