from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('users/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_detail'),

    path('category/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),

    path('photos/', MovieLanguageViewSet.as_view({'get': 'list', 'post': 'create'}), name='photos_list'),
    path('photos/<int:pk>/', MovieLanguageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='photos_detail'),

    path('cart/', FavoriteViewSet.as_view({'get': 'retrieve'}), name='cart_detail'),
    path('cart_items/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_item_list'),
    path('cart_items/<int:pk>/', FavoriteMovieViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]