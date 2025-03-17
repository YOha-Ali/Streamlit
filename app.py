import streamlit as st

st.title("Here is YOha's First Streamlit")
st.header("""خوش آمدید
          Here we Go....""")

user = st.text_input("What is your name?")
if user:
    st.write("Assalam O Alykum", user )

agree = st.checkbox("Agree with me?")
if agree:
    st.write("Lets Goo!", user)
 

if st.button("Click me!"):
    st.success(f"Ramadan Mubarak to you {user}.") 

st.subheader("Dou you wanna play number guessing game ?")

import random 
if "get_started" not in st.session_state:
    st.session_state.get_started = False

if st.button("Yes"):
    st.session_state.get_started = True
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 10)

if st.session_state.get_started:
    st.header("🎲 Guess the number Game begin...")

    guess = st.number_input("Enter a number between 1 to 10: ", min_value = 1, max_value = 10, step = 1)

    if st.button("Guess"):
        if guess > st.session_state.number:
            st.warning("Sorry too High.")
        elif guess < st.session_state.number:
            st.warning("Sorry too Low.")
        else:
         st.success("Yayy! You guess the right number.")
         st.session_state.number = random.randint(1, 10)

if st.button("No"):
    st.session_state.get_started = False
    st.write("Okay! As you want.")



st.title("Counter...")
st.header("Welcome to counter.")

if "count" not in st.session_state:
    st.session_state["count"] = 0 
st.write(f"Current count: {st.session_state.count}") 

count = 0
st.header(st.session_state.count) 

col1, col2 = st.columns(2)

print("Count>>>", st.session_state.count)
with col1:
    if st.button("Increment"):
        st.session_state.count += 1

with col2:
    if st.button("Decrement"):
        st.session_state.count -= 1      

