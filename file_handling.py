from pathlib import Path
import os
def task():
  print("Press 1 to create file")
  print("Press 2 to read file")
  print("Press 3 to update file")
  print("Press 4 to delete file")
  print("Press 5 to stop process")

  taskToDo = int(input("Enter task you want to perform: "))
  if taskToDo == 1:
    createFile()
  elif taskToDo == 2:
    readFile()  
  elif taskToDo == 3:
    updateFile() 
  elif taskToDo == 4:
    deleteFile()
  elif taskToDo == 5:
    print("Process stopped")
    stop()    

def readFileAndFolders():
  path = Path('')
  items = list(path.rglob('*'))
  for i,item in enumerate(items):
    print(f"{i+1}: {item}")

def createFile():
  try:  
    readFileAndFolders()
    name = input("Enter name of the file: ")
    p = Path(name)
    if not p.exists():
      with open(p,'w') as fs:
        data = input("What do you want to enter: ")
        fs.write(data)
        print("FILE CREATED SUCCESSFULLY!!")
    else:
      print("File already exists!!!!")    
  except Exception as err:
    print(f"{err} error occured during execution")    
  finally:
    task()

def readFile():
  try:
    readFileAndFolders()
    name = input("Enter which file you want to read: ")
    path = Path(name)
    if path.exists() and path.is_file():
      with open(path,'r') as fs:
        data = fs.read()
        print(data)
    else:
      print(f"File doesn't exists")    
  except Exception as err:
    print(f"{err} error occured during execution")
  finally:
    task()

def updateFile():
  try:
    readFileAndFolders()
    fileName = input("Enter file you want to update: ")
    p = Path(fileName)
    if p.exists() and p.is_file():
      print("Press 1 if you want to rename the filename")
      print("Press 2 if you want to overwrite the file data")
      print("Press 3 if you want to append the file data")

      res = int(input("Enter your response: "))
      if res == 1:
        newName = input("Enter new name of the file")
        p2 = Path(newName)
        p.rename(p2)
      elif res == 2:
        with open(p, 'w') as fs:
          data = input("What you want to enter: ")
          fs = fs.write(data)
      elif res == 3:
        with open(p,'a') as fs:
          data = input("What to you want to append: ")
          fs = fs.write(data)
      else:
        print("Enter a valid response")  
        return
        
      print("FILE UPDATED SUCCESSFULLY")
    else:
      print("File doesn't exists")

  except Exception as err:
    print(f"{err} error occured during execution")
  finally:
    task()
    
def deleteFile():
  try:
    readFileAndFolders()
    name = input("Enter file you want to delete: ")
    p = Path(name)
    if p.exists() and p.is_file():
      os.remove(name)
      print("File deleted!!!")
    else:
      print("File doesn't exists!")  
  except Exception as err:
    print(f"{err} error occured during execution")
  finally:
    task()  

def stop():
  return


task()
