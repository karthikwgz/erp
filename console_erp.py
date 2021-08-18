import org
import teams
import employee as emp


def menu():
    print("\nPress 0 for organization menu \t  Press 1 for Add Employee \t Press 2 for Delete Employee ")
    print("Press 3 for Search Employee \t  Press 4 for Change Employee  \t Press 5 for Display ")
    print("Press 6 for Manage Teams \t  Press 7 for exit  ")
    print("\n_______________________________________________\n")

print("___________Welcome to console ERP system____________")

while True:
    menu()
    ch = int(input("Enter your choice  "))
    print("")
    if(ch == 0):
        org.org_process()
    elif (ch == 1):
        emp.add_employee()
    elif (ch == 2):
        emp.delete_employee()
    elif (ch == 3):
        emp.search_employee()
    elif (ch == 4):
        serial = int(input("Enter serial no "))
        print(emp.emp.keys())
        if serial not in emp.emp.keys():
            print("Invalid serial no")
        else:
            emp.change_menu()
            cho = int(input("Enter an option"))
            if (cho == 1):
                emp.change_name(serial)
            elif (cho == 2):
                emp.change_age(serial)
            elif (cho == 3):
                emp.change_gender(serial)
            elif (cho == 4):
                emp.change_salary(serial)
            else:
                print("invalid choice")

    elif (ch == 5):
        emp.display_employee()
    elif (ch ==6):
        teams.manage_all_team()
    elif (ch == 7):
        break
    else:
        print("invalid choice ")

        