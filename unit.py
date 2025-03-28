import streamlit as st

st.set_page_config("🔄 Unit Convertor App")
st.title("🔄 Unit Convertor App")
st.subheader("By YOha Ali Azam")
st.markdown("### Convert Lenght Weight And Time Instantly")
st.write("Select a Category and Enter a value and get the converted result.")

category = st.selectbox("**Select a Category**", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
  
  if category == "Length":
    if unit == "Kilometer to Miles":
        return value * 0.621371
    elif unit == "Kilometer to Meter":
       return value * 1000
    elif unit == "Meter to Kilometer":
       return value / 1000
    elif unit == "Miles to Kilometer":
        return value / 1.60934
    elif unit == "Meters to Feet":
        return value * 3.28084
    elif unit == "Feet to Meters":
        return value / 3.28084
    elif unit == "Centimeters to Inches":
        return value / 2.54
    elif unit == "Inches to Centimeters":
        return value * 2.54
    elif unit == "Millimeters to Inches":
        return value / 25.4
    elif unit == "Inches to Millimeters":
        return value * 25.4
    elif unit == "Yards to Meters":
        return value * 0.9144
    elif unit == "Meters to Yards":
        return value / 0.9144
    elif unit == "Miles to Yards":
        return value * 1760
    elif unit == "Yards to Miles":
        return value / 1760
 
  elif category == "Weight":
    if unit == "Kilogram to Pound":
        return value * 2.20462
    elif unit == "Pound to Kilogram":
        return value / 2.20462
    elif unit == "Milligrams to Grams":
        return value / 1000
    elif unit == "Grams to Milligrams":
        return value * 1000 
    elif unit == "Micrograms to Milligrams":
        return value / 1000
    elif unit == "Milligrams to Micrograms":
        return value * 1000


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
  unit = st.selectbox("📏 Select a Conversion:", [
      "Kilometer to Miles", "Meter to Kilometer", "Kilometer to Miles", "Miles to Kilometer",
      "Meters to Feet", "Feet to Meters",
      "Centimeters to Inches", "Inches to Centimeters",
      "Millimeters to Inches", "Inches to Millimeters",
      "Yards to Meters", "Meters to Yards",
      "Miles to Yards", "Yards to Miles"
  ])


elif category == "Weight":
  unit = st.selectbox("⚖️ Select a Conversion:", [
      "Kilogram to Pound", "Pound to Kilogram",
      "Milligrams to Grams", "Grams to Milligrams",
      "Micrograms to Milligrams", "Milligrams to Micrograms"
  ])


elif category == "Time":
  unit = st.selectbox("⏳ **Select a Conversation**:", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", "Days to Hours", "Hours to Days"])

value = st.number_input("**Enter the value to convert**.")

if st.button("🔫 Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        unit_names = unit.split(" to ")  # Splitting "Kilogram to Pound" → ["Kilogram", "Pound"]
        st.success(f"{value} {unit_names[0]} is equal to {result:.2f} {unit_names[1]}")
        st.balloons()
    else:
        st.error("Invalid Conversion. Please try again.")
