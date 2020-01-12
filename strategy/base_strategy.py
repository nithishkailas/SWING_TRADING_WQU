import pandas as pd
from abc import ABC,abstractmethod
class Strategy(ABC):

    def __init__(self,Name,Portfolio):
        self.Name = Name
        self.Portfolio = Portfolio


    @abstractmethod
    def create_features(self):
        return NotImplementedError

    @abstractmethod
    def create_labels(self):
        return NotImplementedError

    @abstractmethod
    def create_model(self):
        return NotImplementedError

    @abstractmethod
    def train(self):
        return NotImplementedError

    @abstractmethod
    def backtest(self):
        return NotImplementedError

    @abstractmethod
    def generate_results(self):
        return NotImplementedError





