from employee import emp


def change_menu():
    print("\nPress 1 for change name ")
    print("Press 2 for change age ")
    print("Press 3 for change gender ")
    print("Press 4 for change salary \n")

def change_name(serial):
    newname = input("Enter new name for the employee ")
    emp[serial].name = newname
def change_age(serial):
    newage = int(input("Enter the new age "))
    emp[serial].age = newage
def change_gender(serial):
    newgender = input("Enter gender ")
    emp[serial].gndr = newgender
def change_salary(serial):
    newsal = input("Enter new salary ")
    emp[serial].slry = newsal