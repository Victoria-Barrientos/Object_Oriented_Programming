from encapsulation import PersonaWithEncapsulation, PersonaWithoutEncapsulation
from validation import PersonaWithValidation, PersonaWithoutValidation
from inheritance import Persona, Customer, Employee, Manager, Discount, EmployeeWithDiscount
from relationship_types import Author, Book, Library, Borrower
from polymorphism import CreditCard, CryptoWallet, make_payment
from abstraction import IndividualPersona, CorporateAccount

def seed_encapsulation():
    unprotected_persona = PersonaWithoutEncapsulation(
        name="Jane Black",
        email="janeblack@example.com",
        bank="Bank of New York",
        card_number="1234567890123456",
        billing_address="456 Elm St, Barbie Town, USA",
        balance=-50.0
    )

    protected_persona = PersonaWithEncapsulation(
        name="Victoria Barrientos",
        email="viictoriab@example.com",
        bank="Bank of America",
        card_number="9876543210987654",
        billing_address="789 Oak St, Fashion City, USA",
        balance=150.0
    )

    print("=== Unprotected information => Persona Without Encapsulation ===")
    print(unprotected_persona)
    print("\n=== Protected information => Persona With Encapsulation ===")
    print(protected_persona)
    pass

def seed_validation():

    invalid_persona_no_validation = PersonaWithoutValidation(
        "Martina",
        "marti@gmail.com",
        "Galicia",
        "125-680-112", # Invalid card number
        "123 Main St",
        2023.48
        )
    
    invalid_persona_with_validation = PersonaWithValidation(
        "Delicia",
        "delicia@example.com",
        "Santander",
        "1234", # Invalid card number
        "456 Elm St",
        1500.00
        )

    print("=== Persona Without Validation ===")
    print(invalid_persona_no_validation)

    print("\n=== Persona With Validation ===")
    print(invalid_persona_with_validation)
    # Testing the balance setter with negative value
    try:
        invalid_persona_with_validation.Balance = -300.00
    except ValueError as e:
        print(f"Error: {e}")
    pass    

def seed_inheritance():

    parent_class_persona = Persona("Victoria", "viictoriabarrientos@example.com", "Bank of Python", "1234567812345678", "123 Python St", 1000.0)
    print(parent_class_persona)

    child_class_customer = Customer("Delicia", "deliciavega@example.com", "Chase", "8765432187654321", "456 Java Ave", 500.0, 150)
    print(child_class_customer)

    child_class_employee = Employee("Martina", "martibe@example.com", "Wells Fargo", "1122334455667788", "789 C# Blvd", 1200.0, "E123")
    print(child_class_employee)

    multi_level_inheritance_class_manager = Manager("Aimara Malen", "aimara22@example.com", "Citibank", "9988776655443322", "654 Go Ln", 2500.0, "E789", "Sales")
    print(multi_level_inheritance_class_manager)

    discount_class = Discount()
    print(discount_class)

    multiple_inheritance_class_employee_w_discount = EmployeeWithDiscount("Luna", "lunacascabelera@example.com", "Bank of Code", "4433221100112233", "321 Ruby Rd", 1300.0, "E456", 15)
    print(multiple_inheritance_class_employee_w_discount)

    discounted_price = discount_class.apply_discount(200, 10)  # 10% discount
    print(f"Discounted Price: ${discounted_price}")
    
    child_class_customer.Balance = 750.0  # Update balance using setter
    child_class_customer.Loyalty_points = 200  # Update loyalty points using setter
    print(f"Updated Balance to ${child_class_customer.Balance}. Bonus of Loyalty Points: {child_class_customer.Loyalty_points}")

    child_class_employee.Balance = 750.0  # Update balance using setter
    print(f"Updated Balance to ${child_class_customer.Balance} for Employee ID: {child_class_employee.Employee_id}")

    multi_level_inheritance_class_manager.Balance = 3000.0  # Update balance using setter
    multi_level_inheritance_class_manager.Department = "Marketing"  # Update department using setter
    print(f"Updated Balance to ${multi_level_inheritance_class_manager.Balance} for Manager of Department: {multi_level_inheritance_class_manager.Department}")

    multiple_inheritance_class_employee_w_discount.Balance = 1600.0  # Update balance using setter
    multiple_inheritance_class_employee_w_discount.Loyalty_points = 350  # Update loyalty points using setter
    print(f"Updated Balance to ${multiple_inheritance_class_employee_w_discount.Balance} with Loyalty Points: {multiple_inheritance_class_employee_w_discount.Loyalty_points} for Employee ID: {multiple_inheritance_class_employee_w_discount.Employee_id}")
    multiple_inheritance_class_employee_w_discount.apply_discount(20)  # Apply a 20% discount
    print(f"Applied a discount of {multiple_inheritance_class_employee_w_discount.discount_percentage}%")
    pass

def seed_relationship_types():
        
    author1 = Author("Simone de Beauvoir")
    author2 = Author("Jane Austen")

    book1 = Book("All Men Are Mortal", author1)
    book2 = Book("She Came To Stay", author1)
    book3 = Book("Pride and Prejudice", author2)

    library = Library("Fatima Al-Qarawiyyin Library")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    borrower = Borrower("Victoria Barrientos")

    book2.borrow(borrower)
    print(f"{borrower.name} borrowed: {[b.title for b in borrower.borrowed_books]}")
    book2.return_book()
    print(f"{borrower.name} borrowed after return: {[b.title for b in borrower.borrowed_books]}")

    jane_austen_books = library.find_books_by_author(author2)
    print(f"Books by {author2.name}: {[b.title for b in jane_austen_books]}")
    pass

def seed_polymorphism():

    # Simulating payment processing with different payment methods
    cc = CreditCard("Bank of Python", "1234567890123456", "123 Python St", 1000.0)
    cw = CryptoWallet("1A2b3C4d5E6f7G8h9I0j", 2.5)  # Balance in BTC

    print(cc)
    print(cw)

    # Using the same interface to process payments
    make_payment(cc, 150.0)  # CreditCard
    make_payment(cw, 0.5)    # CryptoWallet

    print(f"Remaining CreditCard Balance: ${cc.balance}")
    print(f"Remaining CryptoWallet Balance: {cw.balance} BTC")
    
    # Simulating a queue of different payment methods
    payment_queue = [
        CreditCard("Bank A", "1111222233334444", "456 Java Ave", 500.0),
        CryptoWallet("3F4g5H6i7J8k9L0m1N2o", 1.0),
        CreditCard("Bank B", "5555666677778888", "789 C# Blvd", 300.0),
        CryptoWallet("4G5h6I7j8K9l0M1n2O3p", 0.75),
        CreditCard("Bank C", "9999000011112222", "101 Swift St", 800.0)
    ]

    # Using the same method to process payments from the queue
    for method in payment_queue:
        method.process_payment(amount=100 if isinstance(method, CreditCard) else 0.1)
        print(f"Updated Balance: {method.balance if isinstance(method, CreditCard) else method.balance} {'USD' if isinstance(method, CreditCard) else 'BTC'}")
        pass
    pass

def seed_abstraction():

    individual = IndividualPersona("Morena", "morenita@example.com", "Bank of Abstraction", "1234567890123456", "123 Abstract St", 2000.0)
    print(individual)   

    corporate = CorporateAccount("Tech Corp", "A", "Corporate Bank", "6543210987654321", "456 Corporate Ave", 10000.0)
    print(corporate)

    # Demonstrating abstract methods
    individual.get_billing_info() # getter method
    individual.process_payment(500.0) # setter method

    corporate.get_billing_info() # getter method
    corporate.process_payment(2500.0) # setter method

    pass