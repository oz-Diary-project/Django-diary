from django.urls import path, include

urlpatterns = [
    path("api/", include("your_app.urls")),
]