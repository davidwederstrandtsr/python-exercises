# open files using 'with' keyword will ensure the file closes
filename = "data/chores.txt" 
with open(filename) as f:
    print(f.read())
    contents = f.read()
    
print(contents.split('\n'))

with open(filename) as f:
    contents = f.readlines()

contents

message = "hey, this is new"

with open("data/what_have.txt", "a") as f:
    f.write(message)
    
with open("data/what_have.txt", "r") as f:
    print(f.read())
    
