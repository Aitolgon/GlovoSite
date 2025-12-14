from rest_framework import routers
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import (UserProfileListAPIView, UserProfileDetailAPIView,
                    CategoryListAPIView, CategoryDetailAPIView,
                    StoreListAPIView, StoreDetailAPIView,
                    OrderViewSet,
                    CourierProductViewSet, ReviewCreateAPIView, ReviewEditAPIView,
                    OrderStatusListView, OrderStatusDetailView, StoreViewSet,
                    RegisterView, LogoutView, LogoutView, CustomLoginView)


router = routers.SimpleRouter()
router.register('store_create', StoreViewSet)
router.register('order', OrderViewSet)
router.register('courier', CourierProductViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('stores/', StoreListAPIView.as_view(), name='store_list'),
    path('stores/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('reviews/create/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('reviews/create/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),
    path('orders_status/', OrderStatusListView.as_view(), name='order_list'),
    path('orders_status/<int:pk>/', OrderStatusDetailView.as_view(), name='order_detail'),\
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]