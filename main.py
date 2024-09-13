import h5py
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

with h5py.File('movie_recommendation.h5', 'r') as f:
    cosine_sim = f['cosine_sim'][:]
    movie_indices = f['movie_indices'][:]
    movie_titles = np.array(f['movie_titles'], dtype='S')

movie_titles = np.array([title.decode('utf-8') for title in movie_titles])

class MovieRequest(BaseModel):
    movie_title: str

@app.post("/recommend")
async def recommend_movies(request: MovieRequest):
    movie_title = request.movie_title.strip().lower()
    idx = np.where(np.char.lower(movie_titles) == movie_title)[0]

    if len(idx) == 0:
        return {"error": "Movie not found"}

    idx = idx[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    similar_movie_indices = [i[0] for i in sim_scores]
    recommended_movies = [movie_titles[i] for i in similar_movie_indices]

    return {"recommended_movies": recommended_movies}