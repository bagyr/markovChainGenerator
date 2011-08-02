#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import abstractChain, re, collections

__author__ = 'belverk'

class RingBuffer(object):
    def __init__(self, size):
        self.data = [None for i in xrange(0, size)]

    def append(self, item):
        self.data.pop(0)
        self.data.append(item)

    def get(self):
        return self.data

    def ready(self):
        return any(i != None for i in self._data)


class MorphChain(abstractChain.AbstractChain):
    def __init__(self):
        raise NotImplementedError("Implement this!")

    def fromRawText(self, text, order):
        self._text = text.upper()
        self._order = order
        r = re.compile(r'[\W+-]'. re.U)
        words = r.split(self._upper())
        for word in range(0, len(words) - self._order):
            k

