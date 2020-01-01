# Todoist-GoogleHome
A couple of some common custom ToDoist applications to work with Google Assistant

Currently several commands which allow one to use todoist with their Google assisstant have been finished. They can be implemented by using IFTTT with Webhooks to contact a python server. The server here uses Flask although the idea should work in any framework.

ToDoist has its own integration with Google Home but it's somewhat limiting and requires telling the Google Home to talk
to ToDoist first. For instance you can't chain together the name, due date, and project in one command, it requires 3 individual
commands. It's still very useful however and worth trying out.

The Python server code can be used as is although further improvements could be made to improve scaleability. These improvements are commented in the file.

Completed:
    Complete and Remove a task by name
    Move a task to another day
    In one command: add task to this project on this day
    Remove the due date for a task

Todo:
    Read all overdue and current tasks
    
    Success check

Reading tasks with python code requires a variety of paid services (Qpython plugin, Tasker, Autocast). Alternatively one could write the function in shell code and just use Tasker and Autocast.

Useful Links:
https://developer.todoist.com/sync/v8/

https://todoist-python.readthedocs.io/en/latest/_modules/index.html
