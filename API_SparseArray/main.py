from flask import Flask, request
from flask_restful import Resource, Api
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

from flasgger import Swagger
from flasgger.utils import swag_from
from flask_restful_swagger import swagger

from SparseArray import SparsArrayClass
import os

app = Flask(__name__)
api = Api(app)
port = 5000

limiter = Limiter(app, key_func=get_remote_address)
limiter.init_app(app)
 
api = swagger.docs(api,apiVersion='0.1',api_spec_url = '/docs')



class SparseArrayAPI(Resource):
    @swagger.model
    @swagger.operation(notes='Enter string input separated by underscore "_" to get \
                              the number of time it shows up in our string array')

    def get(self,queries_input,strings):
        #Processing user input with underscore to access it more easily with url
        queries = queries_input.split(sep='_')
        #Defining string input
        strings = os.getenv('STRINGS',['ab','abc','abc','abc','bc','bc'])
        #Computing our function
        result = SparsArrayClass.matchingStrings(strings, queries) 
        return {"Response":200,
                'Data':result
                }

#we get access to our API with the input
api.add_resource(SparseArrayAPI,'/MatchingStrings/<string:queries_input>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
    
