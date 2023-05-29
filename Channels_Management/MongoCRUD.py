from pymongo import MongoClient


class CheckOnlineStatus:
    def __init__(self, *args, **kwargs):
        print(kwargs)
        #self.deviceNo = kwargs['']
        for k, v in kwargs.items():
            if k == 'deviceNo':
                self.deviceNo = kwargs['deviceNo']
                self.num = False

            if k == 'mobileNo':
                self.mobileNo = kwargs['mobileNo']
                self.num = True
        
        self.check()


    def check(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.user_coll = self.client['GJJ']['Users']
        if self.num == True:
            self.userInfo = self.user_coll.find_one({"mobileNo": self.mobileNo})
            return
        else:
            self.coll = self.client['GJJ']['devices']
            deviceInfo = self.coll.find_one({"deviceNo": self.deviceNo})
            self.userInfo = self.user_coll.find_one({"mobileNo": deviceInfo['mobileNo']})

    def feedback(self):
        #print(self.mobileNo)
        if self.userInfo['online_status'] == True:
            return  True
        return False





class AddToNotificationsQue:
    pass