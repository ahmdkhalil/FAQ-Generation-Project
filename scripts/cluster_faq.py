import os
from sklearn.cluster import KMeans
import pickle

def perform_clustering(vectors, num_clusters=5):
    """Applies KMeans clustering to vectorized data."""
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(vectors)
    return kmeans

def save_model(model, model_path):
    """Saves the clustering model."""
    # Save in the same directory as cluster_faq.py
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    # Load preprocessed vectorized data
    with open('../models/vectorized_data.pkl', 'rb') as f:  # Adjust path to go up one level
        vectors = pickle.load(f)
    print("Vectorized data loaded successfully.")

    # Perform clustering on loaded vectors
    kmeans_model = perform_clustering(vectors)
    save_model(kmeans_model, '../models/faq_cluster_model.pkl')  # Save in the current directory
    print("Clustering completed and model saved.")
