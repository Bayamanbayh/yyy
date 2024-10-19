from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser

STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simple', 'simple')
)

class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], null=True, blank=True)
    date_registered = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )

    status_profile = models.CharField(max_length=12, choices=STATUS_CHOICES, null=True, blank=True)

class Country(models.Model):
    country_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.country_name

class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio = models.TextField
    age = models.PositiveSmallIntegerField()
    director_image = models.ImageField(upload_to='director_images/', null=True, blank=True)

    def __str__(self):
        return self.director_name

class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField
    age = models.PositiveSmallIntegerField()
    actor_image = models.ImageField(upload_to='director_images/', null=True, blank=True)

    def __str__(self):
        return self.actor_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=32)
    year = models.DateField()
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    TYPE_CHOICES = (
        ('144p', '144p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    )
    types = MultiSelectField(max_length=16, choices=TYPE_CHOICES, max_choices=5)
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movie_trailer/')
    movie_image = models.ImageField(upload_to='movie_images/')
    status_movie = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return self.movie_name

class MovieLanguages(models.Model):
    language = models.CharField(max_length=16)
    video = models.FileField(upload_to='movie_languages/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_language')

    def __str__(self):
        return f'{self.language} - {self.movie}'

class MovieMoments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='movie_moments/')

class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], verbose_name='рейтинг')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

class Favorite(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

