from flask import request
from models import db, User
from namespaces.exceptions import UserDoesNotExist, EmailAlreadyRegistered, PasswordDoesNotMatch
from flask_restx import Namespace, Resource, Model, fields

ns = Namespace(
    name="Users",
    path="/meetme/users",
    description="Operations related to Meet Me users",
)


@ns.errorhandler(UserDoesNotExist)
def handle_user_does_not_exist(_error: UserDoesNotExist):
    return {"message": "User does not exist"}, 404


@ns.errorhandler(PasswordDoesNotMatch)
def handle_wrong_password(_error: PasswordDoesNotMatch):
    return {"message": "Password does not match the user email"}, 401


@ns.errorhandler(EmailAlreadyRegistered)
def handle_email_already_registered(_error: EmailAlreadyRegistered):
    return {"message": "Email already registered"}, 409


login_model = Model(
    "User login model",
    {
        "email": fields.String(required=True, description="Account email"),
        "password": fields.String(required=True, description="Account password"),
    },
)


register_model = Model(
    "User register model",
    {
        "email": fields.String(required=True, description="User email"),
        "password": fields.String(required=True, description="User password"),
        "first_name": fields.String(required=True, description="User first name"),
        "last_name": fields.String(required=True, description="User last name"),
        "gender": fields.String(required=True, description="User gender"),
        "gender_interests": fields.String(required=True, description="User gender interests"),
        "age": fields.Integer(required=True, description="User age"),
        "interests": fields.String(required=True, description="User interests"),
    },
)

register_success_model = Model(
    "User success model",
    {
        "id": fields.Integer(description="User account id")
    },
)

ns.models[login_model.name] = login_model
ns.models[register_model.name] = register_model
ns.models[register_success_model.name] = register_success_model


@ns.route("/login")
class Login(Resource):
    @ns.expect(login_model)
    @ns.response(code=201, description="Success")
    @ns.response(code=401, description="Wrong password")
    @ns.response(code=404, description="User not found")
    def post(self):
        """
        Logins user
        """
        user = User.query.filter(User.email == ns.payload['email']).first()
        if user is None:
            raise UserDoesNotExist
        elif user.password != ns.payload['password']:
            raise PasswordDoesNotMatch
        return {"message": "logged"}, 200


@ns.route('')
class Register(Resource):
    @ns.expect(register_model)
    @ns.response(code=201, description="Success", model=register_success_model)
    @ns.response(code=409, description="Email already registered")
    def post(self):
        """
        Registers user
        """
        user = User.query.filter(User.email == ns.payload['email']).first()
        if user:
            raise EmailAlreadyRegistered
        new_user = User(**ns.payload)
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id}, 201
