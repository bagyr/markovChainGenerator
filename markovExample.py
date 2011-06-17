import letterChain, markovGenerator

__author__ = 'belverk'

def test(order):
    """
    Simple test.
    """
    global text, generator, chain
    chain.fromRawText(text, order)
    print("Order: {0}; Dict size: {1}".format(
        order, len(chain.getTable().keys())))
    generator.fromChain(chain)
    print(generator.makeText())
    print(generator.makeSequence(20))


file = open("azimov_foundation.txt", "r")
text = file.read()

chain = letterChain.LetterChain()
generator = markovGenerator.MarkovGenerator(chain, "")

if __name__ == '__main__':
    for i in range(1, 4):
        test(i)