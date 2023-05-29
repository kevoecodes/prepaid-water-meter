from datetime import datetime
from pymongo import MongoClient
from Mongo_DB.MongoDB import MongoDB

class MongoCreateUser(MongoDB):
    def __init__(self, data):
        super().__init__()
        self.data = {}
        self.data = data
        self.is_created = self.createUser()
        self.account_created = self.createAccount()
        

    def createUser(self):
        try:
            self.data['created_at'] = datetime.now()
            self.data['online'] = False
            reg_acc = self.regAcc_coll.find()
            for x in reg_acc:
                if self.account_coll.find_one({"accountNo": x['acc']}) is None:
                    self.accountNo = x['acc']

            self.data['accountNo'] = self.accountNo
            print(self.data)

            self.users_coll.insert_one(self.data)
            return True
        except:
            return False

    def createAccount(self):
        try:
            self.account_data = {}
            
            self.account_data['accountNo'] = self.accountNo
            self.account_data['deviceNo'] = self.data['deviceNo']
            self.account_data['active'] = True
            self.account_data['current_balance'] = "0"
            self.account_data['water_units'] = "0"
            self.account_data['consumed_litres'] = "0"
            self.account_data['total_deposits'] = "0"
            self.account_data['cash_used'] = "0"
            self.account_coll.insert_one(self.account_data)

            return True         

        except:
            return False
    

    def isCreated(self):
        print(self.is_created, self.account_created)
        if self.is_created and self.account_created:
            self.regAcc_coll.delete_one({"acc": self.accountNo})
            return True
        return False
    
    def details(self):
        
        return self.data