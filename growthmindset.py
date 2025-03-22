import streamlit as st

st.set_page_config(page_title = "Growth Mindset Project")

st.markdown(
    """
    <h1 style="color: #1E90FF; text-align: center;">
        🌱 Growth Mindset AI Project By YOha Ali Azam™
    </h1>
    """,
    unsafe_allow_html=True
)

st.header("Welcome to Your Growth Journey! 🚀")
st.write("Embrace Challenges, Learn From Mistakes, And Unlock Your Full Potential. This Is AI-Powered App Helps You Build a Growth Mindset With Reflection, Challenges And Achievments! 🌟")
st.header("Today's Growth Mindset Quote. ✍")
st.write("Look for the good in every situation, seek the valuable life lesson in every setback, look for the solution to every problem. Think and talk continually about your goals.જ⁀➴🏆")

st.subheader("🚀 What Will You Conquer Today?")
st.write("Every day is a new opportunity to grow. Set your challenge and rise above it! 💪✨")

st.header("What's Your Challenge Today? ⚔️")
user = st.text_input("Describe a Challenge You are Facing? 😮‍💨")
if user:
    st.success(f"You are Facing {user}. Keep Pusing Forward Towards Your Goals.✨🏋️")
else:
    st.warning("Tell Us about Your Challenge to get Started. 🚩")

st.subheader("⚡ Turn Setbacks into Comebacks!")
st.write("Failures are just stepping stones. Every setback is a setup for a comeback! 🔥")


# Reflect

st.header("🧠 Reflecting on experiences helps you grow! Write your thoughts. ✍️")
reflection = st.text_area("Write Your Reflection here:")
if reflection:
    st.success(f"**Great Insight**!👌 Your Reflection: {reflection}. 👑")  
else:          
    st.info("Reflection on Past experience help to you Grow! 📈 Share Your Difficulties. 🤝")

st.subheader("🚀 Push Past Limits, Unlock New Levels!")
st.write("The best version of you is on the other side of your comfort zone. Keep going! 🌟")


# achivement

st.header("Celebrate Your Achivement! Not Perfection. 🏆🎊")
achivement = st.text_input("Share something You have Recently Accomplished By the Grace of **ALLAH**: ")
if achivement:
    st.success(f"Amazing You Achieved By the Grace of **ALLAH**: {achivement}. ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ ")
else:
    st.info("Big or small, light or darker, every achievement counts! Just trust in **Allah’s** plan and keep moving forward. 💎✨")
    
# footer

st.write("- - -")
st.success("Growth begins at the end of your comfort zone. Every challenge is a chance to learn, adapt, and rise stronger. 🌱✨")
st.write("🌸 **Created By YOha Ali Azam™**")