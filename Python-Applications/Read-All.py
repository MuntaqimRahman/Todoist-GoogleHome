from todoist.api import TodoistAPI
from datetime import date

api = TodoistAPI('API KEY')
api.sync()

current_date = str(date.today())
items = api.state["items"]

def CheckDateLess(specDate):
    splitDate = specDate.split('-')
    
    today = date.today()

    if((int(splitDate[0]) <= today.year) and ( int(splitDate[1]) <= today.month) and (int(splitDate[2]) < today.day)):
        return 1
    else:
        return 0

def ReadAllCurrent():
    current_task_name= []
    for i in range(len(items)):
        if (items[i]['due'] != None):
            if (items[i]['due']['date'] == current_date):
                current_task_name.append(items[i]['content'])
    return current_task_name

def ReadAllOverdue():
    overdue_task_name= []
    for i in range(len(items)):
        if (items[i]['due'] != None):
            if (CheckDateLess(items[i]['due']['date']) == 1):
                overdue_task_name.append(items[i]['content'])
    print(overdue_task_name)
    return overdue_task_name