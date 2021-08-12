print("___________Welcome to console ERP system____________")
emp = {}
while True:

    print("\nPress 1 for Add Employee  ")
    print("Press 2 for Delete Employee  ")
    print("Press 3 for Search Employee  ")
    print("Press 4 for Change Employee Data  ")
    print("Press 5 for Display  ")
    print("Press 6 for exit  ")
    print("\n_______________________________________________\n")
    ch = int(input("Enter your choice  "))
    print("")
    if (ch == 1):
        serial = int(input("Enter the serial number "))
        if serial not in emp.keys():
            name = input("Enter Employee name ")
            gender = input("Enter Employee gender ")
            age = int(input("Enter Employee age "))
            place = input("Enter Employee place ")
            slry = input("Enter salary ")
            pcmpny = input("Enter Previous Company name ")
            date = input("Enter joining date ")
            temp = {
                "name":name,
                "age":age,
                "gender":gender,
                "place":place,
                "slry":slry,
                "pcmpny":pcmpny,
                "date":date,
            }
            emp[serial] = temp
        else:
            print("serial No is already taken")

    elif (ch == 2):
        serial = int(input("Enter serial no "))
        if serial not in emp.keys():
            print("invalid serial number")
        else:
            del emp[serial]
    elif (ch == 3):
        name = input("Enter employee name")
        found  = False
        for val in emp.values():
            if (val['name'] == name):
                found = True
                print(f"{val['name']} | {val['age']} | {val['place']} ")
        if(found == False):
            print("not found")
    elif (ch == 4):
        serial = int(input("Enter serial no "))
        if serial not in emp.keys():
            print("Invalid serial no")
        else:
            print("\nPress 1 for change name ")
            print("Press 2 for change age ")
            print("Press 3 for change gender ")
            print("Press 4 for change salary \n")
            cho = int(input("Enter an option"))
            if (cho == 1):
                newname = input("Enter new name for the employee ")
                emp[serial]['name'] = newname
            elif (cho == 2):
                newage = int(input("Enter the new age "))
                emp[serial]['age'] = newage
            elif (cho == 3):
                newgender = input("Enter gender ")
                emp[serial]['gender'] = newgender
            elif (cho == 4):
                newsal = input("Enter new salary ")
                emp[serial]['slry'] = newsal
            else:
                print("invalid choice")

    elif (ch == 5):
            for serial,empl in emp.items():
                print(f"{serial} | {empl['name']} | {empl['age']} | {empl['place']} | {empl['slry']} | {empl['date']} | {empl['gender']}  | {empl['pcmpny']} ")

            #print((emp.index(i)+1)," . ",i)
    elif (ch == 6):
        break
    else:
        print("invalid choice ")

        