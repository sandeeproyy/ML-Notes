import numpy as np
import statistics
class KNN_Classifier:
    def __init__(self, dist_metric='euclidean'):
        # Store the chosen distance metric
        self.dist_metric = dist_metric

    def get_dist_metric(self, training_data_point, test_data_point):
        # Euclidean distance
        if self.dist_metric == 'euclidean':
            dist = 0
            for i in range(len(training_data_point) - 1):  # skip label
                dist += (training_data_point[i] - test_data_point[i]) ** 2
            return np.sqrt(dist)

        # Manhattan distance
        elif self.dist_metric == 'manhattan':
            manhattan_dist = 0
            for i in range(len(training_data_point) - 1):
                manhattan_dist += abs(training_data_point[i] - test_data_point[i])
            return manhattan_dist

        else:
            raise ValueError("Invalid distance metric. Choose 'euclidean' or 'manhattan'.")

    def nearest_neighbor(self, X_train, test_data, k):
        distance_list = []
        for training_data in X_train:
            distance = self.get_dist_metric(training_data, test_data)
            distance_list.append((training_data, distance))  # store as tuple

        # Sort by distance
        distance_list.sort(key=lambda x: x[1])

        # Get the k nearest neighbors (only the data points, not distances)
        neighbors_list = [distance_list[j][0] for j in range(k)]
        return neighbors_list

    def predict(self, X_train, test_data, k):
        neighbors = self.nearest_neighbor(X_train, test_data, k)

        # Collect all labels
        labels = [data[-1] for data in neighbors]

        # Return the most common label
        predicted_class = statistics.mode(labels)
        return predicted_class
