# 🐍 Object Oriented Programming in Python

> Explored and mastered OOP concepts through hands-on Python scripts.  
> Each module demonstrates a core principle—encapsulation, validation, inheritance, relationships, polymorphism, and abstraction.

---

## 📦 Project Structure

```
/project-root
│
├── encapsulation.py         # Encapsulation: Getters & Setters
├── validation.py            # Input validation for credit cards & balance
├── inheritance.py           # Inheritance: Persona → Customer/Employee
├── relationship_types.py    # Relationships: Association, Aggregation, Composition
├── polymorphism.py          # Polymorphism: Unified interface, varied behaviors
├── abstraction.py   # Abstraction: Abstract base classes
└── README.md
```

---

## 🏆 Project Goals

- Apply OOP pillars: **Encapsulation**, **Validation**, **Inheritance**, **Polymorphism**, **Abstraction**
- Practice writing **clean**, **maintainable** Python code
- Understand how different OOP concepts build on one another

---

## 🗂️ Modules Overview

### 1️⃣ `encapsulation.py`  
Encapsulation in Python using private attributes and `@property` getters/setters.  
Safely access and update sensitive data (e.g., account balances).

---

### 2️⃣ `validation.py`  
Builds on encapsulation to implement input validation:  
- Validates credit card number (13–19 digits)  
- Disallows negative balances  
- Raises `ValueError` for invalid operations

**Challenge:**  
- User creation succeeds only with valid input  
- Balance updates never allow negatives

---

### 3️⃣ `inheritance.py`  
Introduces inheritance:  
- `Persona`: base class  
- `Customer` and `Employee`: subclasses with role-specific attributes  
  - `Customer`: `loyalty_points`
  - `Employee`: `employee_id`

---

### 4️⃣ `relationship_types.py`  
Demonstrates class relationships:  
- **Association:** Classes interact; neither "owns" the other (e.g., `Customer` uses `CreditCard`)
- **Aggregation:** One class contains another, but both can exist independently (e.g., `Wallet` holds multiple `PaymentMethods`)
- **Composition:** One class owns another; their lifecycles are tightly linked (e.g., `Account` manages its `TransactionHistory`)

**Library System Challenge:**
- **Association:** `Borrower` borrows/returns `Book` (no ownership)
- **Aggregation:** `Library` aggregates `Book` objects (books exist outside the library)
- **Composition:** `Book` is composed with `Author` (author managed as part of book's lifecycle)

---

### 5️⃣ `polymorphism.py`  
Polymorphism:  
- Unified method `.process_payment()` for different payment types  
- `CreditCard` and `CryptoCurrencyWallet` override `.process_payment()` with unique behaviors

**Challenge:**  
- Create a list of mixed payment objects  
- Loop through and call `.process_payment()`  
- Observe distinct outputs per class

---

### 6️⃣ `abstraction.py`  
Abstraction using Python’s `abc` module:  
- Defines abstract class `BillingEntity` with abstract methods  
- `Persona` or subclasses must implement these methods

**Challenge:**  
- Create billing entities (e.g., `IndividualPersona`, `CorporateAccount`)  
- Implement entity-specific billing logic

---

## 🚀 Get Started

Clone the repo and explore each script individually.  
Each file is self-contained and focuses on a single OOP concept, allowing you to learn by example.

---

## 💡 Learning Resources

- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [Python abc module](https://docs.python.org/3/library/abc.html)

---
If you also want to sharpen your 🐍 skills..
Fork this repo and happy Coding! 🎉
