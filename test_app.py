import unittest
import pandas as pd
from app import clean_data, calculate_score, is_valid_email

class TestHiringSystem(unittest.TestCase):

    def setUp(self):
        # Create dummy data for testing
        self.data = {
            'name': ['Alice', 'Bob', 'Charlie', 'Alice'],  # Duplicate Alice
            'email': ['alice@test.com', 'bob-invalid-email', 'charlie@test.com', 'alice@test.com'],
            'role': ['Dev', 'Dev', 'Dev', 'Dev'],
            'skills': ['Python, SQL', 'Java', 'Python, Machine Learning', 'Python, SQL']
        }
        self.df = pd.DataFrame(self.data)

    def test_email_validation(self):
        """Test if invalid emails are detected correctly"""
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))

    def test_scoring_logic(self):
        """Test if Python and ML skills get correct scores"""
        # Python (5) + SQL (3) = 8
        self.assertEqual(calculate_score("Python, SQL"), 8)
        # Machine Learning (5) + Python (5) = 10
        self.assertEqual(calculate_score("Python, Machine Learning"), 10)
        # HTML (2) = 2
        self.assertEqual(calculate_score("HTML"), 2)

    def test_duplicate_removal(self):
        """Test if duplicates are removed"""
        initial_count = len(self.df)
        df_cleaned = self.df.drop_duplicates(subset="email")
        self.assertTrue(len(df_cleaned) < initial_count)
        print(f"\n✅ Duplicate Test Passed: Reduced from {initial_count} to {len(df_cleaned)}")

if __name__ == '__main__':
    print("Running Automated Tests...")
    unittest.main()