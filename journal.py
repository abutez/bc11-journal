import sqlite3
class Database(object):
    def __init__(self):
        self.db = sqlite3.connect("journal.db")
        self.cursor = self.db.cursor()

    def select_all(self):
        self.cursor.execute("SELECT * FROM journal")
        res=  self.cursor.fetchall()
        return res

    def select_last_entry(self):

        # query the last entry by date from the database

        self.cursor.execute('''
    SELECT * from journal order by creation_date''')

        # save the result set result

        res = self.cursor.fetchall()

        # return the result set

        return res

    def create_entry(self, title, content):
        self.cursor.execute('''INSERT INTO journal(title,content,creation_date,update_date) VALUES (?, ?, DATE(),DATE())''', [title, content])
        self.db.commit()

menu = "Welcome to Jeernal.\n Type'create' to create a new entry.\n Type 'all' to view entries.\n Type 'exit' exit P-journal\n:"
    
db = Database()

print menu

while True:
    user_input = raw_input("Type a command: ")
    
    if user_input == "exit":
        print "Goodbye"
        db.db.close()
        break
    
    if user_input == "create" or user_input == "Create":
        title = raw_input("Enter a title: ")
        content = raw_input("Type your journal entry: ")

        db.create_entry(title, content)
        print "Inserted %s into journal"%(title),"\n"
        continue

    if user_input == "all":
        result = db.select_all()

        for row in result:
            print "********************************************"
            print "Title: ",row[1]
            print "Content:",row[2]
            print "Date written: ", row[3]

    if user_input == "last":
        result = db.select_last_entry()[-1]
        print "********************************************"
        print "Title: ",result[1]
        print "Content:",result[2]
        print "Date written: ", result[3]

db.db.close()
