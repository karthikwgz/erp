from employee import display_employee,emp
teams = {}
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
            name_string = name_string +"|"+emp[i].name
        print(f"{key} => {name_string}")

def process_team_menu():
    print("\t\t1.Add Member")
    print("\t\t2.Delete Member")
    print("\t\t3.display Members")

def add_team_member(team_name):
    display_employee()
    print(team_name)
    print(teams, "printing teams")
    eid = int(input("\t\t Enter Employee id "))
    if eid in emp.keys():
        teams[team_name].append(eid)
    else:
        print("\t\t invalid employee id")

def display_team_members(team_name):
    name_string = ""
    for i in teams[team_name]:
        name_string = name_string +"|"+str(i)+"."+str(emp[i].name)
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