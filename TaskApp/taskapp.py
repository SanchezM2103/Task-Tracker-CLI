### Task App ###
"""
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.


python taskapp.py add "..."
python taskapp delete (una en especifico o todas)
python taskapp deletefile

python taskapp.py list
python taskapp.py listdone
python taskapp.py listnotdone
python taskapp.py currentlist
"""

"open() con a --> Open the file for writing."
"The data being written will be inserted at the end of the file. Creates a new file if it does not exist."


import sys
import os
import json

def exists(file):
    if os.path.exists(file) == False:
        return False
    else:
        return True

def close(f):
    f.close()

if len(sys.argv) == 1:
    exit()
else:
    if exists("tasks.json") == False:
        f = open("tasks.json","w")
        json.dump([],f)   
    else:
        pass
        
    if sys.argv[1] == "add":
        f = open("tasks.json","r")
        cadena = []
        for i in range(len(sys.argv)-2):
            cadena.append(sys.argv[i+2])
        task = " ".join(cadena)    
        element_json = {"Task":task, "Progress":"Not done"}
        data = json.load(f)
        data.append(element_json)
        
        f = open("tasks.json","w")
        f.write(json.dumps(data,indent=3))
        close(f)
    
    if sys.argv[1] == "list":
        f = open("tasks.json","r")
        data = json.load(f)
        #print(tuple(data[0].items())[0][1]) 
        # Si quiero seleccionar la tarea especifica
        for i in range(len(tuple(data))):
            task = tuple(data[i].items())[0][1]
            progress = tuple(data[i].items())[1][1]
            print(f"Task: {task} , Progress: {progress}")
        close(f)
        
    if sys.argv[1] == "delete":
        # Si quiero una en especifico pongo el indice
        # Si quiero vaciarla entero pongo solo "delete" y listo
        f = open("tasks.json","r")
        data = json.load(f)
        f = open("tasks.json","w")
        if len(sys.argv) == 2:
            json.dump([],f)  
        else:
            print(f"{data[int(sys.argv[2])-1]} deleted!")
            del data[int(sys.argv[2])-1]
            json.dump(data,f)
        close(f)
    
    if sys.argv[1] == "mark":
        # "-p" para poner que la tarea esté en progreso
        # "-d" para poner que la tarea está acabada
        pass
    
    if sys.argv[1] == "listdone":
        pass

    if sys.argv[1] == "listnotdone":
        pass

    if sys.argv[1] == "currentlist":
        pass
    
    if sys.argv[1] == "deletefile":
        os.remove("tasks.json")
        