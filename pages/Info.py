import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.markdown(
    # Main Text on Info page
    '''
    # Drum Beat ID 🥁
    '''
    )

col1, col2 = st.columns([0.6, 0.4])

url_lottie = 'https://lottie.host/97406120-08c1-448d-9d1e-17b7db4d46ce/0wDuR6FQxP.json'

lottie = requests.get(url_lottie)
# Creating a blank dictionary to store JSON file,
    # as their structure is similar to Python Dictionary
lottie_json = dict()

if lottie.status_code == 200:
    lottie_json = lottie.json()
else:
    st.write("Error in the URL")

with col1:
    st.markdown(
    '''
    ### This is a project created during the Data Science bootcamp at Le Wagon
    '''
    )

with col2:
    st_lottie(lottie_json,
            # change the direction of our animation
            reverse=False,
            # height and width of animation
            height=250,
            width=250,
            # speed of animation
            speed=1,
            # means the animation will run forever like a gif, and not as a still image
            loop=True,
            # quality of elements used in the animation, other values are "low" and "medium"
            quality='high',
            # THis is just to uniquely identify the animation
            key='drummer'
            )
