from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "nera "
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []

class Item(Resource):
    parser=reqparse.RequestParser() # parser to polsku to analiza skladniowa, no self so it refers to all class
    parser.add_argument('price', type = float, required = True, help = 'any massage, here - this field cannot be blank')

    @jwt_required()
    def get(self, name):

        item = next(filter(lambda x: x["name"]==name, items), None) #filter look for a elements meeting the contidion (function in the first argument) in a list of elemtns(second argument)
        # next is extracting first found element, None argument is a defult whrn there is no elements meeting the contition
        return {"item": item}, 200 if item is not None else 404 #shorter version - 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"]==name, items), None) is not None: #if filtered item is not none = already exists
            return {"message": f"the item with name {name!r} already exists"}, 400 # the code is ok, the user typed in the bad request

        new_item = Item.parser.parse_args()

        item = {"name": name, "price": new_item["price"]}
        items.append(item)
        return item, 201

    def put(self, name):

        data = Item.parser.parse_args() # without paresr it would be request.get_json(), it goes through the arguments and choose the valid ones

        item = next(filter(lambda x: x["name"]==name, items), None)
        if item is None:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        else:
            item.update(data) #function for dictionaries insted doing in example item["price"] = data["price"] for each pair

        return item , 201

    def delete(self, name):
        #if next(filter(lambda x: x["name"]==name, items), None) is None:
        #    return {"message" : f"item of name {name!r} does not exist"}, 400

        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": f"item {name} deleted"}, 201

api.add_resource(Item, '/item/<string:name>')


class ItemsList(Resource):
    def get(self):
        return {"items": items}, 200

api.add_resource(ItemsList, '/items')


app.run(port=5000, debug=True)
