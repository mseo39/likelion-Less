from django.urls import path, include
urlpatterns = [
    path('profile/<int:event_id>', main.views.event, name="event"),
]