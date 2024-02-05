# test_indexing_service.py
import unittest
from indexing_service import IndexingService, DataSource, Item

class TestIndexingService(unittest.TestCase):
    def setUp(self):
        items = [
            Item(1, "Laptop", "High-performance laptop"),
            Item(2, "Mouse", "Ergonomic mouse for gaming"),
            Item(3, "Keyboard", "Mechanical keyboard with RGB lighting"),
        ]
        self.data_source = DataSource(items)
        self.indexing_service = IndexingService(self.data_source)
        self.indexing_service.index_data()

    def test_search_existing_item(self):
        query = "Laptop"
        results = self.indexing_service.search(query)
        self.assertIn(1, results)

    def test_search_non_existing_item(self):
        query = "Headphones"
        results = self.indexing_service.search(query)
        self.assertNotIn(1, results)
        self.assertNotIn(2, results)
        self.assertNotIn(3, results)

    def test_search_partial_query(self):
        query = "gaming"
        results = self.indexing_service.search(query)
        self.assertIn(2, results)

if __name__ == '__main__':
    unittest.main()
