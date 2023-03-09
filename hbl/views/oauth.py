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


class AuthView(APIView):
    def get(self, request):
        code = request.query_params["code"]
        token = yahoo_oauth.fetch_token(
            AUTHLIB_OAUTH_CLIENTS["yahoo"]["authorize_url"],
            authorization_response=AUTHLIB_OAUTH_CLIENTS["yahoo"]["redirect_uri"],
            code=code,
            client_secret=AUTHLIB_OAUTH_CLIENTS["yahoo"]["client_secret"],
        )
        request.session["token"] = token["access_token"]
        request.session["refresh_token"] = token["refresh_token"]

        return HttpResponse(
            f"""
                <body>
                    <script>
                        window.close();
                    </script>
                </body>
            """,
            status=200,
        )
