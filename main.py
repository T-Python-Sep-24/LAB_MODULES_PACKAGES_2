from library import librarian

booksDict = {
    "9780316769174": {
            "title": "The Catcher in the Rye", "author": "J.D. Salinger", "available": True
        },
    "9780446310789": {
        "title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True
    }
}

# add book then display books
librarian.add_book(booksDict, "1984", "George Orwell", "9780451524935")
librarian.display_books(booksDict)

# remove book then display books
librarian.remove_book(booksDict, "9780451524935")
librarian.display_books(booksDict)

# checkout a book then display books
librarian.check_out_book(booksDict, "9780316769174")
librarian.display_books(booksDict)


# return a book then display books
librarian.return_book(booksDict, "9780316769174")
librarian.display_books(booksDict)

