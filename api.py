from flask_restx import Resource, Api
from namespaces.users import ns as users_namespace
from namespaces.likes import ns as likes_namespace

api = Api(
    prefix="/v1",
    title="Meet Me API",
    description="Meet Me Web API",
    validate=True,
)

api.add_namespace(users_namespace)
api.add_namespace(likes_namespace)


@api.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred."
    return {"message": message}, 500
