__author__ = 'belverk'

import random

class MarkovGenerator:

    def __init__(self, chain, separator):
        self._table = chain.getTable()
        self._order = chain.getOrder()
        self.separator = separator

    def makeText(self, maxLen = 40):
        """
        Generates random text according to specified table.
        """
        out = random.choice(list(self._table.keys()))
        while len(out) <= maxLen:
            try:
                out += random.choice(list(
                    self._table[out[-self._order:]].elements())) + self.separator
                #print(out[-self._order:])
            except KeyError:
                return out
        return out

    def makeSequence(self, numWords, maxWordLen = 40):
        """
        Generate sequence of random texts.
        """
        for i in range(numWords):
            print(self.makeText(maxWordLen), end=" ")

    def fromChain(self, chain):
        self._table = chain.getTable()
        self._order = chain.getOrder()