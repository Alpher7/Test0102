my_library = {'A Farewell to Arms': 'Ernest Hemingway', 'The Old Man and the Sea': 'Ernest Hemingway', 'The Garden of Eden': 'Ernest Hemingway',
         'The Financier': 'Theodore Dreiser', 'The Titan': 'Theodore Dreiser', 'Crime and Punishment': 'Fyodor Dostoevsky', 'The Gambler': 'Fyodor Dostoevsky'}

while True:
    choice = input("Choose action: \n\t1. Show library \n\t2. Add book \n\t3. Remove book by name \n\t4. Remove books by writer \n\t5. Sort by book \n\t6. Sort by writer \n\t0. Exit\n")
    match choice:
        case "1":
            for book in my_library.items():
                print(book)
        case "2":
            book = input("Enter book: ")
            writer = input("Enter writer: ")
        case "3":
            book = input("Which book do you want to remove: ")
            my_library.pop(book)
        case "4":
            writer = input("Whose books do you want to remove: ")
            books_to_delete = []
            for key, value in my_library.items():
                if value == writer:
                    books_to_delete.append(key)
            for book in books_to_delete:
                del my_library[book]
        case "5":
            sorted_library = sorted(my_library.items(), key=lambda item: item[0])
            for book in sorted_library:
                print(book)
        case "6":
            sorted_library = sorted(my_library.items(), key=lambda item: item[1])
            for book in sorted_library:
                print(book)
        case "0":
            break
        case _:
            print("Wrong choice")

