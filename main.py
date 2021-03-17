import sys
import argparse
import logging
import yaml
import os
from strategy import StrategyBuilder


# Some important config stuff that we need to do to run the app..
# Can also be refactored into an own 'module/package' whatever
logging.basicConfig(filename='log.log', level=logging.DEBUG)

# We need the root dir of the project, that we can build the filesystem
# ATTENTION: I would generally build the filesystme outside of the code project!
# But like that it is easier to demonstrate the flow

root = os.path.dirname(os.path.abspath(__file__))

with open('app-configuration.yaml','r') as f:
    configuration = yaml.safe_load(f)

if __name__ == "__main__":
    
    # We use argparse library to control the flow of the code ad execute different commands 
    parser = argparse.ArgumentParser(description='Application shell that can do bla bla.')
    parser.add_argument('command', help = 'Task to execute')
    parser.add_argument('--name', help = 'Name of the Experiment', required= True)
    args = parser.parse_args()

    # we add the experiment name to the config that we can easily inject it to the other classes
    configuration['experiment'] = args.name
    configuration['root'] = root
    
    strategy = StrategyBuilder(configuration).get_strategy(args.command)
      
    logging.info(f'Running strategy: {args.command}')

    try:
        result = strategy.run()
        logging.info(f'Execution done..!')
        sys.exit(0)

    except Exception as e:
        logging.error(f'Uuppps... some error occured: {e}')
        sys.exit(-1)