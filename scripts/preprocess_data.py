import Sastrawi.Stemmer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from nltk.corpus import stopwords
import langdetect
from langdetect import detect
import Sastrawi
from nltk.stem import WordNetLemmatizer
import pickle

def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    cleaned_data = []
    
    for text in data['Description']:
        try:
            lang = detect(text)  # Detect language (either 'en' or 'ms')
        except:
            lang = 'unknown'
            
        # Cleans text data by removing special characters and punctuation.
        text = re.sub(r'\W+', ' ', text)  # Remove special characters
        text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
        
        # Initialize stop words and stemmers for both languages
        nltk_stop_words = set(stopwords.words("english"))
        custom_stop_words = ["pertanyaan", "tentang", "bin", "bte", "mengenai", "enquiry", "berkenaan"]  # Custom Malay stopwords
        all_stop_words = nltk_stop_words.union(custom_stop_words)
        
        # Tokenize and remove stop words
        words = text.lower().split()
        lemmatizer = WordNetLemmatizer()
        
        if lang == 'en':
            filtered_words = [word for word in words if word not in all_stop_words]
            stemmed_words = [lemmatizer.lemmatize(word) for word in filtered_words]  # Stem the words
        elif lang == 'ms':  # 'ms' stands for Malay language in langdetect
            filtered_words = [word for word in words if word not in custom_stop_words]
            stemmed_words = [Sastrawi.Stemmer(word) for word in filtered_words]  # Stem the words
        else:
            stemmed_words = words  # If language not recognized, leave the words as is
        
        cleaned_text = " ".join(stemmed_words)
        cleaned_data.append(cleaned_text)

    data['cleaned_text'] = cleaned_data

    vector_stop_words = list(all_stop_words)
    vectorizer = TfidfVectorizer(stop_words=vector_stop_words)
    vectors = vectorizer.fit_transform(data['cleaned_text'])
    
    # Save vectorizer for later use in app.py
    with open('../models/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

    return vectors 



if __name__ == "__main__":
    data = load_data('C:\\Users\\USER\\Desktop\\Client Data Projects\\FAQ-Generation-Project-main\\data\\enquiries.csv')
    vectors = preprocess_data(data)
    print("Data preprocessing completed.")

    # Save the vectors to a pickle file
    with open('../models/vectorized_data.pkl', 'wb') as f:
        pickle.dump(vectors, f)
    print("Vectorized data saved successfully.")
