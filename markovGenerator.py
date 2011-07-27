#!/usr/bin/python
# vim: set fileencoding=utf-8 :

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
                elements = self._table[out[-self._order:]].keys()
                out += random.choice(elements)
#                out += random.choice(list(
#                    self._table[out[-self._order:]].elements())) \
#                    + self.separator
                #print(out[-self._order:])
            except KeyError:
                return out
        return out

    def makeSequence(self, numWords, maxWordLen = 40):
        """
        Generate sequence of random texts.
        """
        out = ''
        for i in range(numWords):
            out += self.makeText(maxWordLen) + ' '

    def fromChain(self, chain):
        self._table = chain.getTable()
        self._order = chain.getOrder()
