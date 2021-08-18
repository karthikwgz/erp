emp = {}
class Employee():
    
    def __init__(self,name,age,gndr,plc,slry,pcm,dt):
        self.name = name
        self.age = age
        self.gndr = gndr
        self.plc = plc
        self.slry = slry
        self.pcm = pcm
        self.dt = dt

    def display(self):
        print(f"Employee Details are :  {self.name} | {self.age} | {self.gndr} | {self.plc} | {self.slry} | {self.pcm} | {self.dt}")

def add_employee():
    serial = int(input("Enter the serial number "))
    if serial not in emp.keys():
        name = input("Enter Employee name ")
        age = int(input("Enter Employee age "))
        gender = input("Enter Employee gender ")
        place = input("Enter Employee place ")
        slry = input("Enter salary ")
        pcm = input("Enter Previous Company name ")
        date = input("Enter joining date ")
        emp[serial] = Employee(name,age,gender,place,slry,pcm,date)
    else:
        print("serial No is already taken")

def delete_employee():
    serial = int(input("Enter serial no "))
    if serial not in emp.keys():
        print("invalid serial number")
    else:
        del emp[serial]

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
            print(i.display())
    elif(ch == 2):
        age = int(input("Enter age"))
        lst = list(filter(lambda x : x.age == age ,emp.values()))
        for i in lst:
            print(i.display())
    elif(ch == 3):
        gender = input("Enter Employee gender")
        lst = list(filter(lambda x : x.gndr == gender , emp.values()))
        for i in lst:
            print(i.display())
    elif(ch == 4):
        slry = input("Enter employee salary")
        lst = list(filter(lambda x : int(x.slry) > slry , emp.values()))
        for i in lst:
            print(i.display())
    else:
        print("Invalid search")

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

def display_employee():
    for serial,empl in emp.items():
        print("serial no : " ,serial)
        print(empl.display())