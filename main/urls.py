from django.urls import path, include
import main.views
urlpatterns = [
    path('', main.views.home, name="main"),
    path('profile/<int:event_id>', main.views.event, name="event"),
]