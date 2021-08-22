from employee import emp


def search_menu():
    print("\nPress 1 for Search by name ")
    print("Press 2 for search by age ")
    print("Press 3 for search by gender ")
    print("Press 4 for search by salary \n")

def search_employee():
    search_menu()
    ch = int(input("Enter choice"))
    if(ch == 1):
        name = input("Enter employee name")
        lst = list(filter(lambda x : str(x.name) == name , emp.values()))
        for i in lst:
            i.display()
    elif(ch == 2):
        age = int(input("Enter age"))
        lst = list(filter(lambda x : x.age == age ,emp.values()))
        for i in lst:
            i.display()
    elif(ch == 3):
        gender = input("Enter Employee gender")
        lst = list(filter(lambda x : x.gndr == gender , emp.values()))
        for i in lst:
            i.display()
    elif(ch == 4):
        slry = input("Enter employee salary")
        lst = list(filter(lambda x : int(x.slry) > slry , emp.values()))
        for i in lst:
            i.display()
    else:
        print("Invalid search")