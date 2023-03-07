from typing import List


class EmailValidator:
    def __init__(self, min_length: int, valid_mails: List[str], valid_domains: List[str]):
        self.min_length = min_length
        self.mails = valid_mails
        self.domains = valid_domains

    def __is_name_valid(self, name: str) -> bool:
        len_name = len(name)
        if len_name >= self.min_length:
            return True
        else:
            return False
        # return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        if mail in self.mails:
            return True
        else:
            return False
        # return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        if domain in self.domains:
            return True
        else:
            return False
        # return domain in self.domains

    def validate(self, email: str) -> bool:
        name = email.split("@")[0]
        mail = email.split("@")[-1].split(".")[0]
        domain = email.split(".")[-1]
        if self.__is_name_valid(name) and\
                self.__is_mail_valid(mail) and\
                self.__is_domain_valid(domain):
            return True
        else:
            return False
        # return all([self.__is_name_valid(name),
        #             self.__is_mail_valid(mail),
        #             self.__is_domain_valid(domain)])


# mails = ["gmail", "softuni"]
# domains = ["com", "bg"]
# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))
