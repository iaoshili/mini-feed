# services/users/project/api/users/views.py


from flask import request
from flask_restx import Namespace, Resource, fields
from project.api.users.crud import (add_user, delete_user, get_all_users,
                                    get_user_by_email, get_user_by_id,
                                    update_user, get_time_line)

users_namespace = Namespace("users")

user = users_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)

timeline_namespace = Namespace("timelines")

timeline = timeline_namespace.model(
    "Tweet",
    {
        "id": fields.Integer(readOnly=True),
        "content": fields.String(required=True),
        "created_date": fields.DateTime,
    }
)


class UsersList(Resource):
    @users_namespace.marshal_with(user, as_list=True)
    def get(self):
        """Returns all users."""
        return get_all_users(), 200

    @users_namespace.expect(user, validate=True)
    @users_namespace.response(201, "<user_email> was added!")
    @users_namespace.response(400, "Sorry. That email already exists.")
    def post(self):
        """Creates a new user."""
        post_data = request.get_json()
        username = post_data.get("username")
        email = post_data.get("email")
        response_object = {}

        user = get_user_by_email(email)
        if user:
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400
        add_user(username, email)
        response_object["message"] = f"{email} was added!"
        return response_object, 201


class Users(Resource):
    @users_namespace.marshal_with(user)
    @users_namespace.response(200, "Success")
    @users_namespace.response(404, "User <user_id> does not exist")
    def get(self, user_id):
        """Returns a single user."""
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")
        return user, 200

    @users_namespace.expect(user, validate=True)
    @users_namespace.response(200, "<user_is> was updated!")
    @users_namespace.response(404, "User <user_id> does not exist")
    def put(self, user_id):
        """Updates a user."""
        post_data = request.get_json()
        username = post_data.get("username")
        email = post_data.get("email")
        response_object = {}

        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")
        update_user(user, username, email)
        response_object["message"] = f"{user.id} was updated!"
        return response_object, 200

    @users_namespace.response(200, "<user_is> was removed!")
    @users_namespace.response(404, "User <user_id> does not exist")
    def delete(self, user_id):
        """Updates a user."""
        response_object = {}
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")
        delete_user(user)
        response_object["message"] = f"{user.email} was removed!"
        return response_object, 200


class TimeLines(Resource):
    @timeline_namespace.marshal_with(timeline, as_list=True)
    @timeline_namespace.response(200, "Success")
    @timeline_namespace.response(404, "User <user_id> does not exist")
    def get(self, user_id):
        """Returns the timeline for a user."""
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")
        return get_time_line(user_id), 200


users_namespace.add_resource(UsersList, "")
users_namespace.add_resource(Users, "/<int:user_id>")
timeline_namespace.add_resource(TimeLines, "/<int:user_id>")
