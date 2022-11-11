# from functions import to_todos,write_todos
import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is ", now)
while True:
    user_input = input("Enter your choice add,show, complete , edit or exit:- ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = functions.to_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_input.startswith("show"):
        todos = functions.to_todos()

        new_todos = []
        for item in todos:
            new_item = item.strip("\n")
            new_todos.append(new_item)

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = functions.to_todos()

            new_todo = input("Enter the edited the todo list")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue



    elif user_input.startswith("complete"):
        try:

            number = int(user_input[8:])

            todos = functions.to_todos()

            index = number - 1
            removed_todo = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo was {removed_todo} from the list"
            print(message)
        except ValueError:
            print("That item is not contain the list")
            continue
        except IndexError:
            print("You entered the wrong command")
            continue


    elif user_input.startswith("exit"):
        break
    else:
        print("Command is not Valid.")
print("Bye!")
