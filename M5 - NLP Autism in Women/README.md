# NLP Autism in Women

This is the README file for the NLP Autism in Women project, which is available at the following GitHub repository: https://github.com/ericajstevenson/METIS_projects/tree/main/M5%20-%20NLP%20Autism%20in%20Women.

## Project Overview

The NLP Autism in Women project aims to analyze social media data, specifically posts from Reddit, to identify the key challenges and experiences faced by women with autism. The project uses Natural Language Processing (NLP) techniques to extract insights from several forums that are specifically for women with autism and uses NLP techniques to compare those with general forums on the same topic.

## Repository Contents

This project contains several Jupyter Notebooks, each covering different aspects of the project:

1. `1 - Reddit Scrape with PRAW.ipynb`: Data collection from Reddit using the PRAW library.
2. `2 - Data Cleaning - SpaCy and NLTK.ipynb`: Data preprocessing and cleaning using SpaCy and NLTK libraries.
3. `3 - NLP analysis.ipynb`: Natural Language Processing techniques applied to the cleaned data.
4. `4 - Recommendation System.ipynb`: Building a recommendation system based on the NLP analysis.
5. `5 - CorEx Anchored Topic Modeling and Sentiment Analysis.ipynb`: Topic modeling and sentiment analysis using the CorEx library.

### Dependencies

To run the project, you need to have the following dependencies installed:

- Python 3.x
- Jupyter Notebook
- pandas
- numpy
- scikit-learn
- nltk
- spaCy
- seaborn
- matplotlib
- wordcloud
- praw
- corextopic

### Dataset

The dataset used in this project consists of Reddit posts collected from the subreddits r/aspergirls and r/autism. The data was obtained using the Python Reddit API Wrapper (PRAW).

## Project Steps

The project follows these steps:

1. Data Collection
2. Data Preprocessing
3. Text Tokenization
4. Feature Extraction
5. Topic Modeling
6. Sentiment Analysis
7. Visualization and Insights
8. Building a Recommendation System

## Usage

To use this project, follow these steps:

1. Clone the repository or download the Jupyter Notebook files.
2. Install the required dependencies.
3. Create a `praw.ini` file with your Reddit API credentials. See [PRAW documentation](https://praw.readthedocs.io/en/stable/getting_started/authentication.html) for more information on obtaining credentials.
4. Open the Jupyter Notebook files using Jupyter Notebook.
5. Run the notebook cells in sequence.

## Contact

If you have any questions or concerns, please feel free to reach out to the project maintainer, Erica Stevenson, at ericajstevenson@gmail.com.
