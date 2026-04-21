books = {"python": True}

def issue(b):
    if books.get(b):
        books[b] = False

def return_book(b):
    books[b] = True
