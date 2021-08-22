from user import User


emp = {}
class Employee(User):
    
    def __init__(self,eid,name,age,gndr,plc,slry,pcm,dt,role):
        self.eid = eid
        self.name = name
        self.age = age
        self.gndr = gndr
        self.plc = plc
        self.slry = slry
        self.pcm = pcm
        self.dt = dt
        self._setuname()
        self._setpasswd()
        self.role = role

    def display(self):
        print(f"Employee Details are :  {self.name} | {self.age} | {self.gndr} | {self.plc} | {self.slry} | {self.pcm} | {self.dt} \n")

def add_employee():
    serial = int(input("Enter the serial number "))
    if serial not in emp.keys():
        eid = serial
        name = input("Enter Employee name ")
        age = int(input("Enter Employee age "))
        gender = input("Enter Employee gender ")
        place = input("Enter Employee place ")
        slry = input("Enter salary ")
        pcm = input("Enter Previous Company name ")
        date = input("Enter joining date ")
        role = input("Enter the role")
        emp[serial] = Employee(eid,name,age,gender,place,slry,pcm,date,role)
    else:
        print("serial No is already taken")

def delete_employee():
    serial = int(input("Enter serial no "))
    if serial not in emp.keys():
       print("invalid serial number")
    else:
        del emp[serial]

def display_employee():
    for serial,empl in emp.items():
        print("serial no : " ,serial)
        empl.display()