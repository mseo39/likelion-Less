from django.urls import path, include
import main.views
urlpatterns = [
    path('', main.views.main, name="main"),
    path('event', main.views.event, name="event"),
    path('eventdetail/<int:event_id>', main.views.eventdetail, name="eventdetail"),
    path('payment', main.views.payment, name="payment"),
    path('goods', main.views.goods, name="goods"),
]