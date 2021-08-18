from employee import display_employee,emp


org = {}
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
            name_string = name_string +"|"+emp[i].name
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