from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due():
        pass

class DeadlinedReminder(Iterable, ABC):

    @abstractmethod
    def is_due():
        pass

class DateReminder(DeadlinedReminder):
    def __init__(self,text,date):
        self.text = text
        self.date = parse(date,dayfirst=True)

    def is_due():
        self.date <= datetime.now()

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])



