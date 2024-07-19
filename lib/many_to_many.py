class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        
        my_contracts = []

        for contract in Contract.all:
            if contract.author == self:
                my_contracts.append(contract)
        return my_contracts
                
    def books(self):
        
        my_books = []

        for books in Contract.all:
            if books.author == self:
                my_books.append(books.book)
        return my_books
                
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total




class Book:

    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        
        my_contracts = []

        for contract in Contract.all:
            if contract.book == self:
                my_contracts.append(contract)
        return my_contracts
                
    def authors(self):
        
        my_authors = []

        for authors in Contract.all:
            if authors.book == self:
                my_authors.append(authors.author)
        return my_authors
                


class Contract: 

    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def get_author(self):
        return self._author
    
    def set_author(self, value):
        if type(value) is Author:
            self._author = value
        else:
            raise Exception("Not Valid Author")
        
    author = property(get_author, set_author)

    def get_book(self):
        return self._book
    
    def set_book(self, value):
        if type(value) is Book:
            self._book = value
        else:
            raise Exception("Not Valid book")
        
    book = property(get_book, set_book)
    
    def get_date(self):
        return self._date
    
    def set_date(self,value):
        if type(value) is str:
            self._date= value
        else:
            raise Exception("Not valid date")

    date = property(get_date,set_date)

    def get_royalties(self):
        return self._royalties
    
    def set_royalties(self, value):
        if type(value) is int:
            self._royalties= value
        else:
            raise Exception("Not valid royalties")

    royalties = property(get_royalties,set_royalties)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
