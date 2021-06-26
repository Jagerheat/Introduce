import json

def print_menu():
    print('1. Print Contact')
    print('2. Create Contact')
    print('3. Delete Contact')
    print('4. Search Contact')
    print('5. Quit')
   
numbers = {}

menu_choice = 0

print_menu()

while menu_choice != 5:
    
    menu_choice = int(input("Choise number (1-5): "))
    
    if menu_choice == 1:
        print("Contact:")
        for n in numbers.keys():
            print("Name_Surname: ", n, "\tPhone:", numbers[n])
        print()

    elif menu_choice == 2:
        print("Add: Name_Surname, Phone, City")
        name = input("Name_Surname: ")
        phone = input("Phone: ")
        city = input("City: ")
        numbers[name] = phone and city
        #numbers[name] = city

    elif menu_choice == 3:
        print("Remove Name_Surname and Phone and City")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]

        else:
            print(name, "oops")

    elif menu_choice == 4:
        print("Search")
        name = input("Name_Surname: ")
        if name in numbers:
            print("Phone", numbers[name])
        
        else:
            print(name, "oops")

    elif menu_choice != 5:
        print_menu()


def write_json(numbers_dict):
	try:
		data = json.load(open('people.json'))
	except:
		data = {}

	data.append(numbers_dict)

	with open('people.json', 'w') as file:
		json.dump(data, file)


def main():

	for i in range(5):
		write_json(print_menu())

