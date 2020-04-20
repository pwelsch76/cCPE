"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app

class Multi(Resource):
       
       def post(self):
            some_json = request.get_json()
            return {"Enviado": some_json}, 201

       def get(self, num):
            return {'result': num*10}

api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    import os
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
        #PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
        #PORT = 5555
    app.run(debug=False)
