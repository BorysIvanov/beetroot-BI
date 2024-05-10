import phonebook_utils

def add_entry(phonebook, first_name, last_name, telephone, city, state):
    entry = {
        'first_name': first_name,
        'last_name': last_name,
        'telephone': telephone,
        'city': city,
        'state': state
    }
    phonebook.append(entry)
    return phonebook

def search_by_first_name(phonebook, first_name):
    return [entry for entry in phonebook if entry['first_name'] == first_name]

def search_by_last_name(phonebook, last_name):
    return [entry for entry in phonebook if entry['last_name'] == last_name]

def search_by_full_name(phonebook, full_name):
    return [entry for entry in phonebook if full_name in f"{entry['first_name']} {entry['last_name']}"]

def search_by_telephone(phonebook, telephone):
    return [entry for entry in phonebook if entry['telephone'] == telephone]

def search_by_city_or_state(phonebook, location):
    return [entry for entry in phonebook if location in f"{entry['city']} {entry['state']}"]

def delete_entry(phonebook, telephone):
    return [entry for entry in phonebook if entry['telephone'] != telephone]

def update_entry(phonebook, telephone, updated_entry):
    for entry in phonebook:
        if entry['telephone'] == telephone:
            entry.update(updated_entry)
            break
    return phonebook


if __name__ == "__main__":
    phonebook_filename = "phonebook.json"
    phonebook = phonebook_utils.load_data(phonebook_filename)

    while True:
        print("\nPhonebook Application")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete entry")
        print("8. Update entry")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            telephone = input("Enter telephone number: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            phonebook = add_entry(phonebook, first_name, last_name, telephone, city, state)
            print("Entry added successfully.")

        elif choice == '2':
            first_name = input("Enter first name to search: ")
            results = search_by_first_name(phonebook, first_name)
            print("Search results:")
            for entry in results:
                print(entry)

        elif choice == '3':
            last_name = input("Enter last name to search: ")
            results = search_by_last_name(phonebook, last_name)
            print("Search results:")
            for entry in results:
                print(entry)

        elif choice == '4':
            full_name = input("Enter full name to search: ")
            results = search_by_full_name(phonebook, full_name)
            print("Search results:")
            for entry in results:
                print(entry)

        elif choice == '5':
            telephone = input("Enter telephone number to search: ")
            results = search_by_telephone(phonebook, telephone)
            print("Search results:")
            for entry in results:
                print(entry)

        elif choice == '6':
            location = input("Enter city or state to search: ")
            results = search_by_city_or_state(phonebook, location)
            print("Search results:")
            for entry in results:
                print(entry)

        elif choice == '7':
            telephone = input("Enter telephone number to delete: ")
            phonebook = delete_entry(phonebook, telephone)
            print("Entry deleted successfully.")

        elif choice == '8':
            telephone = input("Enter telephone number to update: ")
            first_name = input("Enter updated first name: ")
            last_name = input("Enter updated last name: ")
            city = input("Enter updated city: ")
            state = input("Enter updated state: ")
            updated_entry = {'first_name': first_name, 'last_name': last_name, 'city': city, 'state': state}
            phonebook = update_entry(phonebook, telephone, updated_entry)
            print("Entry updated successfully.")

        elif choice == '9':
            phonebook_utils.save_data(phonebook_filename, phonebook)
            print("Exiting Phonebook Application.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

