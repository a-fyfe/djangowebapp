from django.urls import path, include
from . import views

app_name = 'vote'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('user_auth/', include("django.contrib.auth.urls")),
    path('user_auth/', include("user_auth.urls")),
    
]