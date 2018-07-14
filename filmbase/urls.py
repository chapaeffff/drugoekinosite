from django.urls import include, path


from . import views

app_name = 'filmbase'

urlpatterns = [
    path('<int:pk>/', views.film_detail, name='film_detail'),

]
