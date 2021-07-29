from flask import request
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

ns.models[login_model.name] = login_model


@ns.route("/login")
class Login(Resource):
    @ns.expect(login_model)
    @ns.response(code=201, description="Success")
    def post(self):
        """
        Logins user
        """
        return {"message": "logged"}, 200
