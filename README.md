# Object_Oriented_Programming
Applying OOP principles in Python

📂 Project Structure

This project is a collection of small, focused Python scripts.
Each file (.py) demonstrates a different object-oriented programming (OOP) or Python best practice concept in isolation.

/project-root
│
├── encapsulation.py        # Encapsulation with getters & setters
├── validation.py           # Validation logic for credit cards & balance
├── inheritance.py          # Inheritance example (Persona → Customer/Employee)
├── relationship_types.py   # Relationship between classes (Association, Aggregation and Composition)
├── polymorphism.py         # Polymorphism with different behaviors
├── abstraction.py          # Abstraction with abstract base classes
└── README.md


🏆 Goals

Apply OOP pillars: encapsulation, validation, inheritance, polymorphism, abstraction.

Practice writing clean, maintainable Python code.

Understand how different OOP concepts build on one another.


1. encapsulation.py

Demonstrates encapsulation in Python.

Uses __private_attributes and @property getters/setters.

Shows how to safely access and update attributes like balance.


2. validation.py

Builds on encapsulation to add input validation.

Validates credit card number (13–19 digits).

Ensures balance cannot be negative.

Uses raise ValueError for invalid operations.

👉 Expected outcome: User creation should succeed only with valid input, and balance updates should never allow negatives.


3. inheritance.py

Introduces inheritance.

Persona becomes a base class.

New classes like Customer and Employee inherit from it.

👉 Challenge: Add role-specific attributes (e.g., Customer → loyalty_points, Employee → employee_id).


4. relationship_types.py

Demonstrates types of relationships.

Shows association, aggregation, and composition between classes.

- **Association:** Classes interact but do not own each other (e.g., Customer uses CreditCard).
- **Aggregation:** One class contains another as a part, but both can exist independently (e.g., Wallet holds multiple PaymentMethods).
- **Composition:** One class owns another, and their life cycles are tightly linked (e.g., Account creates and manages its TransactionHistory).

Illustrates how objects relate and collaborate in OOP design.
👉 Challenge: Model relationships in a library system.

- Association: The `Borrower` class interacts with `Book` by borrowing and returning books. Neither class owns the other; both can exist independently.
- Aggregation: The `Library` class aggregates `Book` objects. Books are added to the library, but they can exist outside of it and are not deleted if the library is removed.
- Composition: The `Book` class is composed with an `Author`. Each book is tightly linked to its author, and the author is managed as part of the book's lifecycle.


5. polymorphism.py

Demonstrates polymorphism.

Both Credit Card and Crypto Currency Wallet override a single method .process_payment()

Same method name, different outputs depending on the object type.

👉 Challenge: Create a list containing both `CreditCard` and `CryptoCurrencyWallet` objects. Loop through the list and call `.process_payment()` on each object. Observe how each class provides its own implementation, demonstrating polymorphism in action.


6. persona_abstraction.py

Shows abstraction using Python’s abc module.

Defines an abstract class BillingEntity with abstract methods.

Persona or its subclasses must implement those methods.

👉 Challenge: Create different billing entities (e.g., IndividualPersona, CorporateAccount) with different implementations of . ().