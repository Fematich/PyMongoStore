#!/usr/bin/env python
"""
@author:    Matthias Feys (matthiasfeys@gmail.com), IBCN (Ghent University)
@date:      Mon Nov 18 15:28:16 2013
"""
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client['work']
datastore = db['datastore']

def MongoStore(func):
    '''
    This decorator makes an entry in the logger database with the function-name, the variables
    and the resulting output
    '''
    def mongologger(**kwargs):
        res=func(**kwargs)
        call['result']=res
        call['parameters']=kwargs
        datastore.insert(call)
        return res
    call={'name':str(func.__name__),'timestamp':str(datetime.datetime.now())}
    
    return mongologger
    
    
#class mongostore(class):
#    '''
#    This decorator makes an entry in the logger database for the assigned class, TODO
#    '''