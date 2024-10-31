import unittest
from scripts.preprocess_data import clean_text

class TestDataPreprocessing(unittest.TestCase):

    def test_clean_text(self):
        self.assertEqual(clean_text("Hello, World!"), "hello world")
        self.assertEqual(clean_text("Data123"), "data123")
        self.assertEqual(clean_text("Pertanyaan tentang buku, pembayaran dan hafalan"), "buku pembayaran hafalan")
        self.assertEqual(clean_text("Pembayaran Kelas SLPI"), "pembayaran kelas slpi")

if __name__ == "__main__":
    unittest.main()
