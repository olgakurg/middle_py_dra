from ... import models
from rest_framework import serializers



class StringListSerializer(serializers.ListSerializer):
    child = serializers.CharField()


class FilmworkSerializer(serializers.ModelSerializer):
    creation_date = serializers.CharField(source="created")
    genres = serializers.StringRelatedField(many=True)
    actors = StringListSerializer()
    directors = StringListSerializer()
    writers = StringListSerializer()

    class Meta:
        model = models.Filmwork
        fields = (
            "id",
            "title",
            "description",
            "creation_date",
            "type",
            "rating",
            "genres",
            "actors",
            "directors",
            "writers",
        )
        depth = 3
