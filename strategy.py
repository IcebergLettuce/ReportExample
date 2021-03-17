from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from ml.linear import LinearModel
import os
import numpy as np
import datetime

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


class StrategyBuilder:

    def __init__(self, config):
        self.config = config
        self.config['rdir'] = os.path.join(self.config['root'],self.config['experiment'])

    def get_strategy(self,command):
        
        '''
        Here we can do some preflight checks before we execute a strategy
        '''

        if command == 'train':

            if not os.path.exists(self.config['rdir']):
                raise FileNotFoundError('Use the initialisation command first.')

            return TrainStrategy(self.config)

        elif command == 'init':
            if os.path.exists(self.config['rdir']):
                raise FileNotFoundError('Experiment already exists!')

            return InitialisationStrategy(self.config)

        elif command == 'report':
            return ReportStrategy(self.config)
        
        else:
            raise NotImplementedError('Strategy does not exist')


class Strategy(ABC):

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def run(self) -> None:
        pass




class InitialisationStrategy(Strategy):
    def run(self) -> None:
        os.mkdir(self.config['rdir'])




class TrainStrategy(Strategy):
    def run(self) -> None:

        if self.config['ml']['model'] == 'linear':
            model = LinearModel()
            model.fit(None,None)
            result = model.predict(None)
            np.savez(os.path.join(self.config['rdir'],'result.npz'), result = result)

        else:
            raise NotImplementedError()

        return "{Result of the Train Strategy}"



class ReportStrategy(Strategy):
    def run(self) -> None:
        file = np.load(os.path.join(self.config['rdir'],'result.npz'))
        data = file['result']

        mean = np.mean(data)
        std = np.std(data)


        general = {}
        general['mean'] = mean
        general['std'] = std
        general['name'] = self.config['experiment']
        general['date'] = datetime.datetime.now()

        env = Environment(loader=FileSystemLoader(searchpath=''))
        template = env.get_template('template.html')

        html_out = template.render(general)
        HTML(string = html_out).write_pdf(os.path.join(self.config['rdir'],'report.pdf'))
        



class SomeStrategy(Strategy):
    def run(self) -> None:

        '''
        Do Some other stuff..

        '''
        return "{Result of the Generate Strategy}"


