emp = {}
teams = {}
org = {}
print("___________Welcome to console ERP system____________")

def employee_menu():
    print("\nPress 0 for organization menu \t  Press 1 for Add Employee \t Press 2 for Delete Employee ")
    print("Press 3 for Search Employee \t  Press 4 for Change Employee  \t Press 5 for Display ")
    print("Press 6 for Manage Teams \t  Press 7 for exit  ")
    print("\n_______________________________________________\n")

def add_employee():
    serial = int(input("Enter the serial number "))
    if serial not in emp.keys():
        emp[serial] = {
            "name":input("Enter Employee name "),
            "age":int(input("Enter Employee age ")),
            "gender":input("Enter Employee gender "),
            "place":input("Enter Employee place "),
            "slry":input("Enter salary "),
            "pcmpny":input("Enter Previous Company name "),
            "date":input("Enter joining date "),
        }
    else:
        print("serial No is already taken")

def delete_employee():
    serial = int(input("Enter serial no "))
    if serial not in emp.keys():
        print("invalid serial number")
    else:
        del emp[serial]

def search_employee():
    name = input("Enter employee name")
    found  = False
    for val in emp.values():
        if (val['name'] == name):
            found = True
            print(f"{val['name']} | {val['age']} | {val['place']} ")
    if(found == False):
        print("not found")


def change_menu():
    print("\nPress 1 for change name ")
    print("Press 2 for change age ")
    print("Press 3 for change gender ")
    print("Press 4 for change salary \n")

def change_name():
    newname = input("Enter new name for the employee ")
    emp[serial]['name'] = newname
def change_age():
    newage = int(input("Enter the new age "))
    emp[serial]['age'] = newage
def change_gender():
    newgender = input("Enter gender ")
    emp[serial]['gender'] = newgender
def change_salary():
    newsal = input("Enter new salary ")
    emp[serial]['slry'] = newsal


def display_employee():
    for serial,empl in emp.items():
        print(f"{serial} | {empl['name']} | {empl['age']} | {empl['place']} | {empl['slry']} | {empl['date']} | {empl['gender']}  | {empl['pcmpny']} ")

def manage_team_menu():
    print("\t 1. create Team")
    print("\t 2. Display Team")
    print("\t 3. Manage Team")
    print("\t 4. Delete Team")
    print("")

def create_team():
    team_name = input("\t Enter team name")
    teams[team_name] = []

def display_team():
    for key,value in teams.items():
        name_string = ""
        for i in value:
            name_string = name_string +"|"+emp[i]["name"]
        print(f"{key} => {name_string}")

def process_team_menu():
    print("\t\t1.Add Member")
    print("\t\t2.Delete Member")
    print("\t\t3.display Members")

def add_team_member(team_name):
    display_employee()
    print(team_name)
    eid = int(input("\t\t Enter Employee id "))
    if eid in emp.keys():
        teams[team_name].append(eid)
    else:
        print("\t\t invalid employee id")

def display_team_members(team_name):
    name_string = ""
    for i in teams[team_name]:
        name_string = name_string +"|"+str(i)+"."+str(emp[i]["name"])
    print(f"{name_string}")

def delete_team_member(team_name):
    display_team_members(team_name)
    eid = int(input("\t\t Enter employee id "))
    if eid in teams[team_name]:
        teams[team_name].remove(eid)
    else:
        print("\t\t Invalid employee id")


def manage_particular_team():
    team_name = input("\t\t Enter team name ")
    process_team_menu()
    ch = int(input("\t\t Enter your choice "))
    if ch == 1:
        add_team_member(team_name)
    elif ch == 2:
        delete_team_member(team_name)
    elif ch == 3:
        display_team_members(team_name)
    else:
        print("\t Invalid choice")

def delete_team():
    team_name  = input("\t Enter Team name")
    if team_name in teams.keys():
        del teams[team_name]
        print("\t Team Deleted")
    else:
        print("\t Invalid team name")

def manage_all_team():
    while True:
        manage_team_menu()
        ch = int(input("Enter your choice"))
        if(ch == 1):
            create_team()
        elif(ch ==2):
            display_team()
        elif(ch==3):
            manage_particular_team()
        elif(ch == 4):
            delete_team()
        elif(ch == 5):
            break
        else:
            print("Invalid option")

def org_menu():
    print("\t 1. create an Organization \t 2. Manage Organization \t 3.Display Organization")
    print("\t 4. Delete Organization \t 5. Exit")

def create_org():
    or_name = input("Enter organization name")
    org[or_name] = []
    
def display_org():
    for key,val in org.items():
        name_string = ""
        for i in val:
            name_string = name_string +"|"+emp[i]["name"]
        print(f"{key} => {name_string}")
        
def delete_org():
    org_name = input("Enter organization name ")
    if org_name in org.keys():
        del org[org_name]
        print("Organization deleted")
    else:
        print("Organization not found")

def add_org_member(org_name):
    display_employee()
    eid = int(input("Enter Employee id"))
    if eid in emp.keys():
        org[org_name].append(eid)
    else:
        print("Employee not found")

def delete_org_member(org_name):
    display_employee()
    eid = int(input("Enter employee id"))
    if eid in emp.keys():
        org[org_name].remove(eid)
    else:
        print("Employee id is not found")

        


def manage_org():
    org_name = input("Enter the organization name")
    print("\t 1. Add member \t 2. Delete memeber")
    ch = int(input("Enter the choice"))
    if (ch == 1):
        add_org_member(org_name)
    elif (ch == 2):
        delete_org_member(org_name)
    else:
        print("Invalid choice")


def org_process():
    while True:
        org_menu()
        ch = int(input("Enter a choice"))
        if (ch == 1):
            create_org()
        elif (ch == 2):
            manage_org()
        elif (ch == 3):
            display_org()
        elif (ch == 4):
            delete_org()
        elif(ch == 5):
            break
        else:
            print("Invalid Choice")

while True:

    employee_menu()
    ch = int(input("Enter your choice  "))
    print("")
    if(ch == 0):
        org_process()
    elif (ch == 1):
        add_employee()
    elif (ch == 2):
        delete_employee()
    elif (ch == 3):
        search_employee()
    elif (ch == 4):
        serial = int(input("Enter serial no "))
        if serial not in emp.keys():
            print("Invalid serial no")
        else:
            change_menu()
            cho = int(input("Enter an option"))
            if (cho == 1):
                change_name()
            elif (cho == 2):
                change_age()
            elif (cho == 3):
                change_gender()
            elif (cho == 4):
                change_salary()
            else:
                print("invalid choice")

    elif (ch == 5):
        display_employee()
    elif (ch ==6):
        manage_all_team()
    elif (ch == 7):
        break
    else:
        print("invalid choice ")

        