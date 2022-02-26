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
      parser.add_argument('screens') # add args
      parser.add_argument('schedule')
        
      args = parser.parse_args() # parse arguments to dict
        
      return {
          'Prediction': '09090'
      }, 200
        
<<<<<<< HEAD
        accessKey = flask.request.args.get('access_token')
        
        if accessKey == key:
              return self.getImpressions()
        else:
              return self.unauthorized()
        
       
    def requestKey(self, length):
           return key
    
    def unauthorized(self):
          return 'UNAUTHORIZED', 401, {'content-type': 'application/json'}
        
    def getImpressions(self): #Claris function
          return 0

        

=======
>>>>>>> 13b9377d26fabd340b2e24767c999eb41069c5fc
api.add_resource(Predictions, '/predictions')

if __name__ == "__main__":
    app.run() # run our Flask app


