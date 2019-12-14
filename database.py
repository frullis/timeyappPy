from api import API
from config import Config
import pickle
import time
from datetime import datetime

class Database:


    #@staticmethod
    def saveDatabase(self, data):

        '''
        data = {
                "userdata": {"username": "markus.helin88@gmail.com", "password": "$argon2id$v=19$m=65536,t=3,p=2$c29tZXNhbHQ$RdescudvJCsgt3ub+b+dWRWJTmaaJObG"},
                "projects": [],
                "activity": None
                }
        '''
                
                
        
        with open('database.dat', 'wb') as f:
            pickle.dump(data, f)

    def setDefaultDatabase(self):
        
        data = {
                "userdata": {},
                "projects": [],
                "tasks": [],
                "activity": None
                }


        return data




    def readDatabase(self):
        data = None
        new_data = None
        new_data2 = None
 
        try:
            f = open('database.dat', 'rb')
            new_data = pickle.load(f)
            #print(new_data)
            return new_data
        except FileNotFoundError:

            data = self.setDefaultDatabase()
            with open('database.dat', 'wb') as f:
                print("yoyo")
                pickle.dump(data, f)
                return data
                #return new_data2
                #f.close()

        #return new_data

    #@staticmethod
    def saveUser(self,username, api_token, api_expire):

        #Sun, 12 Jan 2020 09:40:10 GMT
        #datetime_obj = datetime.strptime(api_expire, '%a, %d %b %Y %H:%M:%S %Z')
        datetime_obj = self.toDatetimeObject(api_expire)
        userdata = {"username": username, "api_token": api_token, "api_expire": datetime_obj}

        data = self.readDatabase()
        #print(data)
        data["userdata"] = userdata

        self.saveDatabase(data)

    def saveProjects(self, x):

        data = self.readDatabase()

        #print(x)
        new_list = []
        for _x in x:
            #print(_x)
            _x["created_at"] = self.toDatetimeObject(_x["created_at"])
            new_list.append(_x)
            
            #new_dict = _x
            #new_dict

        data["projects"] = new_list

        self.saveDatabase(data)
        #print(data)
    
    def saveTasks(self, x):
        data = self.readDatabase()
        data["tasks"] = x
        #y = data["tasks"]
        #y.append(x)

        #new_list = []
        #print(x)
        #for _x in x:
            #new_list.append(_x)
        
        #data["tasks"] = y
        self.saveDatabase(data)

    def toDatetimeObject(self,str_time):
        datetime_obj = datetime.strptime(str_time, '%a, %d %b %Y %H:%M:%S %Z')

        return datetime_obj


    def searchTask(self, project_id):

        data = self.readDatabase()

        my_list = []
        for _x in data["tasks"]:

            if _x["project_id"] == project_id:
                my_list.append(_x)

        return my_list




#x = Tools()

#x.saveDatabase()
#x.readDatabase()
