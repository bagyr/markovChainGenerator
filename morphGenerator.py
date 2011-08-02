#!/usr/bin/python
# vim: set fileencoding=utf-8 :

__author__ = 'belverk'

class MorphologyGenerator(MarkovGenerator):
    
    def __init__(self, chain, separator):
        super(MarkovGenerator, self).__init__(chain, separator)
