from django.urls import re_path

from hbl.views.oauth import OauthView

urlpatterns = [
    re_path(r"^login/?$", OauthView.as_view()),
]
