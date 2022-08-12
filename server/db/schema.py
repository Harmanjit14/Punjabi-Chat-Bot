import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from .models import *
from graphql import GraphQLError

class UserType(DjangoObjectType):
    class Meta:
        model = UserProfile

class Query(graphene.ObjectType):

    me = graphene.Field(UserType)


    def resolve_me(self,info):
        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        profile = UserProfile.objects.get(user=usr)
        if profile==None:
            raise GraphQLError('Profile does not exist')

        return profile