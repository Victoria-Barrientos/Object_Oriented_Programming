from abc import ABC, abstractmethod

class BillingEntity(ABC):
    @abstractmethod
    def get_billing_info(self):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

class IndividualPersona(BillingEntity):
    def __init__(self, name: str, email: str, bank: str, card_number: str, billing_address: str, balance: float):
        self.name = name
        self.email = email
        self.bank = bank
        self.__card_number = card_number  # Private attribute
        self.__billing_address = billing_address  # Private attribute
        self.__balance = balance  # Private attribute

    def get_billing_info(self):
        return {
            "name": self.name,
            "email": self.email,
            "bank": self.bank,
            "card_number": "**** **** **** " + self.__card_number[-4:],  # Masked card number
            "billing_address": self.__billing_address,
        }

    def process_payment(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        return f"Payment of ${amount} processed. New balance: ${self.__balance}"

    def __str__(self):
        return f"""
        Name: {self.name}
        Email: {self.email}
        Bank: {self.bank}
        Card Number: {self.Card_number}
        Billing Address: {self.__billing_address}
        Balance: ${self.__balance}
        """
class CorporateAccount(BillingEntity):
    @abstractmethod
    def __init__(self, corporate_name: str, tax_bracket: str, bank: str, card_number: str, billing_address: str, balance: float):
        self.corporate_name = corporate_name
        self.tax_bracket = tax_bracket
        self.bank = bank
        self.__card_number = card_number  # Private attribute
        self.__billing_address = billing_address  # Private attribute
        self.__balance = balance  # Private attribute

    def get_billing_info(self):
        return {
            "corporate_name": self.corporate_name,
            "tax_bracket": self.tax_bracket,
            "bank": self.bank,
            "card_number": "**** **** **** " + self.__card_number[-4:],  # Masked card number
            "billing_address": self.__billing_address,
        }

    def process_payment(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        return f"Payment of ${amount} processed. New balance: ${self.__balance}"

    def __str__(self):
        return f"""
        Corporate Name: {self.corporate_name}
        Tax Bracket: {self.tax_bracket}
        Bank: {self.bank}
        Card Number: {self.Card_number}
        Billing Address: {self.__billing_address}
        Balance: ${self.__balance}
        """
