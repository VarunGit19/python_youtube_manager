import sqlite3

connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               number TEXT NOT NULL
    )
''')

def list_contacts():
    cursor.execute("SELECT * from contacts")
    for row in cursor.fetchall():
        print(row)

def add_contact(name, number):
    cursor.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
    
    connection.commit()

def update_contact(contact_id, new_name, new_number):
    cursor.execute("UPDATE contacts SET name = ?, number = ? WHERE id = ?", (new_name, new_number, contact_id))

    connection.commit()

def delete_contact(contact_id):
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))

    connection.commit()

def main():

    while True:
        
        print("\n Contact Manager")
        print("1. List all contacts")
        print("2. Add a contact")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice: 
            case "1":
                list_contacts()

            case "2":
                name = input("Enter the name of contact: ")
                number = input("Enter the number of contact: ")
                add_contact(name, number)

            case "3":
                contact_id = input("Enter the id of contact to update: ")
                new_name = input("Enter the new name: ")
                new_number = input("Enter the new number: ")
                update_contact(contact_id, new_name, new_number)

            case "4":
                contact_id = input("Enter the id of contact to delete: ")
                delete_contact(contact_id)

            case "5":
                break
            
    connection.close()

if __name__ == "__main__":
    main()