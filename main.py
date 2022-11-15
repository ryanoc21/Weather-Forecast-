import streamlit as st
import plotly.express as px
from data_processing import get_data

st.title("Upcoming Weather Forecast")

# Place value will be used again in the script to store in a variable
place = st.text_input("Place: ")

# Days slider
days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="Select the number of forecasted days")


# Sub heading
st.subheader(f"Temperature for the next {days} days in {place}")

if place:
    # Call the function from data_processing
    data = get_data(location=place,forecast_days=days)

    # Get the temperature and sky data to pass to the plot
    temperatures = [temp['main']['temp']/10 for temp in data]
    dates = [date["dt_txt"] for date in data]

    # Create a temperature plot using plotly
    figure = px.line(x=dates,y=temperatures,labels={"x": "Date", "y": "Temperature (C)"})
    st.plotly_chart(figure)