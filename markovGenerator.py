#!/usr/bin/python
# vim: set fileencoding=utf-8 :

__author__ = 'belverk'

import random

class MarkovGenerator(object):

    def __init__(self, chain, separator):
        self._table = chain.getTable()
        self._order = chain.getOrder()
        self.separator = separator

    def makeText(self, maxLen = 40):
        """
        Generates random text according to specified table.
        """
        out = random.choice(self._table.keys()) 
        while len(out) <= maxLen:
            try:
                elements = []
                for i, j in self._table[out[-self._order:]].iteritems():
                    elements += [i] * j
                out += random.choice(elements)
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
        return out

    def fromChain(self, chain):
        self._table = chain.getTable()
        self._order = chain.getOrder()
