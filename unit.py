import streamlit as st
# st.markdown("### <h3 style='color:blue;'>CONVERTER♾</h3>", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/736x/be/25/99/be2599398966482adac244bccd946a6f.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔄 Unit Convertor App")
st.subheader("By YOha Ali Azam")
st.markdown("### Convert Lenght Weight And Time Instantly")
st.write("Select a Category and Enter a value and get the converted result.")

category = st.selectbox("**Select a Category**", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
  if category == "Length":
    if unit == "Kilometer to Miles":
      return value * 0.621371
    elif unit == "Miles to Kilometer":
      return value / 1.60934

  elif category == "Weight":
    if unit == "Kilogram to Pound":
      return value * 2.20462
    elif unit == "Pound to Kilogram":
      return value / 2.20462

  elif category == "Time":
    if unit == "Seconds to Minutes":
      return value /60
    elif unit == "Minutes to Seconds":
      return value * 60
    elif unit == "Hours to Minutes":
      return value * 60
    elif unit == "Minutes to Hours":
      return value / 60
    elif unit == "Days to Hours":
      return value * 24
    elif unit == "Hours to Days":
      return value / 24

if category == "Length":
  unit = st.selectbox("📏**Select a Conversation**", ["Kilometer to Miles", "Miles to Kilometer"])

elif category == "Weight":
  unit = st.selectbox("⚖**## Select a Conversation**", ["Kilogram to Pound", "Pound to Kilogram"])

elif category == "Time":
  unit = st.selectbox("⏳**## Select a Conversation**", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", "Days to Hours", "Hours to Days"])

value = st.number_input("**## Enter the value to convert**.")

if st.button("Convert"):
  result = convert_units(category, value, unit)
  st.success(f"The result is {result:.2f}")
  st.balloons()