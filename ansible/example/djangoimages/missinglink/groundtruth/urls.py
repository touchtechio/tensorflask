from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /image/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /image/5/vote/
    path('<int:image_id>/tag/', views.tag, name='tag'),
]