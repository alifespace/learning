from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# 模拟数据库
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

class User(Resource):
    def get(self, user_id):
        if user_id in users:
            return users[user_id], 200
        return {"message": "User not found"}, 404

    def put(self, user_id):
        data = request.get_json()
        users[user_id] = data
        return data, 201

    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return {"message": "User deleted"}, 200
        return {"message": "User not found"}, 404

class UserList(Resource):
    def get(self):
        return users

    def post(self):
        data = request.get_json()
        user_id = max(users.keys()) + 1 if users else 1
        users[user_id] = data
        return {"id": user_id, **data}, 201

# 路由配置
api.add_resource(UserList, '/users')          # GET, POST
api.add_resource(User, '/users/<int:user_id>')  # GET, PUT, DELETE

if __name__ == '__main__':
    app.run(debug=True)
