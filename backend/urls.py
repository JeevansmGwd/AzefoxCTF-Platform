from django.contrib import admin
from django.urls import path
from .views import (
    about_us_view,
    contact_us_view,
    index_view,
    challenge_view,
    search_results_view,
    sign_up_view,
    sign_in_view
)

urlpatterns = [  
    path("about/", about_us_view, name="about"),  # About Us page
    path("contact/", contact_us_view, name="contact"),  # Contact Us page
    path("challenges/", challenge_view, name="challenges"),  # Challenges page
    path("", index_view, name="home"),  # Home page now points to index_view
    path("admin/", admin.site.urls),
    path("search/", search_results_view, name="search_results"),  # Search page
    path("signup/", sign_up_view, name="signup"),  # Sign-up page
    path("signin/", sign_in_view, name="signin"),  # Sign-in page
    path("sign-in/", sign_in_view, name="sign-in"),  # Alternative sign-in page
]
