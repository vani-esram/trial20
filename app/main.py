from flask import Flask, request, render_template, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = {
    1: {"name": "Apple"},
    2: {"name": "Lemon"}
}


class ItemResource(Resource):
    def get(self, id):
        return jsonify(items[id])

    def put(self, id):
        data = request.get_json()
        items[id]['name'] = data['name']
        return items, 200

    def delete(self, id):
        del items[id]
        return items, 200


class itemlistResource(Resource):

    def post(self):
        new_item = request.get_json()
        itemId = len(items.keys()) + 1
        items[itemId] = {'name': new_item['name']}
        return items

    def get(self):
        return items, 200


class itemsResource(Resource):
    def get(self):
        return "Welcome to World"


api.add_resource(ItemResource, '/Item/<int:id>')
api.add_resource(itemlistResource, '/Items')
api.add_resource(itemsResource, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
