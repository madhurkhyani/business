from django.urls import path
from . import views
urlpatterns = [
    path("", views.ClientPage.as_view(), name="client-page"),
    path("addclient", views.addClient.as_view(), name="add-client"),
    path("client_detail/<int:client_id>/", views.client_detail, name="client_detail")
]