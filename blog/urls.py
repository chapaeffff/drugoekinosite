from django.urls import include, path


from . import views

urlpatterns = [
    path('lists/', views.lists, name='lists'),
    path('lists/<slug:slug>/', views.list, name='list'),

#    path('lists/(?P<slug>[-\w]+)/$', views.list, name='list'),

]
