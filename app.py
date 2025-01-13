import streamlit as st
import pickle
import requests

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-color: #0e1117;
# background-size: cover;
# background-position: center center;
# background-repeat: no-repeat;
# background-attachment: local;
# }}
# [data-testid="stHeader"] {{
# background: rgba(100,200,50,0);
# }}
# </style>
# """

Moviefile = open("movies_list.pkl","rb")
Similarityfile = open("similarity.pkl","rb")
movies = pickle.load(Moviefile)
similarity = pickle.load(Similarityfile)
movies_list = movies["title"].values

# st.markdown(page_bg_img, unsafe_allow_html=True)


def fetchposter(id):
         url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(id)
         data = requests.get(url)
         data = data.json()
         poster_path = data['poster_path']
         path = "https://image.tmdb.org/t/p/w500/"+poster_path
         return path

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetchposter(1632),
    fetchposter(299536),
    fetchposter(17455),
    fetchposter(2830),
    fetchposter(429422),
    fetchposter(9722),
    fetchposter(13972),
    fetchposter(240),
    fetchposter(155),
    fetchposter(598),
    fetchposter(914),
    fetchposter(255709),
    fetchposter(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)


st.header("Movie Recommended System")
select_value = st.selectbox("Select movie from dropdown",movies_list)


def recommend(movie):
    index  = movies[movies['title'] == movie] .index[0]
    distance  = sorted(list(enumerate(similarity[index])), reverse = True,key=lambda vector:vector[1])

    recommendMovies = []
    recommendPoster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommendMovies.append(movies.iloc[i[0]].title)
        recommendPoster.append(fetchposter(movies_id))
    return recommendMovies, recommendPoster

if st.button("Show recommanded movies"):
    Recommended_Movies, Recommended_Poster = recommend(select_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(Recommended_Movies[0]) 
        st.image(Recommended_Poster[0])
    with col2:
        st.text(Recommended_Movies[1]) 
        st.image(Recommended_Poster[1])

    with col3:
        st.text(Recommended_Movies[2])
        st.image(Recommended_Poster[2]) 
    with col4:
        st.text(Recommended_Movies[3]) 
        st.image(Recommended_Poster[3])

    with col5:
        st.text(Recommended_Movies[4]) 
        st.image(Recommended_Poster[4])