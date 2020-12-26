from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse

class DeadlinedMetaReminder(Iterable,ABCMeta=metaclass):

    @abstractmethod
    def is_due():
        pass

class DeadlinedReminder(Iterable,ABC):

    @abstractmethod
    def is_due():
        pass

class DateReminder(DeadlinedReminder):
    def __init__(self,date):



