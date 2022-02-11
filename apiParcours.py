from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Car(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rideLength', type=int, default=1)
        parser.add_argument('fastChargeTime', type=int, default=0)
        parser.add_argument('chargeTime', type=int, default=20)
        parser.add_argument('batterySize', type=int, default=50)
        parser.add_argument('averageSpeed', type=int, default=60)
        args = parser.parse_args()



        time = (args['rideLength']*1000/(args['averageSpeed']/3.6))
        print(args['rideLength']>args['batterySize'])
        if(args['rideLength']>args['batterySize']):
            print("Ride length is greater than battery size")
            if(args['fastChargeTime']!=0):

                time+=args['fastChargeTime']*60*(args['rideLength']//args['batterySize'])

            else:
                time+=args['chargeTime']*60*(args['rideLength']//args['batterySize'])

        return time

api.add_resource(Car, '/Car')
api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run()