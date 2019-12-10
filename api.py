import requests
from datetime import datetime
import logging

class API:

    api_endpoint = 'http://127.0.0.1:5000'
    timeout=5    
    

    def get_activity(self, api_token, start_date, end_date):

        headers = {'accept': 'application/json',
                'api_token': api_token}

        try:
            req = requests.get(self.api_endpoint+ "/1.0/activity?start_date="+start_date+"&end_date="+end_date, headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(self.api_endpoint))

    ''' DELETE activity '''
    def activity_del(self, api_key, activity_id):
        headers = {'content-type': 'application/json'}

        try:
            req = requests.delete(self.api_endpoint+ "/1.0/activity/" + str(activity_id), headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(self.api_endpoint))


    def activity_add(self, api_token, time_start, time_stop, project_id):
        headers = {'content-type': 'application/json',
                'api-token': api_token}

        payload = {'time_start': time_start, 'time_stop': time_stop, 'project_id': project_id}


        try:
            req = requests.post(self.api_endpoint+ "/1.0/activity", headers=headers, json=payload, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(self.api_endpoint))


    def activity_current(self, api_token):
        headers = {'accept': 'application/json',
                'api-token': api_token}

        try:
            req = requests.get(self.api_endpoint+ "/1.0/activity/current", headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(self.api_endpoint))


    def activity_start(self, api_token, project_id, task_id=None):
        headers = {'content-type': 'application/json',
                'api-token': api_token}

        payload = {'agent': 'python-request', 'project_id': project_id}

        if type(task_id) == int:
            payload["task_id"] = task_id

        try:
            req = requests.post(self.api_endpoint+ "/1.0/activity/start", headers=headers, json=payload, timeout=self.timeout)
            logging.debug("SEND GET request")
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(self.api_endpoint))


    def activity_stop(self, api_token, time_id):
        headers = {'content-type': 'application/json',
                'api-token': api_token}

        try:
            req = requests.put(self.api_endpoint+ "/1.0/activity/stop/"+ str(time_id), headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))


    ''' Get Project '''
    def get_projects(self, api_token):
        headers = {'accept': 'application/json',
                'api-token': api_token}

        try:
            req = requests.get(self.api_endpoint+ "/1.0/project", headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(self.api_endpoint))


    def project_add(self, api_token, name):
        
        headers = {'content-type': 'application/json',
                'api-token': api_token}
        payload = {"name": name}

        try:
            req = requests.post(self.api_endpoint+ "/1.0/project", headers=headers, json=payload, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))


    def project_update(self, api_token,project_id, name):

        headers = {'content-type': 'application/json',
                'api-token': api_token}

        payload = {"name": name}

        try:
            req = requests.put(self.api_endpoint+ "/1.0/project/" + str(project_id), headers=headers, json=payload, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))


    def project_delete(self, api_token, project_id):
        headers = {'accept': 'application/json',
                'api-token': api_token}

        try:
            req = requests.delete(self.api_endpoint+ "/1.0/project/" + str(project_id), headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))


    def reports_activity(self, api_token, start_date, end_date):
        headers = {'accept': 'application/json',
                'api_token': api_token}

        #end_date = datetime.utcnow().isoformat()
        #start_date = datetime.utcnow().replace(hour=0,minute=0,second=0,microsecond=0).isoformat()

        try:
            req = requests.get(self.api_endpoint+ "/1.0/activity?start_date="+start_date+"&end_date="+end_date+"&group_by=date", headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))






    def auth(self, username, password):
        headers = {'content-type': 'application/json'}
        payload = {"username": username, "password": password}


        try:
            req = requests.post(self.api_endpoint+ "/1.0/user/auth", headers=headers, json=payload, timeout=self.timeout, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            return {"error": "connection error could not reach: "+self.api_endpoint}
            logging.error("Can not reach API (%s)",(self.api_endpoint))
        except requests.exceptions.ConnectionError as e:
            return {"error": "connection error could not reach: "+self.api_endpoint}
            logging.error("Can not reach API (%s)",(self.api_endpoint))


    def user_find(self, api_token, user_id):
        headers = {'accept': 'application/json',
                'api-token': api_token}

        try:
            req = requests.get(self.api_endpoint+ "/1.0/user/"+ str(user_id), headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))


    def whoami(self, api_token):
        headers = {'accept': 'application/json',
            'api-token': api_token}

        try:
            req = requests.get(self.api_endpoint+ "/1.0/user/whoami", headers=headers)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))


    def task_get(self, api_token, project_id):
        headers = {'accept': 'application/json',
            'api-token': api_token}

        try:
            req = requests.get(self.api_endpoint + "/1.0/task/" + str(project_id), headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))


    def task_add(self,api_token, project_id, name):
        headers = {'content-type': 'application/json',
            'api-token': api_token}
        
        payload = {"name": name}

        try:
            req = requests.post(self.api_endpoint + "/1.0/task/" + str(project_id), headers=headers, json=payload, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))



    def task_delete(self, api_token, task_id):

        headers = {'accept': 'application/json',
                'api-token': api_token}

        try:
            req = requests.delete(self.api_endpoint + "/1.0/task/" + str(task_id), headers=headers, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))

    def task_update(self, api_token, task_id, name):

        headers = {'content-type': 'application/json',
                'api-token': api_token}

        payload = {"name": name}

        try:
            req = requests.put(self.api_endpoint + "/1.0/task/" + str(task_id), headers=headers, json=payload, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))


    ''' update password for user '''
    def user_update(self, api_token, payload):
        headers = {'content-type': 'application/json',
                'api-token': api_token}

        #payload = {"password": password}

        try:
            req = requests.put(self.api_endpoint + "/1.0/user", headers=headers, json=payload, timeout=self.timeout)
            return req.json()
        except requests.exceptions.RequestException as e:
            logging.error("Can not reach API (%s)",(api_endpoint))



