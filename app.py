import pickle
import streamlit as st
import requests


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]  # this will get index number of the movie
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    # x[0] is index number, x[1] is similarity
    movies_name = []
    movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        movies_poster.append(fetch_poster(movie_id))
        movies_name.append(movies.iloc[i[0]].title)
    return movies_name, movies_poster


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=a077ffed7d63dbeead8a3fcb9053a0d7".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


st.header("Movies Recommendation System Using Machine Learning 🎬🍿🥤")
movies = pickle.load(open('artificial/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificial/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])





