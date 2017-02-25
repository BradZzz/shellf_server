import os
import sys
import json
from django.core.management.base import BaseCommand, CommandError
from pymongo import MongoClient
from main.lib.parse import parsedBooks
from main.lib.utils import saveData

class Command(BaseCommand):

    def printt(self,msg):
        self.stdout.write(msg)

    def handle(self, *args, **options):
        # MONGODB = os.environ.get('MONGODB', '')
        # DB_NAME = os.environ.get('DB_NAME', '')
        # if not MONGODB or not DB_NAME:
        #     self.printt(".env variables not set! Please set the vars and run the script again.")
        #     sys.exit()
        # else:

        books = parsedBooks()

        #Create the connection
        self.printt("<-- Creating Connection -->")
        # client = MongoClient(MONGODB)
        # db = client[DB_NAME]

        #Define the tables
        self.printt("<-- Defining Tables -->")
        # glossary = db.glossary
        # words = db.words
        # polarity = db.polarity
        # subjectivity = db.subjectivity
        # similarity = db.similarity
        # condense = db.condense

        # Clear out the current information in all the tables
        self.printt("<-- Flushing Information -->")
        # glossary.remove({})
        # words.remove({})
        # polarity.remove({})
        # subjectivity.remove({})
        # similarity.remove({})
        # condense.remove({})

        # Insert the new data
        self.printt("<-- Inserting New Data -->")
        base = 'analysis/'

        self.printt("Glossary...")
        # glossary.insert(books.list())
        saveData(base + 'glossary.json',json.dumps(books.list()))
        self.printt("Words...")
        # words.insert(books.words())
        saveData(base + 'words.json',json.dumps(books.words()))
        self.printt("Subjectivity...")
        # subjectivity.insert(books.subjectivity())
        saveData(base + 'subjectivity.json',json.dumps(books.subjectivity()))
        self.printt("Polarity...")
        # polarity.insert(books.polarity())
        saveData(base + 'polarity.json',json.dumps(books.polarity()))
        self.printt("Similarity...")
        # similarity.insert(books.similarity())
        saveData(base + 'similarity.json',json.dumps(books.similarity()))
        self.printt("Condense...")
        # condense.insert(books.condense())
        saveData(base + 'condense.json',json.dumps(books.condense()))

        self.printt("Sync Complete!")