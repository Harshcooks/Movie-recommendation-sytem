import streamlit as st
import pandas as pd
import pickle

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# Page setup
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.markdown("## 🎥 *Movie Recommender System*")
st.markdown("Get similar movie suggestions based on your favorite picks!")

# Movie selection
selected_movie_name = st.selectbox(
    "🎞️ Choose a movie from the list:",
    movies['title'].values
)

# Recommend button
if st.button('🎯 Recommend'):
    with st.spinner('Finding the best movies for you...'):
        recommendations = recommend(selected_movie_name)

    st.markdown("---")
    st.markdown("### 🔍 Recommended Movies:")
    
    for idx, movie in enumerate(recommendations, 1):
        with st.container():
            st.markdown(f"**{idx}.** 🎬 *{movie}*")

# Optional footer
st.markdown("---")
st.markdown("<p style='text-align:center; font-size: 13px;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
