class Student:

    def __init__(self, ID, name, gender, age, mobile_no, email, password):
        self.ID = ID
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile_no = mobile_no
        self.email = email
        self.password = password

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender
    
    def set_gender(self, gender):
        self.gender = gender

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age


    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password

    

 

    

    