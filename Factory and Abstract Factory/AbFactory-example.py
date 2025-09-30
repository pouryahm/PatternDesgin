from abc import ABC, abstractmethod


class NotificationBase(ABC):
    @property
    @abstractmethod
    def messageContent(self):
        pass

    @property
    @abstractmethod
    def senderInfo(self):
        pass

    @property
    @abstractmethod
    def deliveryMethod(self):
        pass


class Email:
    pass


class SMS:
    pass


class Push:
    pass
