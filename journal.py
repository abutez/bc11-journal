import sqlite3
class Database(object):
    def __init__(self):
        self.db = sqlite3.connect("journal.db")
        self.cursor = self.db.cursor()

    def select_all(self):
        pass

    def select_one(self,entry_id):
        pass

    def select_latest(self):
        pass

    def create_entry(self, title,content):
        pass
    
db = Database()

while True:
    user_input = raw_input(menu())

    if user_input == "exit":
        print "Goodbye"
        break
    
    if user_input == "create" or user_input == "Create":
        title = raw_input("Enter a title: ")
        content = raw_input("Type your journal entry: ")

        db.create_entry(title, content)
        
