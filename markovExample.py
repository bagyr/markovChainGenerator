#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import letterChain, markovGenerator

__author__ = 'belverk'

if __name__ == '__main__':
    ch = letterChain.LetterChain()
    ch.fromJson('kapitan.json')
    gen = markovGenerator.MarkovGenerator(ch, 20)
    print gen.makeText(20)
    print gen.makeSequence(20)
