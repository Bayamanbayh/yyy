from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'password', 'first_name', 'last_name',
                  'age', 'date_registered', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = '__all__'

class MovieMomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieMoments
        fields = '__all__'

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'movie_time', 'average_rating', 'year']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class MovieDetailSerializers(serializers.ModelSerializer):
    genre = GenreSerializers()
    ratings = RatingSerializers(many=True, read_only=True)
    movie_language = MovieLanguagesSerializers(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    year = serializers.DateField(format='%d-%m-%Y')
    owner = ProfileSerializers()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        return obj.get_average_rating()

class FavoriteMovieSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), write_only=True, source='product')

    class Meta:
        model = FavoriteMovie
        fields = ['id', 'movie', 'movie_id', 'quantity', 'get_total_price']

class FavoriteSerializers(serializers.ModelSerializer):
    items = FavoriteMovieSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'items', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()

class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

