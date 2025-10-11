class WhatsAppService:

    def send_whatsapp(self, to, text):
        print(f"whatsapp msg ---> : from : {to} \t  --  Message : {text}")


class TelegramService:
    def send_telegram(self, chat_id, msg):
        print(f"from telegram --> to : {chat_id} \t  --  massage : {msg}")


class SMSService:
    def send_sms(self, number, text):
        print(f"from SMS---> to : {number}\t  --  Message : {text}")


# ======= Main class ========

class MessageSender:
    def send_message(self, msg):
        return msg


# ===============  Adaptors  =======================
class WhatsappAdaptor(MessageSender):
    def __init__(self, number):
        self.number = number
        self.service = WhatsAppService()

    def send_message(self, msg):
        self.service.send_whatsapp(self.number, msg)
        return f"✅ message sent to {self.number}"


class TelegramAdaptor(MessageSender):
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.service = TelegramService()

    def send_message(self, msg):
        self.service.send_telegram(self.chat_id, msg)
        return f"✅ message sent to {self.chat_id}"


class SMSAdaptor(MessageSender):

    def __init__(self, number):
        self.number = number
        self.service = SMSService()

    def send_message(self, msg):
        self.service.send_sms(self.number, msg)
        return f"✅ message sent to {self.number}"


# ====== MAIN RUN=====

if __name__ == "__main__":
    w1 = WhatsappAdaptor(912237)
    t1 = TelegramAdaptor("@pouria")
    s1 = SMSAdaptor(91223)

    for item in [w1, t1, s1]:
        item.send_message("hellooo every one")
