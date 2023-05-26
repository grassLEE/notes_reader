import os
from datetime import datetime

class Notes:
    def __init__(self, name):
        self.name = name
        
    def newEntry(name):
        name = name
        pa_filename = input("Enter the PA Filename\n").lower()
        value = os.fspath(pa_filename)  # os path like object, accepts variable value
        with open(value, "+a", encoding="UTF-8") as new: # with statement to open txt files as 'append' for writing
            content = str(input(f"Please enter the note for {value}\n"))
            new.write("\n")
            new.write(content)
            now = datetime.now() # variable 'now' with the value of current date/time
            new_form = now.strftime("%Y-%b: %a %d | %I:%M%p") # .strftime allows formatting "%b" is the symbol for rendering the month in abbreviated text for example, Jun for June. 
            new.write("\n")
            new.write(new_form)
            new.write("\n")
            new.close()

CT = Notes("Carlos")
CG = Notes("Christian")
SS = Notes("Santiago")
CC = Notes("Cesar")
BO = Notes("Bo")
MM = Notes("Michael")
New = Notes("Placeholder")
New.newEntry()


