from django.urls import re_path

from hbl.views.oauth import AuthView, OauthView

urlpatterns = [
    re_path(r'^login/?$', OauthView.as_view()),
    re_path(r'^auth/?$', AuthView.as_view())
]