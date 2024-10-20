# real_time_analytics/test_data_model.py
import unittest
from unittest.mock import Mock
from data_model import DataModel
from data_model import DataSource


class TestDataModel(unittest.TestCase):
    def test_calculate_average_with_dummy_data(self):
        # Dummy data source with predefined data
        dummy_data = [1, 2, 3, 4, 5]
        dummy_data_source = Mock(spec=DataSource)
        dummy_data_source.get_data.return_value = dummy_data

        # Create the data model with the dummy data source
        data_model = DataModel(dummy_data_source)

        # Calculate the average
        average = data_model.calculate_average()

        # Verify the result
        self.assertEqual(average, 3.0)

    def test_calculate_average_with_empty_data(self):
        # Empty data source
        empty_data_source = Mock(spec=DataSource)
        empty_data_source.get_data.return_value = []

        data_model = DataModel(empty_data_source)
        average = data_model.calculate_average()
        self.assertEqual(average, 0.0)


if __name__ == '__main__':
    unittest.main()
