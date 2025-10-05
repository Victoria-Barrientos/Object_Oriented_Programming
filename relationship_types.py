# This file illustrates different types of relationships in OOP:
# Association, Aggregation, and Composition using a library system example.

from typing import List, Optional

class Author:
	"""Represents an author in the library system."""
	def __init__(self, name: str):
		self._name = name

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, value: str):
		if not value:
			raise ValueError("Author name cannot be empty.")
		self._name = value

class Book:
	"""Represents a book, composed with an Author (composition)."""
	def __init__(self, title: str, author: Author):
		self._title = title
		self._author = author
		self._borrower: Optional['Borrower'] = None

	@property
	def title(self) -> str:
		return self._title

	@title.setter
	def title(self, value: str):
		if not value:
			raise ValueError("Book title cannot be empty.")
		self._title = value

	@property
	def author(self) -> Author:
		return self._author

	@property
	def borrower(self) -> Optional['Borrower']:
		return self._borrower

	def borrow(self, borrower: 'Borrower'):
		if self._borrower is not None:
			raise Exception(f"Book '{self._title}' is already borrowed.")
		self._borrower = borrower
		borrower.borrow_book(self)

	def return_book(self):
		if self._borrower is None:
			raise Exception(f"Book '{self._title}' is not borrowed.")
		self._borrower.return_book(self)
		self._borrower = None

class Library:
	"""Represents a library, which aggregates books (aggregation)."""
	def __init__(self, name: str):
		self._name = name
		self._books: List[Book] = []

	@property
	def name(self) -> str:
		return self._name

	@property
	def books(self) -> List[Book]:
		return self._books

	def add_book(self, book: Book):
		self._books.append(book)

	def find_books_by_author(self, author: Author) -> List[Book]:
		return [book for book in self._books if book.author == author]

class Borrower:
	"""Represents a borrower who can borrow books (association)."""
	def __init__(self, name: str):
		self._name = name
		self._borrowed_books: List[Book] = []

	@property
	def name(self) -> str:
		return self._name

	@property
	def borrowed_books(self) -> List[Book]:
		return self._borrowed_books

	def borrow_book(self, book: Book):
		if book not in self._borrowed_books:
			self._borrowed_books.append(book)

	def return_book(self, book: Book):
		if book in self._borrowed_books:
			self._borrowed_books.remove(book)

def main():
	# Create authors
	author1 = Author("Simone de Beauvoir")
	author2 = Author("Jane Austen")

	# Create books (composition)
	book1 = Book("All Men Are Mortal", author1)
	book2 = Book("She Came To Stay", author1)
	book3 = Book("Pride and Prejudice", author2)

	# Create library and add books (aggregation)
	library = Library("Fatima Al-Qarawiyyin Library")
	library.add_book(book1)
	library.add_book(book2)
	library.add_book(book3)

	# Create borrower (association)
	borrower = Borrower("Victoria Barrientos")

	# Borrow and return books
	book2.borrow(borrower)
	print(f"{borrower.name} borrowed: {[b.title for b in borrower.borrowed_books]}")
	book2.return_book()
	print(f"{borrower.name} borrowed after return: {[b.title for b in borrower.borrowed_books]}")

	# Find books by author
	jane_austen_books = library.find_books_by_author(author2)
	print(f"Books by {author2.name}: {[b.title for b in jane_austen_books]}")

if __name__ == "__main__":
	main()