import books
import logging

# Configure logging
logging.basicConfig(filename='books_logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    while True:
        user_menu = input("For 'Books list': Press '1'\n"
                          "To 'Add book': Press '2'\n"
                          "To quit program: Press '0'\n"
                          "Choose your options: ")

        if user_menu == "0":
            logging.info("User exited the program.")
            print("Good bye!")
            break
        elif user_menu == "1":
            logging.info("User requested to display books list.")
            books.display_books()
        elif user_menu == "2":
            logging.info("User requested to add a book.")
            books.add_book()
        else:
            logging.warning("User entered invalid input.")
            print("Invalid input! Try again!")

if __name__ == "__main__":
    main()