# 🎬 Movie Recommendation System

This project is a content-based Movie Recommendation System built using Python. It recommends movies based on cosine similarity between metadata like genres, keywords, cast, and crew.

## 📂 Features

- Loads TMDB 5000 Movies and Credits datasets
- Cleans and preprocesses metadata
- Computes similarity matrix using `cosine_similarity`
- Streamlit web UI for movie input and recommendations

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

```bash
git clone https://github.com/Harshcooks/Movie-recommendation-sytem.git
cd Movie-recommendation-sytem
pip install -r requirements.txt
```
Download Required Files
Download the required .pkl files from this Google Drive folder:

https://drive.google.com/drive/u/1/folders/1hS0xpvWwNUjhQeYNuSlr7WNDoRKg2Nba

Place the downloaded files in the app/ directory of your project:

```
Edit
project-root/
├── app/
│   ├── similarity.pkl
│   └── movie_dict.pkl
```
### Run the App:
```
streamlit run app.py
```
🛠 Tech Stack
   Python

   Pandas, NumPy

   Scikit-learn

   Streamlit

   Pickle
