import unittest
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from scripts.cluster_faq import perform_clustering, save_model

class TestClustering(unittest.TestCase):

    def setUp(self):
        """Set up sample data and vectorize it."""
        self.data = ["What is AI?", "How does ML work?", "Explain NLP concepts."]
        vectorizer = TfidfVectorizer(stop_words='english')
        self.vectors = vectorizer.fit_transform(self.data)

    def test_perform_clustering(self):
        """Test if clustering works as expected."""
        model = perform_clustering(self.vectors, num_clusters=2)
        self.assertEqual(model.n_clusters, 2)

    def test_save_model(self):
        """Test if the model saves correctly."""
        model = perform_clustering(self.vectors, num_clusters=2)
        save_model(model, 'models/test_cluster_model.pkl')
        self.assertTrue(os.path.exists('models/test_cluster_model.pkl'))
        os.remove('models/test_cluster_model.pkl')  # Clean up after test

if __name__ == "__main__":
    unittest.main()
