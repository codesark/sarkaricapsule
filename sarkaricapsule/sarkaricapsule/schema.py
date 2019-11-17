import graphene

import events.schema

class Query(events.schema.Query, 
            graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)