def who_do_you_know():
    # Ask for a list of people they know

    known_people = []
    known_people = input("Enter a list of people you know: ")

    return known_people


def ask_user():
    # Ask user for a name

    name = input("Enter the name of a person: ")
    return name


# see if the name is in the known people list
# print out if they know the person

a_list_of_people = who_do_you_know()
person = ask_user()

if person in a_list_of_people:
    print("You know {}!".format(person))
else:
    print("You dont know {} :(".format(person))
