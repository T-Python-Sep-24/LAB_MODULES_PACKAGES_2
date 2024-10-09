from library.librarian import *
import library.librarian as l


l.library["1984"] = {"title": "1984", "author": "George Orwell", "isbn": "7778", "available": True}
l.library["The Great Gatsby"] = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "1234", "available": True}
display_books(l.library)
add_book(l.library, "Brave New World", "Aldous Huxley", "5678")
add_book(l.library, "Brave New World", "Aldous Huxley", "5678")
display_books(l.library)
check_out_book(l.library, "7778")
check_out_book(l.library, "7778")
display_books(l.library)
return_book(l.library, "7778")
display_books(l.library)
remove_book(l.library, "1234")
display_books(l.library)
remove_book(l.library, "0000")
display_books(l.library)
