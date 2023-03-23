# # Single Responsibility (SRP):


from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self) -> str:
        pass


class MyContent(IContent):
    def format(self) -> str:
        return '\n'.join(['<myML>', self.text, '</myML>'])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender: str):
        pass

    @abstractmethod
    def set_receiver(self, receiver: str):
        pass

    @abstractmethod
    def set_content(self, content: object):
        pass


class Email(IEmail):
    def __init__(self, protocol: str):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: str) -> None:
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver: str) -> None:
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content: object) -> None:
        self.__content = content.format()

    def __repr__(self) -> str:
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)

# Sender: I'm qmal
# Receiver: I'm james
# Content:
# <myML>
# Hello, there!
# </myML>
