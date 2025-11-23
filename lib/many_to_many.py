# many_to_many.py

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all.append(self)

    def contracts(self):
        """Return a list of all Contract instances associated with this author."""
        return self._contracts

    def books(self):
        """Return a list of all Book instances associated with this author via contracts."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Sign a contract linking this author to a book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the sum of royalties from all contracts for this author."""
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all.append(self)

    def contracts(self):
        """Return a list of all Contract instances associated with this book."""
        return self._contracts

    def authors(self):
        """Return a list of all Author instances associated with this book via contracts."""
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author")
        if not isinstance(book, Book):
            raise TypeError("book must be a Book")
        if not isinstance(date, str):
            raise TypeError("date must be a str")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Link contract to author and book
        author._contracts.append(self)
        book._contracts.append(self)

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date=None):
        """Return all contracts sorted by date. If a date is provided, filter by that date."""
        sorted_contracts = sorted(cls.all, key=lambda c: c.date)
        if date is not None:
            sorted_contracts = [c for c in sorted_contracts if c.date == date]
        return sorted_contracts
