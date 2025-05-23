import streamlit as st

# Assuming you have a function like this:
def recommend(movie):
    # Replace this with your real logic
    return ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]

# Streamlit App
st.title("🎬 Movie Recommendation System")

# Search box
movie_name = st.text_input("Enter a movie name")

# Recommend button
if st.button("Recommend"):
    if movie_name:
        recommendations = recommend(movie_name)
        st.subheader("Recommended Movies:")
        for i, movie in enumerate(recommendations, start=1):
            st.write(f"{i}. {movie}")
    else:
        st.warning("Please enter a movie name.")
