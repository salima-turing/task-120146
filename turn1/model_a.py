import unittest
from typing import Any

class DataModel:
	def __init__(self, data_source: Any = None):
		self.data_source = data_source

	def load_data(self):
		# Dummy data loading logic for demonstration
		if self.data_source is None:
			self.data = [1, 2, 3, 4, 5]
		else:
			self.data = self.data_source.load_data()

class DataProcessor:
	def __init__(self, data_model: DataModel):
		self.data_model = data_model

	def process_data(self):
		self.data_model.load_data()
		result = sum(self.data_model.data)
		return result

class DummyDataSource:
	def load_data(self):
		return [10, 20, 30]

class TestDataProcessor(unittest.TestCase):
	def test_process_data_with_dummy_data(self):
		# Provide a mock DataModel with dummy data source
		dummy_data_source = DummyDataSource()
		data_model = DataModel(data_source=dummy_data_source)
		data_processor = DataProcessor(data_model)

		result = data_processor.process_data()
		self.assertEqual(result, 60)

if __name__ == '__main__':
	unittest.main()
