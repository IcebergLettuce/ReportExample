from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class ModelBase(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def fit(self, X,y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    @abstractmethod
    def refit(self, X,y):
        pass

