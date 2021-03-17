import signal
import sys

class Signals:
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum, frame):
        print('Disposing Resources')
        print('Gracefully Stopping Application!')
        sys.exit()

