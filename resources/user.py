from flask_restful import Resource, reqparse
from modules.user import UserModel


class RegisterUser(Resource):

    user_parser = reqparse.RequestParser()
    user_parser.add_argument('username', type=str, required=True, help="Username can not be blank")
    user_parser.add_argument('password', type=str, required=True, help="Password can not be blank")

    def post(self):
        registration_details = RegisterUser.user_parser.parse_args()
        found_user = UserModel.find_by_username(registration_details['username'])
        if found_user is not None:
            return "User already exists", 409
        else:
            UserModel.add_user(registration_details['username'], registration_details['password'])
            return "Success", 200