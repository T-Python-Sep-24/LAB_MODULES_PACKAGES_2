from Library.Librarian import * 
librarian = {}

#Add books
add_book(library, "A Little Life", "Hanya Yanagihara", "1447294831")
add_book(library, "The Secret History", "Tartt Donna", "0140167773")
add_book(library, "And Then There Were None", "Christie, Agatha", "0062073486")

print("\nAll the Books You Have Added:")
display_books(library)

print("\nChecked Out Books:")
check_out_book(library, "1447294831")
check_out_book(library, "0140167773")

print("\nAll the Books You Have Checkout:")
display_books(library)

print("\nThe Returned Books:")
return_book(library, "1447294831")

print("\nAll the Books You Returned:")
display_books(library)

print("\nThe Removing Books:")
remove_book(library, "1447294831")

print("\nAll The Books After Your Removal:")
display_books(library)