from todoist.api import TodoistAPI

api = TodoistAPI('API KEY')
api.sync()

def findTaskID(name):
    tasks = api.state["items"]
    for i in range(len(tasks)):
        if(tasks[i]['content'] == name and tasks[i]['date_completed'] == None):
            return tasks[i]["id"]
    
    return -1

def RemoveTask(name):
    taskID = findTaskID(name)
    api.items.delete(taskID)
    api.commit()
    return 1

def CompleteTask(name):
    taskID = findTaskID(name)
    api.items.complete(taskID)
    api.commit()

def UpdateTask(name,day):
    taskID = findTaskID(name)
    api.items.update(taskID,due={"string":day})
    api.commit()

def RemoveDate(name):
    taskID = findTaskID(name)
    api.items.update(taskID,due={None})
    api.commit()

        
