import streamlit as st

st.title("Upcoming Weather Forecast")

# Place value will be used again in the script to store in a variable
place = st.text_input("Place: ")

# Days slider
days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="Select the number of forecasted days")

# Select box
select_data = st.selectbox("Select data to view",
                           ("Temperature","Sky"))

# Sub heading
st.subheader(f"{select_data} for the next {days} days in {place}")