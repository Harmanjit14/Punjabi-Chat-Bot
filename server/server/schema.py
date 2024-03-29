import graphene
import graphql_jwt
import db.schema as db

class Query(db.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)