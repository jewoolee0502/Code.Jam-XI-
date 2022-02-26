from http.client import UNAUTHORIZED
import flask
from flask_restful import Resource, Api, reqparse
import ast
import secrets
import random
import string

app = flask(__name__)
api = Api(app)

'''
The schema for the payload: 
{
  "screens": [<list of screen ids>],
  "schedule": [
    "Mon-00", // Monday at midnight
    "Mon-01", // Monday at 1 am
    "Tue-13", // Tuesday at 1pm
    ...
  ]
}
'''


key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits)for _ in range(16))

class Predictions(Resource):
  
  def post(self):
      parser = reqparse.RequestParser() # initialize
      parser.add_argument('screens', required=True) # add args
      parser.add_argument('schedule', required=True)
        
      args = parser.parse_args() # parse arguments to dict
        
        
      accessKey = flask.request.args.get('access_token')
        
      if accessKey != key:
            return self.unauthorized()
      
      return {
          'Prediction': self.getImpressions()
      }, 200
        
        
      
        
       
  def requestKey(self, length):
        return key
    
  def unauthorized(self):
        return 'UNAUTHORIZED', 401, {'content-type': 'application/json'}
        
  def getImpressions(self): #Claris function
        return 0

        
api.add_resource(Predictions, '/predictions')

if __name__ == "__main__":
    app.run() # run our Flask app


