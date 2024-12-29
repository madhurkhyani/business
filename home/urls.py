from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("feature/<str:feature>", views.Features.as_view(), name='feature123_page'),
    path("previous-trans/<str:feature>", views.previous_transaction, name="previous_transaction"),
    path("soon", views.soon, name='soon'),
    path('delete-object/<str:slug>/<int:object_id>/', views.delete_object, name='delete_object')
]
