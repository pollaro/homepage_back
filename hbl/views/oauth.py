import json

import requests
from django.http import HttpResponse
from requests_oauthlib import OAuth2Session
from rest_framework.views import APIView

from homepage_back.settings import AUTHLIB_OAUTH_CLIENTS

yahoo_oauth = OAuth2Session(
    AUTHLIB_OAUTH_CLIENTS["yahoo"]["client_id"],
    redirect_uri=AUTHLIB_OAUTH_CLIENTS["yahoo"]["redirect_uri"],
)


class OauthView(APIView):
    def post(self, request):
        auth_url, state = yahoo_oauth.authorization_url(
            AUTHLIB_OAUTH_CLIENTS["yahoo"]["access_token_url"],
        )
        return HttpResponse(auth_url)

    def get(self, request):
        if 'access_token' in request.body:
            return HttpResponse(
                    json.dumps({'token': request.query_params['access_token'], 'refresh_token': request.query_params['refresh_token']}), status=200
                )


class AuthView(APIView):
    def get(self, request):
        code = request.query_params["code"]
        token = yahoo_oauth.fetch_token(
            AUTHLIB_OAUTH_CLIENTS["yahoo"]["authorize_url"],
            authorization_response=AUTHLIB_OAUTH_CLIENTS['yahoo']['redirect_uri'],
            code=code,
            client_secret=AUTHLIB_OAUTH_CLIENTS["yahoo"]["client_secret"],
        )
        request.session['token'] = token
        requests.get('https://127.0.0.1:8000/hbl/login', params={'token': token['access_token'], 'refresh_token': token['refresh_token']})
        return HttpResponse(status=200)