from . import views
from django.urls import path


urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
#    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'), #Slug converter!
#    path('<slug:slug>/', views.GameReviews.as_view(), name='reviews'), # TO BE EDITED!
    #path('reviews/<slug:slug>/', views.ReviewDetail.as_view(), name='reviews'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='game_detail'),
]                              
