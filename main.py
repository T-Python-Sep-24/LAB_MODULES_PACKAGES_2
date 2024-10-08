import library.librarian as lib

library={}
print("Welcome to the library!")
while True:
    try:
        Choice=input("1-add a book\n2-remove a book\n3-check out a book\n4-return a book\n5-Display a book\n6-Exit\n")
        if Choice=='1':
            isbn=input("Enter the ISBN for the book you want to add: ")
            if not isbn:
                raise TypeError()
            if isbn in library:
                print(f"The book with ISBN {isbn} already exists in the library.\n")
                input("press any key to continue\n ")
            else:
             title=input("Enter Title: ")
             author=input("Enter Author: ")
             lib.add_book(library,title,author,isbn)
             input("press any key to continue\n ")
        elif Choice=='2':
            isbn=input("Enter the ISBN for the book you want to delete: ")
            if not isbn:
                raise ValueError()
            if isbn in library:
                lib.remove_book(library,isbn)
                input("press any key to continue\n ")
            else:
                print("Sorry there is no book with that ISBN")
                input("press any key to continue\n ")
        elif Choice=='3':
            isbn=input("Enter the ISBN for the book you want to borrow: ")
            if not isbn:
                raise ValueError()
            if isbn not in library :
                print("Sorry there is no book with that ISBN")
                input("press any key to continue\n ")
            elif library[isbn]['available']==False:
                print("The Book is not available")
                input("press any key to continue\n ")
            else:
                lib.check_out_book(library,isbn)
                input("press any key to continue\n ")
        elif Choice=='4':
            isbn=input("Enter the ISBN for the book you want to borrow: ")
            if not isbn:
                raise ValueError()
            if isbn not in library :
                print("Sorry there is no book with that ISBN")
                input("press any key to continue\n ")
            else:
                lib.return_book(library,isbn)
        elif Choice=='5':
            if library:
                lib.display_books(library)
                input("press any key to continue\n ")
            else:
                print("There is no books yet!")
                input("press any key to continue\n ")
        elif Choice=='6':
            print("Have a nice day!")
            break
        else:
            print("invalid input!")
            
    except ValueError:
        print("ISBN can not be empty! ")
    except Exception as e:
        print(e.__class__)
        print(e)
         
        

