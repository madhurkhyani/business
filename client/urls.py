from django.urls import path
from . import views
urlpatterns = [
    path("", views.ClientPage.as_view(), name="client-page"),
    path("addclient", views.addClient.as_view(), name="add-client")
]
