from django.urls import path

from base.views import MenuPageView

urlpatterns = [
    path('', MenuPageView.as_view(), name='index')
]