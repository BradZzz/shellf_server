from main.lib.utils import openFile

# This file reads the analysis files and formats them appropriately
class reader():

    base = 'analysis/'

    def glossary(self):
        return openFile(self.base + 'glossary.json')

    def condense(self):
        return openFile(self.base + 'condense.json')

    def polarity(self):
        return openFile(self.base + 'polarity.json')

    def similarity(self):
        return openFile(self.base + 'similarity.json')

    def subjectivity(self):
        return openFile(self.base + 'subjectivity.json')

    def words(self):
        return openFile(self.base + 'words.json')