#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import json, codecs

__author__ = 'belverk'

class AbstractChain(object):
    def __init__(self):
        self._table = {}
        self._order = 0

    def fromRawText(self, text, order):
        raise NotImplementedError("Implement this!")

    def fromJson(self, jsonEncoded):
        """
        Restore JSON-encoded markov chain.
        """
        f = codecs.open(jsonEncoded, mode='r', encoding='utf-8')
        text = f.read()
        self._table = json.loads(text, encoding='utf-8')
        self._order = len(self._table.iterkeys().next())
        f.close()

    def getTable(self):
        """
        Returns actual table.
        """
        return self._table

    def getOrder(self):
        """
        Return chain order.
        """
        return self._order

    def toJson(self):
        """
        Serialize table to json.
        """
        return json.dumps(self._table, ensure_ascii = False)
