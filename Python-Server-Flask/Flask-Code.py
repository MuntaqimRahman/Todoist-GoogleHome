
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request

from todoist.api import TodoistAPI
from datetime import datetime
import pytz

api = TodoistAPI('API-KEY')
api.sync()

app = Flask(__name__)

#Future: Convert the items and task to a hash table which is stored and changed only when adding a new task instead of linear search makes it more scaleable

def findTaskID(name):
    tasks = api.state["items"]
    for i in range(len(tasks)):
        taskName = (tasks[i]['content']).lower()
        if(taskName == name.lower() and tasks[i]['date_completed'] == None):
            return tasks[i]["id"]

    return -1

def projectID(project):
    projects = api.state["projects"]
    for i in range(len(projects)):
        projectName = (projects[i]['name']).lower()
        if (projectName == project.lower()):
            return projects[i]["id"]

    return -1

@app.route('/read-current', methods = ["POST"])
def ReadAllCurrent():
    current_date_gmt = pytz.utc.localize(datetime.utcnow())
    current_date_est = current_date_gmt.astimezone(pytz.timezone("America/Toronto"))
    current_date = current_date_est.strftime("%Y-%m-%d")

    items = api.state["items"]
    current_task_name= []
    for i in range(len(items)):
        if (items[i]['due'] != None):
            if (items[i]['due']['date'] == current_date):
                current_task_name.append(items[i]['content'])
    print(current_task_name)
    return current_task_name

@app.route('/remove-task',methods = ["POST"])
def RemoveTask():
    name = (request.get_data()).decode('ascii')
    print(name)

    taskID = findTaskID(name)
    api.items.delete(taskID)
    api.commit()
    return 1

@app.route('/remove-date',methods = ["POST"])
def RemoveDate():
    name = (request.get_data()).decode('ascii')
    print(name)

    taskID = findTaskID(name)
    api.items.update(taskID,due={None})
    api.commit()
    return 1

@app.route('/complete-task',methods = ["POST"])
def CompleteTask():
    name = (request.get_data()).decode('ascii')
    print(name)

    taskID = findTaskID(name)
    api.items.complete(taskID)
    api.commit()
    return 1

@app.route('/update-task',methods = ["POST"])
def UpdateTask():
    messageContent = (request.get_data()).decode('ascii')
    name_date = messageContent.split(' to ') #name then new date of task
    print(name_date)

    name = name_date[0]
    date = name_date[1]

    taskID = findTaskID(name)
    api.items.update(taskID,due={"string":date})
    api.commit()
    return 1

@app.route('/create-task',methods = ["POST"])
def taskProjectAdder():
    messageContent = (request.get_data()).decode('ascii')
    messageContent = messageContent.replace(" for "," to ") #Future: Use a regex split instead in the future makes it more scaleable

    name_project_date = messageContent.split(' to ',2) #name then project name then date of the task

    print(name_project_date)

    name = name_project_date[0]
    project = name_project_date[1]
    date = name_project_date[2]

    specProjId = projectID(project)

    newTask = api.items.add(name,project_id=specProjId)
    newTask.update(due={"string":date})
    api.commit()

    return 1
