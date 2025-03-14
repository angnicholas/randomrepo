from django.urls import include, path
from .views import ProtectedView

urlpatterns = [
    path('', ProtectedView.as_view()),
]