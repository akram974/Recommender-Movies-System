import streamlit as st
import pickle
import pandas as pd
import requests


custom_css = """
<style>
body {
    background-color: #3498db;  /* Replace with your preferred shade of blue */
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown(custom_css, unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie, recommended_movie_posters

st.header('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_movie_posters[4])

