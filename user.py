class User:
    def __init__(self,role):
        self.__uname = ""
        self.__passwd = ""
        self.role = role

    def _setuname(self):
        self.__uname = input("Enter the user name")
    def _setpasswd(self):
        self.__passwd = input("Enter the password")
    def _getuname(self):
        return self.__uname
    # def _getpasswd(self):
    #     return self.__passwd