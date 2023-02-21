from admin_panel import *

class Main:

    def __init__(self, admin):
        self.admin = admin

    def execute(self, choice):

    
        try:
            if choice == 1:
                print("***************Admin Login *****************")

                username = input("enter your usename:")
                password = input("enter your password:")
                flag = self.admin.admin_login(username, password)
                if flag:
                    print("Logged In Successfully")

                    while True:

                        choice = int(input("Enter \n1. Add module \n2.Add Students\n3.Add Trainer"))

                        if choice == 1:
                            print("Add Module")
                            module_name = input("Enter module name:")
                            duration = input("Enter duration time")
                            # total_module_dict = {}
                            
                            total_module_dict = self.admin.add_module(module_name, duration)
                            
                            print(total_module_dict)


                        elif choice == 2:
                            print("**********Add students ***************")
                            stud_details = self.admin.add_student()
                            print("student details that is added", stud_details)

                else:
                    print("Invalid credentials")

        except Exception as e:
            raise e


admin = AdminPanel()
main = Main(admin)
main.execute(1)