import pandas as pd
from cleantext import clean
# Load model directly
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from transformers import pipeline
# from transformers import BartForConditionalGeneration, BartTokenizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def remove_repetitive_sentences(text, similarity_threshold=0.8):
    # Split text into sentences
    sentences = list(set(text.split(". ")))  # Remove exact duplicates

    # Compute TF-IDF vectors
    vectorizer = TfidfVectorizer().fit_transform(sentences)
    vectors = vectorizer.toarray()

    # Compute cosine similarity between sentences
    similarity_matrix = cosine_similarity(vectors)

    # Remove similar sentences
    unique_sentences = []
    for i, sentence in enumerate(sentences):
        is_duplicate = False
        for j in range(i):
            if similarity_matrix[i][j] > similarity_threshold:  # If similarity is high
                is_duplicate = True
                break
        if not is_duplicate:
            unique_sentences.append(sentence)

    return ". ".join(unique_sentences)

def clean_comments(df):
    df['clean_text'] = df['text'].apply(lambda x: clean(x, lower=False, no_emoji=True))
    df = df[df['clean_text'].str.split().str.len() > 2]
    df = df.drop_duplicates(subset=['clean_text'])
    result = ', '.join(df['clean_text'])
    return result

# df = pd.read_csv('youtube_comments_Squpd-w-Uk8.csv', delimiter=',', header='infer')
# result = clean_comments(df)
# result = remove_repetitive_sentences(result)
# print(result)



text = """ This coding tutorial is highly praised for its clear and engaging teaching skills. It is highly praised for its clear explanations and clear explanations. The instructor is highly praised for its clear explanations and clear explanations. This coding tutorial is highly praised for its clear explanations and clear explanations. 
The video is highly praised for its clear explanations and clear explanations. The video is highly praised for its clear explanations. This coding tutorial is highly praised for its clarity and clarity. It is highly praised for its clarity and clarity. The video is highly praised for its clarity and clarity. 
This coding tutorial is highly praised for its positive energy and good vibes. The instructor's comments are highly praised for its clear explanations and clear explanations. The video is highly praised for its clear explanations and clear explanations, highlighting the difficulty with naming the app in the INSTALLED_APPS. 
This coding tutorial is highly praised for its clear and engaging teaching style. The video is highly praised for its clear and effective teaching style, with viewers expressing gratitude for the tutorial's excellent teaching style. The tutorial is highly praised for its clear explanations and clear explanations. This coding tutorial is highly praised for its clarity and clarity. 
The video is highly praised for its clarity and clarity. The video is highly praised for its clarity and clarity. This coding tutorial is highly praised for its clear explanations and clear explanations. The instructor is also praised for its clear explanations and clear explanations. The tutorial is highly praised for its clear explanations and clear explanations. 
This coding tutorial is highly praised for its clear explanations and clear explanations. The video is highly praised for its clear explanations and clear explanations. The video is highly praised for its clear explanations and clear explanations. This coding tutorial is highly praised for its clarity and practicality. The video is highly praised for its clear explanations and clear explanations. 
The tutorial is highly praised for its clear explanations and clear explanations. This coding tutorial is highly praised for its clear and engaging content. The video is highly praised for its clear and clear explanations. The video is highly praised for its clarity and clarity. This coding tutorial is highly praised for its clarity, interactively and intuitively. The viewer appreciates the tutorial's clear explanations and clear explanations. 
The video is highly praised for its clear explanations and clear explanations. This coding tutorial is highly praised for its clarity and practicality. The video is highly praised for its clear explanations and clear explanations. This coding tutorial is highly praised for its clear explanations and clear explanations. The video is highly praised for its clear explanations and clear explanations. 
The instructor's understanding of Django is highly praised for its clear explanations and clear explanations. This coding tutorial is highly praised for its clear and detailed explanations. The tutorial is highly praised for its clear and detailed explanations, including the use of the command 'django-admin' and the use of GET to retrieve information. The tutorial is highly praised for its clear and detailed explanations, including the use of the command 'django-admin'. 
This coding tutorial is highly praised for its clarity and clarity. The video is highly praised for its clarity and clarity. The video is highly praised for its clarity and clarity. This coding tutorial is highly praised for its clarity and clarity. The video is highly praised for its clear and concise explanations. The video is highly praised for its clarity and clarity. This coding tutorial is highly praised for its clear explanations and usefulness. 
The reviewer expresses gratitude for the tutorial's ability to delete a database file from python.
"""

# text = remove_repetitive_sentences(text)
# print(text)

