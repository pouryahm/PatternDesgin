from abc import ABC, abstractmethod


# ======================BASE CLASSES  ===============================
class NotificationBase(ABC):

    @property
    @abstractmethod
    def content(self):
        pass

    @property
    @abstractmethod
    def sender(self):
        pass

    @property
    @abstractmethod
    def delivery(self):
        pass


class DeliveryBase(ABC):
    @abstractmethod
    def show(self):
        pass


class SenderBase(ABC):
    @abstractmethod
    def show(self):
        pass


class ContentBase(ABC):
    @abstractmethod
    def show(self):
        pass


# ======================LOG FACTORY SINGLOTEN ===============================
class SingleMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingleMeta):
    def __init__(self):
        self.logs = []

    def log(self, kind, message, **meta):
        data = {
            "type": kind,
            "message": message,
            "data": meta,
            "time": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        }
        self.logs.append(data)

    def show_logs(self):
        print("\n---LOGS----")
        for log in self.logs:
            meta_text = " | ".join([f"{k}: {v}" for k, v in log["data"].items()])
            print(f"[{log['time']}] [{log['type']}] {log['message']} → {meta_text}")


# ======================EMAIL FACTORY ===============================


class EmailSender(SenderBase):
    def __init__(self, email):
        self.email = email

    def show(self):
        return f"the email sender is {self.email.email_sender}"


class EmailContent(ContentBase):
    def __init__(self, email):
        self.email = email

    def show(self):
        return f"the email Content is {self.email.email_content}"


class EmailDelivery(DeliveryBase):
    def __init__(self, email):
        self.email = email

    def show(self):
        return f"the email Delivery method is {self.email.delivery_method}"


class EmailNotification(NotificationBase):

    def __init__(self, email_content, email_sender, delivery_method, ):
        self.email_content = email_content
        self.email_sender = email_sender
        self.delivery_method = delivery_method

        # add to logs
        Logger().log("Email", "Email Create", sender=self.email_sender, msg=self.email_content)

    def __str__(self):
        return f" Email Notification from ( {self.email_sender} )"

    @property
    def sender(self):
        return EmailSender(self)

    @property
    def content(self):
        return EmailContent(self)

    @property
    def delivery(self):
        return EmailDelivery(self)


# ======================SMS FACTORY ===============================

class SmsSender(SenderBase):
    def __init__(self, sms):
        self.sms = sms

    def show(self):
        return f'The phone Number is {self.sms.phone_number}\t'


class SmsContent(ContentBase):

    def __init__(self, sms):
        self.sms = sms

    def show(self):
        return f" sms content is {self.sms.sms_content}\t"


class SmsProvider(DeliveryBase):
    def __init__(self, sms):
        self.sms = sms

    def show(self):
        return f" The provider is {self.sms.provider} \t"


class SMSNotifications(NotificationBase):

    def __init__(self, sms_content, phone_number, provider):
        self.sms_content = sms_content
        self.phone_number = phone_number
        self.provider = provider
        # add to logs
        Logger().log("SMS", "SMS Create", sender=self.phone_number, msg=self.sms_content)

    def __str__(self):
        return f"SMS notification from ( {self.phone_number} )"

    @property
    def content(self):
        return SmsContent(self)

    @property
    def sender(self):
        return SmsSender(self)

    @property
    def delivery(self):
        return SmsProvider(self)


# ======================PUSH FACTORY ===============================

class PushContent(ContentBase):
    def __init__(self, push):
        self.push = push

    def show(self):
        return f"Push Title: {self.push.push_title}, Message: {self.push.push_message}"


class PushSender(SenderBase):
    def __init__(self, push):
        self.push = push

    def show(self):
        return f"Sent from app: {self.push.app_name}"


class PushDelivery(DeliveryBase):
    def __init__(self, push):
        self.push = push

    def show(self):
        return "Delivered via Firebase Cloud Messaging"


class PushNotification(NotificationBase):
    def __init__(self, push_title, push_message, app_name):
        self.push_title = push_title
        self.push_message = push_message
        self.app_name = app_name

        # add to logs
        Logger().log("Push", "Push Create", app=self.app_name, msg=self.push_message)

    def __str__(self):
        return f"Push notification from ( {self.app_name} )"

    @property
    def content(self):
        return PushContent(self)

    @property
    def sender(self):
        return PushSender(self)

    @property
    def delivery(self):
        return PushDelivery(self)


if __name__ == "__main__":
    e1 = EmailNotification("e1 content ", "pourya@gmail.com", "SMTP")
    s1 = SMSNotifications("Hello Pouria", "09122379077", "Hamrah  aval")
    p1 = PushNotification("The New Push", " Hello From Push ", "Radio Javan")
    notifList = [e1, s1, p1]

    for item in notifList:
        print(f"== The {item} ===")
        print(item.content.show())
        print(item.sender.show())
        print(item.delivery.show())
        print("\t")

    Logger().show_logs()
