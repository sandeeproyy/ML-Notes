import numpy as np
class Linear_Regression( ):

  # intiating the parameters (learning rate & no of iterations)
  def __init__(self, learning_rate, n_iters):

    self.learning_rate = learning_rate
    self.n_iters = n_iters


  def fit(self, X, Y):

    # no of training exaples and no of features
    self.m, self.n = X.shape   # no of rows(n) and columns(m)

    # initiating the weight and bias
    self.w = np.zeros(self.n)
    self.b = 0
    self.X = X
    self.Y = Y

    # Implementing Gradient Descent

    for i in range(self.n_iters):
      self.update_weights()

  def update_weights(self):

    Y_prediction = self.predict(self.X)

    # calculate gradients

    dw = - (2 * (self.X.T).dot(self.Y - Y_prediction)) / self.m
    db = - 2 * np.sum(self.Y - Y_prediction) / self.m

    # updating the weights

    self.w = self.w - self.learning_rate * dw
    self.b = self.b - self.learning_rate * db

  def predict(self, X):

    return X.dot(self.w) + self.b