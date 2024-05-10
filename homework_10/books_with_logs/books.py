import datetime


BOOKS = [
    {
        "name": "Dune",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 896,
        "entry_added": datetime.datetime(2023, 11, 15, 12, 13, 14),
    },
    {
        "name": "Dune Messiah",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 256,
        "entry_added": datetime.datetime(2023, 12, 16, 20, 0, 11),
    },
    {
        "name": "Murder on the Orient Express",
        "author": " Agatha Christie",
        "genre": "Crime novel",
        "pages": 256,
        "entry_added": datetime.datetime(2021, 10, 30, 7, 43, 28),
    },
]


def display_books():
    for book in BOOKS:
        print(f"{book['name']} by {book['author']} is {book['genre']} and has {book['pages']} pages\n" + "="*60)



def add_book():
    book_name = input("Enter a book name: ")
    while not book_name:
        book_name = input("Please enter a book name: ")

    book_author = input("Enter a book author: ")
    while not book_author:
        book_author = input("Please enter a book author: ")

    book_genre = input("Enter a book genre: ")
    while not book_genre:
        book_genre = input("Please enter a book genre: ")

    book_pages = input("Enter book pages: ")

    if book_pages.isdigit():
        book_pages = int(book_pages)
    else:
        book_pages = None

    entry_added = datetime.datetime.now()
    BOOKS.append(
        {
            "name": book_name,
            "author": book_author,
            "genre": book_genre,
            "pages": book_pages,
            "entry_added": entry_added
        }
    )
    print(f"Book: '{book_name}' added successfully")


