import streamlit as st
import pandas as pd
import plotly.express as px 
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(page_title = "Airbnb Analysis",
                   layout = "wide",
                   initial_sidebar_state = "expanded",
                   menu_items = {'About' : " This project was done by Narmadha Devi B"})

with st.sidebar:
    selected = option_menu(None, ["Overview","Home","Data Exploration"],
                           default_index=0,
                           orientation="vertical")


df = pd.read_csv("Airbnb.csv")


if selected == "Overview":
    st.title(':red[Airbnb Analysis]')
    st.subheader(':blue[Domain:] Travel Industry, Property Management and Tourism ')
    st.subheader(':blue[Overview:] This project involves analyzing Airbnb data by cleaning and preparing the dataset and then developing a Streamlit application with interactive plots to explore listings based on prices, ratings, and location. The analysis focuses on pricing variations, availability patterns, and location-based trends. And also create a dashboard in Tableau or Power BI presenting key insights from the data.')
    st.subheader(':blue[Skills Take Away:] Python Scripting, Data Collection, Data Preprocessing, Data Visualization, EDA, Streamlit, PowerBI or Tableau ')


if selected == "Home":

    col1, col2 = st.columns(2)

    with col1:
        st.image(r"C:\Users\Bala Krishnan\OneDrive\Desktop\download.png")

    with col2:
        st.markdown("##### :black[Airbnb is an online platform that connects people looking to rent out their homes with travelers seeking unique accommodations. The Airbnb offers a wide range options, from single rooms to entire homes, across the globe. It operates on a peer-to-peer model, allowing hosts to list their properties and guests to book them for short-term stays. Also it is often more affordable alternatives to hotels, Airbnb has become a major player in the travel industry and Tourism.]")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### :black[Airbnb is a popular choice for travelers because it offers unique and affordable accommodations in a variety of locations, from city centers to remote areas. Unlike traditional hotels, Airbnb provides a more personalized and local experience, often allowing guests to stay in homes with amenities like kitchens and laundry facilities, which can save money on meals and other expenses. The platform is easy to use, with a wide range of options that cater to different needs, making it a convenient and flexible option for all types of travelers.]")

    with col2:
        st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGthaXo5N2xtdm55aWgxM2k0NTR0OTAyOGc5dTR2NzZyZjgxeTFveiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6ZsVuc0gxSeAV3hu/giphy.webp")


    st.markdown("## :blue[Offical Websites:]")
    url = "https://www.airbnb.co.in/"
    st.markdown(f" ### [Airbnb | Holiday rentals, cabins, beach houses & more]({url})")

    url = "https://en.wikipedia.org/wiki/Airbnb"
    st.markdown(f" ### [Airbnb Informations]({url})")


if selected == "Data Exploration":

    st.title(':red[Airbnb Analysis]')

    Insights = st.sidebar.selectbox("**Insights**", ("Price Analysis", "Availability Analysis", "Location Analysis"))

    if Insights == "Price Analysis":
        col1, col2 = st.columns(2)
        with col1:
            Country= st.selectbox("Select the Country",df["Country"].unique())
        with col2:
            RoomType= st.selectbox("Select the RoomType",df["RoomType"].unique())

        data = df[(df["Country"] == Country) & (df["RoomType"] == RoomType)]
        df1 = data.groupby("Property_type")[["Price", "Total_Reviews"]].sum().reset_index()

        fig_bar = px.bar(
            df1, 
            x='Property_type', 
            y='Price', 
            title='Price for Property Types',
            hover_data=['Total_Reviews'],
            color_discrete_sequence=px.colors.sequential.Aggrnyl
            )
        st.plotly_chart(fig_bar)

        df2 = data.groupby("Response")[["Price", "ExtraPeople"]].sum().reset_index()

        fig_pi= px.pie(df2, values="Price", names= "Response",
                            hover_data=["ExtraPeople"],
                            color_discrete_sequence=px.colors.sequential.algae,
                            title="PRICE DIFFERENCE BASED ON Extra People",
                            )
        st.plotly_chart(fig_pi)


    if Insights == "Availability Analysis":
        col1, col2, col3 = st.columns(3)
        with col1:
            Country= st.selectbox("Select the Country",df["Country"].unique())
        with col2:
            RoomType= st.selectbox("Select the RoomType",df["RoomType"].unique())
        with col3:
            Property_type= st.selectbox("Select the Property_type",df["Property_type"].unique())

        data = df[(df["Country"] == Country) & (df["RoomType"] == RoomType) & (df['Property_type'])]

        fig = px.sunburst(data, path = ['RoomType', 'BedType', 'Location'], 
                          values = 'Avail_30',
                          title="Availability_30",
                          color_discrete_sequence=px.colors.sequential.Agsunset)
        
        st.plotly_chart(fig)

        fig = px.sunburst(data, path = ['RoomType', 'BedType', 'Location'], 
                          values = 'Avail_60',
                          title="Availability_60",
                          color_discrete_sequence=px.colors.sequential.amp)
        
        st.plotly_chart(fig)


        fig = px.sunburst(data, path = ['RoomType', 'BedType', 'Location'], 
                          values = 'Avail_90',
                          title="Availability_90",
                          color_discrete_sequence=px.colors.sequential.Blackbody)
        
        st.plotly_chart(fig)


        fig = px.sunburst(data, path = ['RoomType', 'BedType', 'Location'], 
                          values = 'Avail_365',
                          title="Availability_365",
                          color_discrete_sequence=px.colors.sequential.Bluered)
        
        st.plotly_chart(fig)
        
    if Insights == "Location Analysis":

        col1, col2, col3 = st.columns(3)
        with col1:
            Country= st.selectbox("Select the Country",df["Country"].unique())

        with col2:
            Property_type= st.selectbox("Select the Property_type",df["Property_type"].unique())    

        with col3 :
            RoomType= st.selectbox("Select the RoomType",df["RoomType"].unique())

        data = df[(df["Country"] == Country) & (df["Property_type"] == Property_type) & (df["RoomType"] == RoomType)]

        df1 = data.groupby("Accomadate")[["Cleaning", "Bedroom", "Price", "Guests","ExtraPeople"]].sum().reset_index()
        fig_bar = px.bar(
            df1, 
            x='Accomadate', 
            y=['Cleaning', 'Bedroom', 'Price', 'Guests'], 
            title='Accomadations by Country and its Property Type',
            hover_data=['ExtraPeople'],
            color_discrete_sequence=px.colors.sequential.Blugrn
            )
        st.plotly_chart(fig_bar)
