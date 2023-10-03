from rest_framework.generics import ListAPIView, RetrieveAPIView
from . import serializers
from ...models import Filmwork
from django.db.models import Q
from django.contrib.postgres.aggregates import ArrayAgg
from ...pagination import CustomPagination

class MoviesAPIMixin:

    serializer_class = serializers.FilmworkSerializer

    def get_person_aggregation(self, role):
        return ArrayAgg("personfilmwork__person__full_name",
                    filter=Q(personfilmwork__role=str(role)))

    def get_queryset(self):
        queryset = Filmwork.objects.all()
        films = (
            queryset.prefetch_related("persons")
            .annotate(
                actors=self.get_person_aggregation("actor")
                )
            .annotate(
                directors=self.get_person_aggregation("director"),
                )
            .annotate(
                writers=self.get_person_aggregation("writer"),
                )
            .select_related()
        )
        return films


class MoviesListAPIView(MoviesAPIMixin, ListAPIView):
    pagination_class = CustomPagination


class MoviesDetailApi(MoviesAPIMixin, RetrieveAPIView):
    pass
