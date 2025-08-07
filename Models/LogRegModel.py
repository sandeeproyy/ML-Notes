import numpy as np
class Logistic_Regression():

  def  __init__(self, learning_rate, n_iters):

    self.learning_rate = learning_rate
    self.n_iters = n_iters

  def fit(self, X, Y):

    self.m, self.n = X.shape  # m -->no of rows, n--->no of colummns(features)

    self.w = np.zeros(self.n)
    self.b = 0
    self.X = X
    self.Y = Y

    # gradient descent algo:
    for i in range(self.n_iters):
      self.update_weights()

  def update_weights(self):

    Y_hat = 1 / (1 + np.exp(-(self.X.dot(self.w) + self.b)))  #sigmoid function
    dw = (1/self.m) * np.dot(self.X.T, (Y_hat - self.Y))
    db = (1/self.m) * np.sum(Y_hat - self.Y)

    self.w = self.w - self.learning_rate * dw
    self.b = self.b - self.learning_rate * db


 # writing the sigmoid equation and decision boundary
  def predict(self, X):

    Y_pred = 1 / (1 + np.exp(-(self.X.dot(self.w) + self.b)))
    Y_pred = np.where( Y_pred > 0.5, 1, 0)
    return Y_pred