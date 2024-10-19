from django_filters import FilterSet
from .models import Movie

class ProductFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'year': ['gt', 'lt'],
            'country': ['exact'],
            'actor': ['exact'],
            'genre': ['exact'],
            'director': ['exact'],
            'status_movie': ['exact'],
            'types': ['exact']
        }