import re    # for character
import streamlit as st

st.set_page_config(page_title = "Password Strenght Checker By YOha Ali Azam", page_icon = "🌘", layout = "centered")

st.markdown("<h1 style='color: purple;'>🔐 Welcome to the Password Strenght Checker By YOha Ali Azam!😎</h1>", unsafe_allow_html=True)

st.markdown("""
Use this simple tool to check the strength of your password and get suggestions that how to make it stronger.
            We will give you helpful tips to create a **Strong Password** 🔒""")

password = st.text_input("Enter your password", type = "password")

score = 0
feedback = [] # using append

# make condition
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1 
    else:
        feedback.append("❌ Password should contain both **upper and lower** case characters.")
  
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least **one digit**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least **one special character**(!@#$%^&*).")

    if score == 4:
        st.success("✅ Your Password is **Strong**.")
        st.balloons()
        
    elif score == 3:
        feedback.append("🟡 Your Password is medium strenght. It could be stronger.")
    else:
        feedback.append("🔴 Your Password is weak. Please make it stronger.")

    if feedback:
        st.markdown("## Improvement suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")
