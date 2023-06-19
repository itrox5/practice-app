from django.urls import path
from . import views

urlpatterns = [
    # If URL second parameter request is 'janurary' Access index function in views file
    path("january", views.january),
    path("february", views.february),
     #<month> is a dynamically entered parameter, its value is checked in the 'monthly_challenge' functions switch statement 
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]
