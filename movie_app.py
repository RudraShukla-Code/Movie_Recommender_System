import streamlit as st
import pickle 
import pandas as pd
import requests

def fetch(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8fb020786f8cabbe0eb4e6a2f75a8f79&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    movie_ind = movie_li[movie_li['title'] == movie].index[0]
    distance = similar[movie_ind]
    movie_list = sorted(list(enumerate(distance)),reverse= True,key = lambda x:x[1])[1:6]
    
    Recommend_movie = []
    Recommend_poster = []
    for i in movie_list:
        movie_id = movie_li.iloc[i[0]].movie_id
        Recommend_movie.append(movie_li.iloc[i[0]].title)
        Recommend_poster.append(fetch(movie_id))
    return Recommend_movie, Recommend_poster


movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movie_li = pd.DataFrame(movie_dict)
# movie_li = pickle.load(open('movies.pkl','rb'))
# movie_li = movie_li['title'].values

similar = pickle.load(open('similar.pkl','rb'))

st.title('Movie recommender system')

select = st.selectbox('Pick one', movie_li['title'].values)


if st.button('Recommend'):
    names, poster = recommend(select)

    #for i in range(0,5):
    #       st.image(poster[i], caption=None, width=150)
    #       st.write(names[i])


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
       st.text(names[1])
       st.image(poster[1])
    with col3:
       st.text(names[2])
       st.image(poster[2])
    with col4:
       st.text(names[3])
       st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])

