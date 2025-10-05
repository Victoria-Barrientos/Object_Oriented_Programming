class Persona:
    """
    Persona as a base class for inheritance
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
        self.__card_number = card_number
        self.__billing_address = billing_address
        self.__balance = balance
    
    @property #Getter
    def Balance(self):
            return self.__balance
        
    @Balance.setter #Setter
    def Balance(self, value):
        if (value > 0):
            self.__balance = value
            print(f"Your new balance is: ${self.__balance}")
        else:
            raise ValueError("Balance cannot be negative")
        
    def __str__(self):
        return f"""
        Name: {self.name}
        Email: {self.email}
        Bank: {self.bank}
        Card Number: **** **** **** {self.__card_number[-4:]}
        Billing Address: {self.__billing_address}
        Balance: ${self.__balance}
        """

class Customer(Persona):
    # Customer inherits from Persona (Single Inheritance)
    def __init__(self, name, email, bank, card_number, billing_address, balance, loyalty_points):
        super().__init__(name, email, bank, card_number, billing_address, balance)
        self.loyalty_points = loyalty_points

    @property
    def Loyalty_points(self):
        return self.loyalty_points
    
    @Loyalty_points.setter
    def Loyalty_points(self, value):
        if value >= 0:
            self.loyalty_points = value
        else:
            raise ValueError("Loyalty points cannot be negative")
        
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}\nLoyalty Points: {self.loyalty_points}"
    
class Employee(Persona):
    # Employee inherits from Persona (Single Inheritance)
    def __init__(self, name, email, bank, card_number, billing_address, balance, employee_id):
        super().__init__(name, email, bank, card_number, billing_address, balance)
        self.__employee_id = employee_id

    @property
    def Employee_id(self):
        return self.__employee_id
    
    @Employee_id.setter
    def Employee_id(self, value):
        if value:
            self.__employee_id = value
        else:
            raise ValueError("Employee ID cannot be empty")
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}\nEmployee ID: {self.__employee_id}"
    
class Manager(Employee):
    # Manager inherits from Employee (Multilevel Hierarchical Inheritance)
    def __init__(self, name, email, bank, card_number, billing_address, balance, employee_id, department):
        super().__init__(name, email, bank, card_number, billing_address, balance, employee_id)
        self.department = department

    @property
    def Department(self):
        return self.department
    
    @Department.setter
    def Department(self, value):
        if value:
            self.department = value
        else:
            raise ValueError("Department cannot be empty")
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}\nDepartment: {self.department}"

class Discount:
    # Mixin class for discount functionality
    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.discount_percentage = discount_percentage
        else:
            raise ValueError("Discount percentage must be between 0 and 100")
        
class EmployeeWithDiscount(Employee, Discount):
    # EmployeeWithDiscount inherits from both Employee and Discount (Multiple Inheritance)
    def __init__(self, name, email, bank, card_number, billing_address, balance, employee_id, discount_percentage):
        Employee.__init__(self, name, email, bank, card_number, billing_address, balance, employee_id)
        Discount.__init__(self, discount_percentage)  