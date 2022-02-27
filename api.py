from http.client import UNAUTHORIZED
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast
import secrets
import random
import string
import joblib
import pandas as pd
from pathlib import Path

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

key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits)for _ in range(16))


class Predictions(Resource):
  
  def post(self):
      data = request.get_json()
      # parser = reqparse.RequestParser() # initialize
      # parser.add_argument('screens', required=True) # add args
      # parser.add_argument('schedule', required=True)
        
      # args = parser.parse_args() # parse arguments to dict
        
      # accessKey = request.args.get('access_token')
        
      # if accessKey != key:
      #       return self.unauthorized()
      
      return {
          'Prediction': self.get_impressions(data)
      }, 200


  @app.route("/requestKey", methods=["GET"])
  def requestKey():
      return key
    
  def unauthorized(self):
      return 'UNAUTHORIZED', 401, {'content-type': 'application/json'}
        
  # def getImpressions(self): #Claris function
  #     return 0
      
  # Load the model from pickles
  # def loadModel ():
  #     return pickle.loads('my_model.pkl')
      
  def get_impressions(self, data):
      return self.model.predict(self.adapt_input(data))
    
    
  def adapt_input(self, json_input):
      data = json_input
      # data = pd.read_json(json_input)
      data['schedule'] = pd.to_datetime(data['schedule'], format='%a-%d')
      assert data['schedule'].isnull().sum() == 0, "missing Date"
      data['Date_hour'] = data['schedule'].hour
      data['Date_dayofweek'] = data['schedule'].dayofweek
      return data
      
  def __init__(self):
      self.model = joblib.load(open(Path(__file__).with_name('my_model.pkl'), 'rb'))

api.add_resource(Predictions, '/predictions')

if __name__ == "__main__":
    app.run() # run our Flask app
    #model = joblib.load(open(Path(__file__).with_name('my_model.pkl'), 'rb'))
    #print("hurray")
