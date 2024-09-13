# Abisha Movie Buzz

## Overview
Abisha Movie Buzz is a movie recommendation system that uses cosine similarity to recommend movies based on their features such as genres, actors, and more. This system is built using FastAPI for the backend API and integrates an automated CI/CD pipeline for seamless deployment.

## Features
- **Cosine Similarity**: Provides movie recommendations by comparing feature vectors.
- **FastAPI**: API backend for querying recommendations.
- **CI/CD Pipeline**: Deployed on Koyeb using GitHub Actions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Abishanavam/Abisha-Movie-Buzz.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Abisha-Movie-Buzz
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```
2. Access the API at:
   ```bash
   http://127.0.0.1:8000/docs
