class Database(object):
    def __init__(self):
        self.db = sqlite3.connect("data/journal.db")
        self.cursor = self.db.cursor()

    def select_all(self):
        pass

    def select_one(self,entry_id):
        pass

    def select_latest(self):
        pass

    def create_entry(self, title,content):
        pass

    
    
    

