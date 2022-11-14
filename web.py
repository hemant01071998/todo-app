import streamlit as st
import functions

todos = functions.to_todos()
st.title("My Todo App")
st.subheader("This is my app")
st.write("It's help to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo......")
