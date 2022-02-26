from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

app = Flask(__name__)
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

class Predictions(Resource):
  
  def post(self):
      parser = reqparse.RequestParser() # initialize
      parser.add_argument('screens') # add args
      parser.add_argument('schedule')
        
      args = parser.parse_args() # parse arguments to dict
        
      return {
          'Prediction': '09090'
      }, 200
        
api.add_resource(Predictions, '/predictions')

if __name__ == "__main__":
    app.run() # run our Flask app
