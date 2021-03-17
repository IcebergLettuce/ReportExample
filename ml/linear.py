from .base import ModelBase
import numpy as np

class LinearModel(ModelBase):

    def __init__(self):
        pass

    def fit(self, X,y):
        pass

    def predict(self, X):
        return np.random.normal(0,10,100)

    def refit(self, X,y):
        pass
