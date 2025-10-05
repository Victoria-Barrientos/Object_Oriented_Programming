# This is to illustrate encapsulation principles in OOP
# Shows how to safely protect, access and update attributes like balance.
# 👉 Challenge: Prevent direct access to sensitive attributes like __card_number.

class PersonaWithoutEncapsulation:
    def __init__(
            self,
            name: str,
            email: str,
            bank: str,
            card_number: str,
            billing_address: str,
            balance: float
        ):
        self.name = name
        self.email = email
        self.bank = bank
        self.card_number = card_number
        self.billing_address = billing_address
        self.balance = balance

    def __str__(self):
        return f"""
        Name: {self.name}
        Email: {self.email}
        Bank: {self.bank}
        Card Number: {self.card_number}
        Billing Address: {self.billing_address}
        Balance: ${self.balance}
        """

class PersonaWithEncapsulation:
    """
    Applying encapsulation principles -> Getters and Setters
    """
    def __init__(
            self,
            name: str,
            email: str,
            bank: str,
            card_number: str,
            billing_address: str,
            balance: float
        ):
        self.name = name
        self.email = email
        self.bank = bank
        # Safe guard card_number as a private attribute ==> __card_number       
        self.__card_number = card_number
        self.__billing_address = billing_address
        self.__balance = balance

        # Don't expose the card number directly - sensitive information
        # Instead, provide a method to get a masked version of the card number.    
        #        @property
        #        def Card_number(self):
        #            return self.__card_number
        
        @property #Getter but doesn't get the full card number
        def Card_number(self):
            return "**** **** **** " + self.__card_number[-4:]


        @Card_number.setter #Setter
        def Card_Number(self, value):
            if value.isdigit() and 13 <= len(value) <= 19:
                self.__card_number = value
            else: 
                print("Card number must be between 13 and 19 digits")
    def __str__(self):
        return f"""
        Name: {self.name}
        Email: {self.email}
        Bank: {self.bank}
        Card Number: {self.Card_number}  # Using the property to get masked card number
        Billing Address: {self.__billing_address}
        Balance: ${self.__balance}
        """