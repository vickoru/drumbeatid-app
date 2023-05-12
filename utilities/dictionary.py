
def drummer_dictionaries(genre):
    '''
    Dictionary with a set of url and small biographies of specific drummers
    depending on the drumming style
    '''
    images = {
        'rock': "https://www.rollingstone.de/wp-content/uploads/2016/04/01/12/John-Bonham-GettyImages-77186814-992x560.jpg",
        'jazz': "https://www.bluenote.com/files/2019/03/TonyWilliams_byFrancisWolff.jpg",
        'funk': "https://drummagazine.com/wp-content/uploads/2018/11/James-Diamond-WIlliams-Ohio-Players_2.jpg",
        'latin': "https://npr.brightspotcdn.com/dims4/default/f128c94/2147483647/strip/true/crop/800x533+0+0/resize/880x586!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F6b%2Ff5%2Fb8d62d964faa80d7f334a0500285%2Ftito-puente-at-timbales.jpg",
        'hiphop': "https://drummagazine.com/wp-content/uploads/2021/12/questlove-soundclash-scaled.jpg",
        'soul': "https://i.pinimg.com/originals/45/76/ba/4576ba99b4c56ad17c8a3bd40e1e5b84.jpg"
    }

    captions = {
        'rock': 'John Bonham, drummer of Led Zeppelin, 1948-1980',
        'jazz': 'Tony Williams, 1945-1997',
        'funk': "James Diamond, drummer of Ohio Players, 1950-today",
        'latin': "Tito Puente, 1923-2000",
        'hiphop': "Questlove, drummer of The Roots, 1971-today",
        'soul': "Clyde Stubblefield, collaborated with James Brown, 1943-2017"
        }

    return images[genre], captions[genre]





                #    if genre == "rock":
                #         st.image("https://www.rollingstone.de/wp-content/uploads/2016/04/01/12/John-Bonham-GettyImages-77186814-992x560.jpg", width=500)
                #         st.caption(f'### John Bonham, drummer of Led Zeppelin, 1948-1980', unsafe_allow_html=False)
                #     elif genre == "jazz":
                #         st.image("https://www.bluenote.com/files/2019/03/TonyWilliams_byFrancisWolff.jpg", width = 500)
                #         st.caption(f'### Tony Williams, 1945-1997', unsafe_allow_html=False)
                #     elif genre == "funk":
                #         st.image("https://drummagazine.com/wp-content/uploads/2018/11/James-Diamond-WIlliams-Ohio-Players_2.jpg", width = 500)
                #         st.caption(f'### James Diamond, drummer of Ohio Players, 1950-today', unsafe_allow_html=False)
                #     elif genre == "latin":
                #         st.image("https://npr.brightspotcdn.com/dims4/default/f128c94/2147483647/strip/true/crop/800x533+0+0/resize/880x586!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F6b%2Ff5%2Fb8d62d964faa80d7f334a0500285%2Ftito-puente-at-timbales.jpg", width=500)
                #         st.caption(f'### Tito Puente, 1923-2000', unsafe_allow_html=False)
                #     elif genre == "hiphop":
                #         st.image("https://drummagazine.com/wp-content/uploads/2021/12/questlove-soundclash-scaled.jpg", width=300)
                #         st.caption(f'### Questlove, drummer of The Roots, 1971-today', unsafe_allow_html=False)
                #     else:
                #         st.image("https://i.pinimg.com/originals/45/76/ba/4576ba99b4c56ad17c8a3bd40e1e5b84.jpg", width=300)
                #         st.caption(f'### Clyde Stubblefield, collaborated with James Brown, 1943-2017', unsafe_allow_html=False)
