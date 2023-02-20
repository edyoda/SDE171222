from admin_panel import *

class Main:

    def __init__(self, admin):
        self.admin = admin

    def execute(self, choice):

        if choice == 1:
            print("***************Admin Login *****************")

            username = input("enter your usename:")
            password = input("enter your password:")
            flag = self.admin.admin_login(username, password)
            if flag:
                print("Logged In Successfully")

                while True:

                    choice = int(input("Enter \n1. Add module \n2.Add trainer \n3.Add Students"))

                    if choice == 1:
                        print("Add Module")
                        module_name = input("Enter module name:")
                        duration = input("Enter duration time")
                        # total_module_dict = {}
                        
                        total_module_dict = self.admin.add_module(module_name, duration)

                        print(total_module_dict)

            else:
                print("Invalid credentials")


admin = AdminPanel()
main = Main(admin)
main.execute(1)