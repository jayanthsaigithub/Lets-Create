# indexing_service.py

class IndexingService:
    def __init__(self, data_source):
        self.data_source = data_source
        self.index = {}

    def index_data(self):
        for item in self.data_source.get_items():
            indexed_item = self._process_item(item)
            self.index[item.id] = indexed_item

    def search(self, query):
        results = []
        for item_id, indexed_item in self.index.items():
            if query in indexed_item.values():
                results.append(item_id)
        return results

    def _process_item(self, item):
        indexed_item = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            # Add more fields to index as needed
        }
        return indexed_item


class DataSource:
    def __init__(self, items):
        self.items = items

    def get_items(self):
        return self.items


class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
