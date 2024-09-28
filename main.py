import psycopg2

connection = psycopg2.connect("dbname=number_book user=postgres password=2910")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users"
               "(id SERIAL PRIMARY KEY, "
               "name VARCHAR(50),"
               "second_name VARCHAR(50),"
               "phone INTEGER)")

print("Wcisnij 1 jezeli chcesz dodac nowy numer, "
      "2 jeżeli chcesz znaleźć konkretny numer,"
      " 3 jeżeli chcesz usunac numer,"
      "4 jeżeli chcesz wyswietlic wszystkie numery")

user_option = int(input("Co chcesz zrobić: "))

if user_option == 1:
    name = input("Wprowadz imie kontaktu: ")
    second_name = input("Wprowadzw nazwisko kontaktu:")
    phone_number = int(input("Podaj numer telefonu bez spacji"))

    cursor.execute("INSERT INTO users(name, second_name, phone) VALUES(%s, %s, %s)", (name, second_name, phone_number))

if user_option == 2:
    print("Jeżeli chcesz znaleźć po imieniu wpisz [i],"
          " jezeli chcesz znalezc po nazwisku wpisz [k], "
          "jezeli po numerze wpisz [n]")

    user_choice = input("Co chcesz zrobić: ")

    match user_choice:

        case "i":
            first_name = input("Wprowadź imię szuaknego numeru: ")
            cursor.execute("SELECT name, second_name, phone FROM users WHERE name = %s", (first_name,))
            print(cursor.fetchall())

        case "k":
            last_name = input("Wprowadź nazwisko szuaknego numeru: ")
            cursor.execute("SELECT name, second_name, phone FROM users WHERE second_name = %s", (last_name,))
            print(cursor.fetchall())

        case "n":
            phone = int(input("Wprowadź numer szuaknego numeru (bez spacji): "))
            cursor.execute("SELECT name, second_name, phone FROM users WHERE phone = %s", (phone,))
            print(cursor.fetchall())

if user_option == 3:
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
    user_id = input("Podaj id rekordu którego chcesz usunąć: ")
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))


if user_option == 4:
    cursor.execute("SELECT name, second_name, phone FROM users")
    cursor.fetchall()

connection.commit()
cursor.close()
connection.close()
