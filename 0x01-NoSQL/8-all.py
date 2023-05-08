#!/usr/bin/env python3
"""  lists all documents in a collection
"""

import pymongo


def list_all(mongo_collection):
    """ list all documents
    """
    docs = mongo_collection.find()
    return [x for x in docs]