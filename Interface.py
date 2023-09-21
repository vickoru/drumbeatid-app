import streamlit as st
import requests
import os
from streamlit_lottie import st_lottie
from utilities.dictionary import drummer_dictionaries



# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
# url = "http://localhost:8000"
# url = None
# Set page tab display

st.set_page_config(
   page_title="Drumbeat ID Project 🥁",
   page_icon= 'X',
   layout="wide",
   initial_sidebar_state="expanded",
)

url_endpoint = st.secrets.SERVICE_URL
# url_endpoint = st.secrets.LOCAL_URL

url_lottie = 'https://lottie.host/72f1c0f8-9dfa-40ce-904a-5048f407cd82/NQDeef2Nnv.json'

lottie = requests.get(url_lottie)
# Creating a blank dictionary to store JSON file,
# as their structure is similar to Python Dictionary
lottie_json = dict()

if lottie.status_code == 200:
    lottie_json = lottie.json()
else:
    st.write("Error in the URL")


col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.markdown(
    # Main Text on Homepage
    '''
    # User Interface for Drum Beat ID
    '''
    )

with col2:
    st_lottie(lottie_json,
            # change the direction of our animation
            reverse=False,
            # height and width of animation
            height=200,
            width=200,
            # speed of animation
            speed=1,
            # means the animation will run forever like a gif, and not as a still image
            loop=True,
            # quality of elements used in the animation, other values are "low" and "medium"
            quality='high',
            # THis is just to uniquely identify the animation
            key='drummer'
            )


st.markdown(
        '''
        ### Upload WAV-File and get the result of our classification:
        '''
        )

# File uploading section
st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_wav = st.file_uploader("Choose a WAV file", type="wav", accept_multiple_files=False)

if uploaded_wav is not None:
    # read and play the audio file
    st.write('### Play audio')
    audio_bytes = uploaded_wav.read()
    st.audio(audio_bytes, format='audio/wav')

    if st.button('Analyze Audiofile'):
        # Progress bar
        st.spinner("Sending the Audiofile to the API ...")
        # try:
        #     # calling API for prediction
        #     response = requests.post(url + "/upload_wav",
        #                             files={'wav': audio_bytes}, timeout=60)
        #     print(response.status_code)
        # except ConnectionError:
        #     st.write('### API is unresponsive or does not exist! 😨 🤖')
        # breakpoint()
        if url_endpoint: #response.status_code == 200:
            response = requests.post(url=url_endpoint,
                                     files={'wav': audio_bytes}, timeout=60)
            genre = response.json()['genre']
            st.write('### Analysis of Wave-File performed ! 🎉')

            with st.expander("See result of analysis 👀"):
                imageurl, caption_ = drummer_dictionaries(genre[0])
                if len(genre) > 1:
                    st.write(
                        f"### Not so sure about the style of your drumbeat 😨 🤖")
                    st.write(
                        f'''
                        ### It could be _{genre[0].capitalize()}_ or _{genre[1].capitalize()}_
                        '''
                    )
                    st.image(imageurl, width=300)
                    st.caption(f'### {caption_}', unsafe_allow_html=False)
                else:
                    st.write(f"### The style of your drumbeat is:")
                    st.write(f"## _{genre[0].capitalize()}_")
                    st.image(imageurl, width=300)
                    st.caption(f'### {caption_}', unsafe_allow_html=False)
        ## Non responsive API
        else:
            st.write('### API is unresponsive or does not exist! 😨 🤖')
