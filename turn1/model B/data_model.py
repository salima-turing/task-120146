# real_time_analytics/data_model.py

class DataModel:
    def __init__(self, data_source):
        self.data_source = data_source

    def calculate_average(self):
        data = self.data_source.get_data()
        total = sum(data)
        if len(data) == 0:
            return 0
        return total / len(data)

# real_time_analytics/data_source.py

class DataSource:
    def get_data(self):
        raise NotImplementedError
