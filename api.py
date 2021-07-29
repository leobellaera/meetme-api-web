from flask_restx import Resource, Api

api = Api(
    prefix="/v1",
    title="Meet Me API",
    description="Meet Me Web API",
    validate=True,
)


@api.route('')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
