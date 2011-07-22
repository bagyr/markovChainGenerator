#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import letterChain, markovGenerator, argparse
import codecs, sys

__author__ = 'belverk'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'Convert raw text to JSON Markov net.')
    parser.add_argument('-i', type = str, help = 'Take input from file')
    parser.add_argument('-o', type = str, help = 'Output to file')
    args = parser.parse_args()

    if args.i is not None:
        inFile = codecs.open(args.i, encoding='utf-8', mode='r')
        text = inFile.read()
        inFile.close()
    else:
        text = sys.stdin.read().decode('utf-8')

    chain = letterChain.LetterChain()
    chain.fromRawText(text, 4)
    json = chain.toJson()

    if args.o is not None:
        outFile = codecs.open(args.o, encoding='utf-8', mode='w')
        outFile.write(json.decode('utf-8'))
        outFile.close()
    else:
        print(json.encode('utf-8'))
