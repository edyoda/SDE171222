import random
from student import *

class AdminPanel:

    def __init__(self):
        self.total_module_dict = {}
        self.student_details = {}

    def admin_login(self, username, password):
        if username == "admin" and password == "admin":
            return True
        return False

    def add_module(self, module_name, duration):
        topic_list = []
        
        
        topic_size = int(input("Enter the no. of topics for this module:"))
        for i in range(topic_size):
            topic = input("enter topic name:")
            topic_list.append(topic)


        module_data = {
            "module_name": module_name,
            "duration": duration,
            "topics": topic_list
        }

        self.total_module_dict[module_name]= module_data
        print("printitng from inside total module dict function", self.total_module_dict)
        return self.total_module_dict


    def add_student(self):
        
        student_size = int(input("enter the number of students to be added:"))

        for i in range(1, student_size+1):
            print("Enter details of students below as asked:")
            name = input("enter name:")
            gender = input("enter gender:")
            age = input("enetr age:")
            mobile_no = input("enetr mobile no.")
            email = input("enter email")
            password = input("enter student pwd")
            student = Student(i, name, gender, age, mobile_no, email, password)

            student_dict = {'ID': i, 'name': name, 'gender': gender, 'age': age, 
                            'mobile_no': mobile_no, 'email': email, 'pwd': password}
            
            self.student_details[i] = student_dict
        # print("printing student details:", self.student_details)

        return self.student_details
            






ap = AdminPanel()
x= ap.admin_login("abc", "abc")
print(x)