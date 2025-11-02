from app.extensions import ma
from app.models import Movie, User, UserTag

class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        load_instance = True

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserTagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserTag
        load_instance = True
        include_fk = True

usertag_schema = UserTagSchema()
usertags_schema = UserTagSchema(many=True)


