import streamlit as st
import info
import pandas as pd
import plotly.express as px
import json

def datal():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def welcomepage():
    st.markdown('<h1 style="text-align: center;">Hi! My name is Desdemona Stubbs!</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">Keep reading to learn more about my favorite island:</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 20px;"><strong>Turks and Caicos</strong></p>', unsafe_allow_html=True)
    st.image(info.profile_picture, width = 400)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<hr style="width: 50%; margin-left: auto; margin-right: auto;">', unsafe_allow_html=True)



welcomepage()

def overview():
    st.image("images/Turks")
    
    option = st.radio(
        "Click to learn more about the geography of Turks and Caicos!",
        ("Land", "Water")
    )

    if option == "Land":
        land_option = st.radio("Choose an option about Land", ("Cool", "Even Cooler"))
        
        if land_option == "Cool":
            st.write("The Turks and Caicos islands are primarily formed from coral reefs, with the majority of the islands sitting on a large underwater plateau made up of coral deposits, creating a barrier reef system.")
        else:
            st.write("The Turks and Caicos Islands are made up of about 40 islands and cays.")

    else:
        water_option = st.radio("Choose an option to learn more about the water", ("Cool", "Even Cooler"))

        if water_option == "Cool":
            st.write("The water is consistently warm year-round")
        else:
            st.write("Most of the water around the islands is relatively shallow, contributing to the bright blue color.") 

overview()




st.write("")
st.write("")
st.write("")

st.write('''
    <div style="text-align: center; font-size: 24px;">
        <strong>Out of all the places I have traveled to, Turks and Caicos is my favorite! From the graphs that I have below you will be able to see I definitely love Turks and Caicos!!</strong>
    </div>
    '''), unsafe_allow_html=True
st.write("")
st.write("")
st.write("")

def static_chart():
    data = datal()
    st.write("Some of my favorite vacation locations and the amount of times I have been there")
    vacation_data = pd.DataFrame(data['favorite_vacation_locations'])
    st.line_chart(vacation_data.set_index('Place'))

static_chart()



def packing_slider():
    st.header("Packing for Turks and Caicos")

    num_items = st.slider( #NEW
        "How many outfits do you think I usually pack for a 5 day trip to Turks and Caicos?", 
        min_value=1, 
        max_value=15, 
        value=12
    )

    if num_items <= 5:
        st.write("So you think I'm boring?")
    elif 5 <= num_items <= 8:
        st.write("I wish I packed this light.")
    elif 9 <= num_items <= 11:
        st.write("Yes, you are correct!")
    else:
        st.write("That would be a crazy amount for 5 days!")



trip_data = pd.DataFrame({
    'Place': ["Turks and Caicos", "Minneapolis, Minnesota", 
              "Panama City Beach, Florida", "Negril, Jamaica", "Ocho Rios, Jamaica", "Turks and Caicos", "Turks and Caicos", "Turks and Caicos", "Europe", "The Bahamas"],
    'Year': [2023, 2024, 2024, 2024, 2024, 2024, 2025, 2025, 2025, 2025]
})
st.write("")
st.write("")
st.write("")


def dynamic_chart():
    data = datal()
    st.header("Ok, but if you think the amount of times I have been to Turks is bad, change the year to see all of the vacations I have taken within the past three years!")
    trip_data = pd.DataFrame(data['trip_data'])
    
    selected_years = st.multiselect(
        'Select the years to see all of the trips I have been on:',
        trip_data['Year'].unique(),
        default=trip_data['Year'].unique()
    )
    
    filtered_data = trip_data[trip_data['Year'].isin(selected_years)]
    
    if not filtered_data.empty:
        st.write(f"Showing trips for the years: {', '.join(map(str, selected_years))}")
        st.bar_chart(filtered_data['Place'].value_counts())
    else:
        st.write("No trips available for the selected years.")
dynamic_chart()



st.write("")
st.write("")

def favorite_activities_pie():
    st. write("I think after that graph you can truly imagine how much I love being in Turks! You must be wondering whats so fun about Turks and Caicos theres just beach but here is a pi chart that shows all of my favorite activities distributed based on how fun I think each is")

    data = datal()
    activities_data = pd.DataFrame(data['favorite_activities'])
    fig = px.pie(activities_data, values='Rating', names='Activity', title="My Favorite Activities")
    st.plotly_chart(fig)

favorite_activities_pie()
st.write("Hopefully now you can understand why I love Turks and Caicos so much! I hope you learned something new today and enjoyed reading about my favorite place to travel!")











