#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import abstractChain, re, collections

__author__ = 'belverk'

class LetterChain(abstractChain.AbstractChain):

    def __init__(self):
        abstractChain.AbstractChain.__init__(self)

    def fromRawText(self, text, order):
        """
        Generate markov chain from raw text
        """
        self._order = order
        self.rawText = text
        self._text = re.sub(ur'[^a-zA-Zа-яА-Я ]', '', self.rawText)
        self._text = re.sub(ur' {2,}', ' ', self._text)
        self._text = self._text.lower()
        for i in range(0, len(self._text) - self._order):
            key = self._text[i:i+self._order]
            if ' ' in key or '\n' in key:
                continue
            if not key in self._table:
#                self._table[key] = collections.Counter(
#                        self._text[i+self._order])
                self._table[key] = {self._text[i+self._order]: 1}
            if not self._text[i+self._order] in self._table[key]:
                self._table[key][self._text[i+self._order]] = 0
            self._table[key][self._text[i+self._order]] += 1            

    def getOrder(self):
        return self._order
