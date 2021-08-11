print("___________Welcome to console ERP system____________")
emp = []
while True:
    print("Press 1 for Add Employee  ")
    print("Press 2 for Delete Employee  ")
    print("Press 3 for Search Employee  ")
    print("Press 4 for Change Employee Data  ")
    print("Press 5 for Display  ")
    print("Press 6 for exit  ")
    ch = int(input("Enter your choice  "))
    if (ch == 1):
        name = input("Enter Employee name ")
        if name:
            emp.append(name)
    elif (ch == 2):
        name = input("Enter Employee name ")
        emp.remove(name)
    elif (ch == 3):
        name = input("Enter Employee name ")
        if name in emp:
            print(name , " is found in the list ")
        else:
            print(name," not in the list ")
    elif (ch == 4):
        name = input("Enter the name which do you want to change ")
        emp[emp.index(name)] = input("Enter new name ")
    elif (ch == 5):
        for i in emp:
            print((emp.index(i)+1)," . ",i)
    elif (ch == 6):
        break
    else:
        print("invalid choice ")

        