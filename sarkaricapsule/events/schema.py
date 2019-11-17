from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

# from django_filters import FilterSet, OrderingFilter
from .models import Event, EventType


class EventTypeNode(DjangoObjectType):
  class Meta:
    model = EventType
    filter_fields = ['name']
    interfaces = (relay.Node, )

class EventNode(DjangoObjectType):
  class Meta:
    model= Event
    # Filtering schema
    filter_fields = {
      'id': ['exact'],
      'title': ['exact', 'icontains', 'istartswith'],
      'event_type': ['exact'],
      'event_type__name': ['exact'],
    }
    interfaces = (relay.Node, )

class Query(ObjectType):
  event_type = relay.Node.Field(EventNode)
  all_event_types = DjangoFilterConnectionField(EventTypeNode)

  event = relay.Node.Field(EventNode)
  all_events = DjangoFilterConnectionField(EventNode) 

























# class EventTypeQL(DjangoObjectType):
#     class Meta:
#         model = EventType
#         fields = ("__all__")


# class EventFilter(FilterSet):
#   class Meta:
#     model = Event

#   order_by = OrderingFilter(
#     fields=(
#       ('created_at', 'modified_at'),
#     )
#   )

# class EventQL(DjangoObjectType):
#     class Meta:
#         model = Event
#         fields = "__all__"

#     # event_type = graphene.String()
#     # def resolve_event_type(self, info):
#     #   return


# class Query(object):
#     all_events = graphene.List(EventQL)

#     def resolve_all_events(self, info, **kwargs):
#         return Event.objects.all()
#     event = graphene.Field(EventQL, event_id=graphene.String())

#     def resolve_event(self, info, event_id):
#         Event.objects.get(pk=event_id)
