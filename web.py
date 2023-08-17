import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo.title())
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("Something else")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="New To-Do:", placeholder="Add a new To-Do",
              on_change=add_todo, key="new_todo")