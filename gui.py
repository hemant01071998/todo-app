import functions
import PySimpleGUI as sg
import time

sg.theme("black")
clock = sg.Text("",key="clock")
label = sg.Text("Type in a To Do ")
input_box = sg.InputText(tooltip="Enter To Do",key="To do")
list_box = sg.Listbox(values=functions.to_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit",button_color="orange")
add_button = sg.Button("Add",button_color="yellow")
complete_button = sg.Button("Complete",button_color="green")
exit_button = sg.Button("Exit",button_color="red")
window = sg.Window("My To Do App",
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],[exit_button]],
                   font=('Helvetica',20))
while True:
    event , values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.to_todos()
            new_todo = values['To do'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['To do']
                todos = functions.to_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(todos)
            except IndexError:
                sg.popup("select the item first in the list ",font=('Helvetica',20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.to_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(todos)
                window['To do'].update(value='')
            except IndexError:
                sg.popup("select the item first in the list ", font=('Helvetica', 20))


        case "todos":
            window['To do'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()