import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To Do ")
input_box = sg.InputText(tooltip="Enter To Do",key="To do")
list_box = sg.Listbox(values=functions.to_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
add_button = sg.Button("Add")
window = sg.Window("My To Do App",
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=('Helvetica',20))
while True:
    event , values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.to_todos()
            new_todo = values['To do'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['To do']
            todos = functions.to_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(todos)

        case "todos":
            window['To do'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()