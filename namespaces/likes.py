from models import db, Like
from flask_restx import Namespace, Resource, Model, fields, reqparse

ns = Namespace(
    name="Likes",
    path="/meetme/likes",
    description="Operations related to Meet Me likes",
)

likes_request_model = Model(
    "Likes request model",
    {
        "user_1": fields.Integer(required=True, description="Id of the user who liked"),
        "user_2": fields.Integer(required=True, description="Id of the user who was liked")
    },
)

likes_response_model = Model(
    "Likes response model",
    {
        "match": fields.Boolean(required=True, description="If a match happened between the users"),
    },
)


ns.models[likes_request_model.name] = likes_request_model
ns.models[likes_response_model.name] = likes_response_model

parser = reqparse.RequestParser()
parser.add_argument('user_1', type=int, location='form')
parser.add_argument('user_2', type=int, location='form')


@ns.route('')
class Likes(Resource):
    @ns.expect(likes_request_model)
    @ns.response(code=200, description='Like registered', model=likes_response_model)
    def post(self):
        """
        Likes
        """
        args = ns.payload
        args["user_1_liked"] = True
        args["user_2_liked"] = False
        id_1 = args["user_1"]
        id_2 = args["user_2"]

        like = Like.query.filter((Like.user_1 == id_1) & (Like.user_2 == id_2)).first()
        if like is None:
            like = Like.query.filter((Like.user_2 == id_1) & (Like.user_1 == id_2)).first()
            if like is None:
                new_like = Like(**args)
                db.session.add(new_like)
                db.session.commit()
                return {"match": False}, 200
            like.user_2_liked = True
            db.session.add(like)
            db.session.commit()
            return {"match": True}, 200

        return {"match": like.user_1_liked & like.user_2_liked}, 200
