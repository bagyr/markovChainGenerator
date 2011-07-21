#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import letterChain, markovGenerator, argparse
import codecs

__author__ = 'belverk'

def usage():
    print('Usage toJason.py -i <infile> -o <outfile>')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i')
    parser.add_argument('-o')
    args = parser.parse_args()
    if 'i' not in args.__dict__ or 'o' not in args.__dict__:
        usage()
        sys.exit()

    inFile = codecs.open(args.i, encoding='utf-8', mode='r')
    text = inFile.read()
    chain = letterChain.LetterChain()
    chain.fromRawText(text, 4)
    json = chain.toJson()

    outFile = codecs.open(args.o, mode='w+', encoding='utf-8')
    outFile.write(json)
    outFile.close()
