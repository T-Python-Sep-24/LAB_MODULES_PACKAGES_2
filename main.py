from library.librarian import *


mylibrary = {}

#add_book
add_book(mylibrary, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
add_book(mylibrary, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
add_book(mylibrary, "1984", "George Orwell", "9780451524935")


#display-----------------------------
print("_"*25 +'display_books'+"_"*25 +'\n')
display_books(mylibrary)


#check_out_book----------------------------
print("_"*25 +'check_out_book'+"_"*25 +'\n')
check_out_book(mylibrary, "9780316769174")


#display---------------------------------
print("_"*25 +'display_books'+"_"*25 +'\n')
display_books(mylibrary)


#return_book---------------------------------
print("_"*25 +'return_book'+"_"*25 +'\n')
return_book(mylibrary, "9780316769174") 


#remove_book--------------------------------
print("_"*25 +'remove_book'+"_"*25 +'\n')
remove_book(mylibrary,"888888")


#display------------------------------------
print("_"*25 +'display_books'+"_"*25 +'\n')
display_books(mylibrary)

print("_"*60 +'\n')
