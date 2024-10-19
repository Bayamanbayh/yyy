from django.contrib import admin
from .models import *


class MovieMomentInline(admin.TabularInline):
    model = MovieMoments
    extra = 1


class MovieLanguagesInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1


class MovieInline(admin.ModelAdmin):
    inlines = [MovieMomentInline, MovieLanguagesInline]


admin.site.register(Movie, MovieInline)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(FavoriteMovie)
admin.site.register(History)
