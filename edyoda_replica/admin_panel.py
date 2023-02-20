class AdminPanel:

    total_module_dict = {}

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

        total_module_dict[module_name]= module_data
        print("printitng from inside total module dict function", total_module_dict)
        return total_module_dict


ap = AdminPanel()
x= ap.admin_login("abc", "abc")
print(x)