menu = '''
1 - Show menu
2 - Add
3 - Edit
4 - Remove
5 - Search
0 - quit the program
'''
print(menu)

contact_dictionary = {}
choice = input('Enter your choice: ')
end = False

while True:

    if choice == '0':
        answer = input('Are you sure you wanto to exit? (y, N): ')
        while True:
            if answer == 'y':
                print('exiting program...')
                end = True
                break
            elif answer == 'N':
                choice = input('Enter your choice: ')
                break
            else:
                print('Choose the right option!')
                answer = input('Are you sure you want to exit? (y, N): ')
    
    if end is True:
        break

    if choice == '1':
        print(menu)

    if choice == '2':
        person_first_name = input('Enter person first name: ')
        person_last_name = input('Enter person last name: ')
        person_phone_number = input('Enter person phone number: ')
       
        if person_first_name.isalnum() \
                and person_last_name.isalnum() \
                and person_phone_number.isdigit():

            if person_first_name not in contact_dictionary:
                contact_dictionary[person_first_name] = [person_last_name, person_phone_number]
                print(f'{person_first_name} {person_last_name} added to contacts')

        else:
            print('Enter valid fields! Try again!')

    if choice == '3':
        person_first_name = input('Enter person first name you want to edit: ')

        if person_first_name in contact_dictionary:
            new_first_name = input('Enter new first name: ')
            new_last_name = input('Enter new last name: ')
            new_phone_number = input('Enter new phone number: ')
            contact_dictionary[new_first_name] = contact_dictionary.pop(person_first_name)
            contact_dictionary[new_first_name] = [new_last_name, new_phone_number] 
            print('Successfully edit contact!')
        else:
            print('Enter a valid name')

    if choice == '4':
        person_first_name = input('Enter person first name you want to delete: ')
        if person_first_name in contact_dictionary:
            contact_dictionary.pop(person_first_name)
            print(f'{person_first_name} has been removed from contact list.')
        else:
            print('Enter a valid name')

    if choice == '5':
        person_first_name = input('Enter person first name: ')
        if person_first_name in contact_dictionary:
            fullname = person_first_name + ' ' + contact_dictionary[person_first_name][0]
            phonenumber = contact_dictionary[person_first_name][1]
            print(f'{fullname} -> {phonenumber}')

        else:
            print('Enter a valid name')

    choice = input('Enter your choice: ')

print()
if end is True: 
    if len(contact_dictionary) > 0:
        sorted_contact_dictionary = dict(sorted(contact_dictionary.items(), key=lambda first_name: first_name[0]))
        print('Contact list:')
        print('Name:                  Phonenumber:')
        for first_name, last_name_and_phone_number in sorted_contact_dictionary.items():
            last_name = last_name_and_phone_number[0]
            phonenumber = last_name_and_phone_number[1]
            fullname = first_name + ' ' + last_name
            print(f'{fullname}         {phonenumber}')
    else:
        print('Contact list is empty!')
