from flask import request
from models import db, User
from flask_restx import Namespace, Resource, Model, fields

ns = Namespace(
    name="Users",
    path="/meetme/users",
    description="Operations related to Meet Me users",
)

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
        "first_name": fields.String(required=True, description="User first name"),
        "last_name": fields.String(required=True, description="User last name"),
        "gender": fields.String(required=True, description="User gender"),
        "gender_interests": fields.String(required=True, description="User gender interests"),
        "age": fields.Integer(required=True, description="User age"),
        "interests": fields.String(required=True, description="User interests"),
    },
)

ns.models[login_model.name] = login_model
ns.models[register_model.name] = register_model


@ns.route("/login")
class Login(Resource):
    @ns.expect(login_model)
    @ns.response(code=201, description="Success")
    def post(self):
        """
        Logins user
        """
        return {"message": "logged"}, 200


@ns.route('')
class Register(Resource):
    @ns.expect(register_model)
    def post(self):
        """
        Registers user
        """
        new_user = User(**ns.payload)
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id}, 201
