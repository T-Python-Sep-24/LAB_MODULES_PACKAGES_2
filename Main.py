from Library.Librarian import * 
librarian = {}

#Add books
add_book(library, "A Little Life", "Hanya Yanagihara", "1447294831")
add_book(library, "The Secret History", "Tartt Donna", "0140167773")
add_book(library, "And Then There Were None", "Christie, Agatha", "0062073486")

print("\nAll the books:")
display_books(library)

print("\nChecking out a book:")
check_out_book(library, "1447294831")
check_out_book(library, "0140167773")

print("\nDisplaying all books after checkout:")
display_books(library)

print("\nReturning a book:")
return_book(library, "1447294831")

print("\nDisplaying all books after return:")
display_books(library)

print("\nRemoving a book:")
remove_book(library, "1447294831")

print("\nDisplaying all books after removal:")
display_books(library)