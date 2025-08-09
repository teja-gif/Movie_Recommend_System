import pandas as pd
import streamlit as st
import pickle


def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]  # This is a 1D array
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        #Fetch poster from API

        recommended_movies.append(movies.iloc[i[0]]['title'])

    return recommended_movies


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend_movies(selected_movie_name)
    for i in recommendations:
        st.write(i)

