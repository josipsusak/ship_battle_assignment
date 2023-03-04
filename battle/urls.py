from battle.views import Battle
from django.urls import path

urlpatterns = [
    path("", Battle.as_view(), name="battle")
]
