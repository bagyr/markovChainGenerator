#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import json

__author__ = 'belverk'

class AbstractChain:
    def __init__(self):
        self._table = {}
        self._order = 0

    def fromRawText(self, text, order):
        raise NotImplementedError("Implement this!")

    def fromJson(self, jsonEncoded):
        """
        Restore JSON-encoded markov chain.
        """
        self._table = json.loads(jsonEncoded)

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
        return json.dumps(self._table)
