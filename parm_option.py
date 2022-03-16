import argparse


class ParmOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.initialized = False

    def initialize(self):
        # experiment specifics
        self.parser.add_argument('--height', type=int, default='164', help='height option')
        self.parser.add_argument('--weight', type=int, default='64', help='weight option')
        self.parser.add_argument('--chest', type=int, default='93', help='chest option')
        self.parser.add_argument('--waist', type=int, default='76', help='waist option')
        self.parser.add_argument('--hips', type=int, default='102', help='hips option')
        self.parser.add_argument('--inseam', type=int, default='76', help='inseam option')
        self.parser.add_argument('--exercise', type=int, default='1', help='exercise option')
        self.initialized = True
    def parse(self, save=True):
        if not self.initialized:
            self.initialize()
        self.opt = self.parser.parse_args()
        return self.opt