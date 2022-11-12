import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To Do ")
input_box = sg.InputText(tooltip="Enter To Do",key="To do")
list_box = sg.Listbox(values=functions.to_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit",button_color="orange")
add_button = sg.Button("Add",button_color="black")
complete_button = sg.Button("Complete",button_color="green")
exit_button = sg.Button("Exit",button_color="red")
window = sg.Window("My To Do App",
                   layout=[[label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],[exit_button]],
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

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.to_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(todos)
            window['To do'].update(value='')

        case "todos":
            window['To do'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()