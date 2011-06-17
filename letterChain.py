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
        self._text = re.sub(r'[^a-zA-Zа-яА-Я ]', '', self.rawText)
        self._text = re.sub(r' {2,}', ' ', self._text)
        self._text = self._text.lower()
        for i in range(0, len(self._text) - self._order):
            key = self._text[i:i+self._order]
            if ' ' in key or '\n' in key:
                continue
            if not key in self._table:
                self._table[key] = collections.Counter(
                        self._text[i+self._order])
            else:
                self._table[key][
                        self._text[i+self._order]] += 1

    def getOrder(self):
        return self._order