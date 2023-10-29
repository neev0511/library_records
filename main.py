import mysql.connector
from passwords import get_password


def execute_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def getAllBooks():
    query = "SELECT book_id,book_name,student_id FROM library_records"
    result = execute_query(query)
    for row in result:
        print(str(row)[1:-1])


def getName(book_id):
    query = "SELECT student_id FROM library_records WHERE book_id = " + book_id
    result = execute_query(query)
    try:
        print(result[0][0])
    except:
        print("No book found")


def getAssignedBooks():
    query = "SELECT book_id,book_name,student_id FROM library_records WHERE student_id IS NOT NULL"
    result = execute_query(query)
    for row in result:
        print(str(row)[1:-1])


def getFreeBooks():
    query = "SELECT book_id,book_name FROM library_records WHERE student_id IS NULL"
    result = execute_query(query)
    for row in result:
        print(str(row)[1:-1])


def addBook(book_id, book_name):
    query = "INSERT INTO library_records(book_id,book_name,student_id) VALUES(" + \
        book_id+",'"+book_name+"',null)"
    # try:
    #     execute_query(query)
    #     print("Book Added")
    # except:
    #     print("Error occured")
    execute_query(query)


def assignBook(book_id, student_id):
    # Check if book is assigned
    query = "UPDATE library_records SET student_id = " + student_id + \
        "WHERE book_id = "+book_id+" AND student_id IS NULL"
    try:
        execute_query(query)
        print("Book Assigned")
    except:
        print("Error occured")


def freeBook(book_id):
    query = "UPDATE library_records SET student_id = NULL WHERE book_id = "+book_id
    try:
        execute_query(query)
        print("Book Free")
    except:
        print("Error occured")


def getBooksByStudentID(student_id):
    query = "SELECT book_id,book_name FROM library_records WHERE student_id = "+student_id
    result = execute_query(query)
    for row in result:
        print(str(row)[1:-1])


def deleteBook(book_id):
    query = "DELETE FROM library_records WHERE book_id="+book_id
    try:
        execute_query(query)
        print("Book Deleted")
    except:
        print("Error occured")


def start_DB_and_Table():
    cursor.execute("CREATE DATABASE IF NOT EXISTS LIBRARY;")
    cursor.execute("USE LIBRARY;")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS library_records(book_id int PRIMARY KEY, book_name varchar(255), student_id int)")


def show_menu():
    print("1. Get All Books")
    print("2. Get Name by Book ID")
    print("3. Get Assigned Books")
    print("4. Get Free Books")
    print("5. Add Book")
    print("6. Assign Book")
    print("7. Free Book")
    print("8. Get Book by Student ID")
    print("9. Delete Book")
    print("10. Exit")


if __name__ == "__main__":
    host, user, password = get_password()
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = conn.cursor()
    start_DB_and_Table()

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            getAllBooks()
        elif choice == 2:
            book_id = input("Enter book ID: ")
            getName(book_id)
        elif choice == 3:
            getAssignedBooks()
        elif choice == 4:
            getFreeBooks()
        elif choice == 5:
            # NOT WORKING
            book_id = input("Enter book ID: ")
            book_name = input("Enter book name: ")
            addBook(book_id, book_name)
        elif choice == 6:
            book_id = input("Enter book ID: ")
            student_id = input("Enter student ID: ")
            assignBook(book_id, student_id)
        elif choice == 7:
            book_id = input("Enter book ID: ")
            freeBook(book_id)
        elif choice == 8:
            student_id = input("Enter Student ID: ")
            getBooksByStudentID(student_id)
        elif choice == 9:
            book_id = input("Enter book ID: ")
            deleteBook(book_id)
        elif choice == 10:
            break
        else:
            print("Invalid choice")
