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
    def apply_discount(self, amount, discount_percentage):
        if 0 <= discount_percentage <= 100:
            discount_amount = (discount_percentage / 100) * amount
            return amount - discount_amount
        else:
            raise ValueError("Discount percentage must be between 0 and 100")
        
class EmployeeWithDiscount(Employee, Discount):
    # EmployeeWithDiscount inherits from both Employee and Discount (Multiple Inheritance)
    def __init__(self, name, email, bank, card_number, billing_address, balance, employee_id, amount, discount_percentage):
        Employee.__init__(self, name, email, bank, card_number, billing_address, balance, employee_id)
        Discount.__init__(self, amount, discount_percentage)  

# Example usage
if __name__ == "__main__":
    p = Persona("Victoria", "viictoriabarrientos@example.com", "Bank of Python", "1234567812345678", "123 Python St", 1000.0)
    print(p)

    c = Customer("Delicia", "deliciavega@example.com", "Chase", "8765432187654321", "456 Java Ave", 500.0, 150)
    print(c)

    e = Employee("Martina", "martibe@example.com", "Wells Fargo", "1122334455667788", "789 C# Blvd", 1200.0, "E123")
    print(e)

    m = Manager("Nala", "nalita22@example.com", "Citibank", "9988776655443322", "654 Go Ln", 2500.0, "E789", "Sales")
    print(m)

    d = Discount()

    ewd = EmployeeWithDiscount("Luna", "lunacascabelera@example.com", "Bank of Code", "4433221100112233", "321 Ruby Rd", 1300.0, "E456", 300, 15)
    print(ewd)

    discounted_price = d.apply_discount(200, 10)  # 10% discount
    print(f"Discounted Price: ${discounted_price}")

    
    
    print(f"Manager's Department: {m.Department}")
    print(f"Customer's Balance before update: ${c.Balance}")
    c.Balance = 750.0  # Update balance using setter
    print(f"Customer's Balance after update: ${c.Balance}")
    print(f"Employee's ID: {e.Employee_id}")
    print(f"Customer's Loyalty Points before update: {c.Loyalty_points}")
    c.Loyalty_points = 200  # Update loyalty points using setter
    print(f"Customer's Loyalty Points after update: {c.Loyalty_points}")
    print(f"Employee's Card Number (masked): {e.Card_number}")
    print(f"Manager's Card Number (masked): {m.Card_number}")
    print(f"Manager's Employee ID: {m.Employee_id}")
    print(f"Manager's Balance before update: ${m.Balance}")
    m.Balance = 3000.0  # Update balance using setter
    print(f"Manager's Balance after update: ${m.Balance}")
    print(f"Manager's Department before update: {m.Department}")
    m.Department = "Marketing"  # Update department using setter
    print(f"Manager's Department after update: {m.Department}")
    print(f"Employee's Balance before update: ${e.Balance}")
    e.Balance = 1500.0  # Update balance using setter
    print(f"Employee's Balance after update: ${e.Balance}")
    print(f"Persona's Card Number (masked): {p.Card_number}")
    print(f"Persona's Balance before update: ${p.Balance}")
    p.Balance = 1100.0  # Update balance using setter
    print(f"Persona's Balance after update: ${p.Balance}")
    print(f"Persona's Card Number (masked): {p.Card_number}")

    print(f"Persona's Email: {p.email}")
    print(f"Customer's Email: {c.email}")
    print(f"Employee's Email: {e.email}")
    print(f"Manager's Email: {m.email}")