from django.urls import path
from .views import event_list_view, event_detail_view

urlpatterns = [
    path('list/', event_list_view, name='event_list'),
    path('<uuid:pk>/', event_detail_view, name='event_detail'),
    #path('new/', event_new_view, name='event_new')
]
