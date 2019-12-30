from todoist.api import TodoistAPI

api = TodoistAPI('API KEY')
api.sync()

def projectID(project):
    projects = api.state["projects"]
    for i in range(len(projects)):
        if (projects[i]["name"] == project):
            return projects[i]["id"]
    
    return -1


def taskProjectAdder(name,project,day):

    specProjId = projectID(project)
    #Add if -1

    newTask = api.items.add(name,project_id=specProjId)
    newTask.update(due={"string":day})
    api.commit()
    

