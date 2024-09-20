### Task App ###
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
        for i in range(len(tuple(data))):
            task = tuple(data[i].items())[0][1]
            progress = tuple(data[i].items())[1][1]
            print(f"Task: {task} , Progress: {progress}")
        close(f)
        
    if sys.argv[1] == "delete":
        f = open("tasks.json","r")
        data = json.load(f)
        f = open("tasks.json","w")
        if len(sys.argv) == 2:
            json.dump([],f,indent=3)  
        else:
            print(f"{data[int(sys.argv[2])-1]} deleted!")
            del data[int(sys.argv[2])-1]
            json.dump(data,f,indent=3)
        close(f)
    
    if sys.argv[1] == "mark":
        # "-p": In progress 
        # "-d": Done
        f = open("tasks.json","r")
        data = json.load(f)
        f = open("tasks.json","w")
        if len(sys.argv) == 4 and int(sys.argv[3]) < len(data):
            if sys.argv[2] == "-p":
                data[int(sys.argv[3])-1]["Progress"] = "In progress"
                json.dump(data,f,indent=3)
            elif sys.argv[2] == "-d":
                data[int(sys.argv[3])-1]["Progress"] = "Done"
                json.dump(data,f,indent=3)        
        else:
            json.dump(data,f,indent=3) 
            print("Index out of range!")
        close(f)
    
    if sys.argv[1] == "listdone":
        f = open("tasks.json","r")
        data = json.load(f)
        for i in range(len(tuple(data))):
            task = tuple(data[i].items())[0][1]
            progress = tuple(data[i].items())[1][1]
            if progress == "Done":
                print(f"Task: {task}")
        close(f)

    if sys.argv[1] == "listnotdone":
        f = open("tasks.json","r")
        data = json.load(f)
        for i in range(len(tuple(data))):
            task = tuple(data[i].items())[0][1]
            progress = tuple(data[i].items())[1][1]
            if progress == "Not done":
                print(f"Task: {task}")
        close(f)

    if sys.argv[1] == "currentlist":
        f = open("tasks.json","r")
        data = json.load(f)
        for i in range(len(tuple(data))):
            task = tuple(data[i].items())[0][1]
            progress = tuple(data[i].items())[1][1]
            if progress == "In progress":
                print(f"Task: {task}")
        close(f)
    
    if sys.argv[1] == "deletefile":
        os.remove("tasks.json")
        