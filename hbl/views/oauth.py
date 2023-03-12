import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from requests_oauthlib import OAuth2Session
from rest_framework.views import APIView

from hbl.models.hbluser import HblUser
from homepage_back.settings import AUTHLIB_OAUTH_CLIENTS

yahoo_oauth = OAuth2Session(
    AUTHLIB_OAUTH_CLIENTS["yahoo"]["client_id"],
    redirect_uri=AUTHLIB_OAUTH_CLIENTS["yahoo"]["redirect_uri"],
)


class OauthView(APIView):
    email = None

    def post(self, request):
        global email
        email = request.POST.get("email")
        if email:
            try:
                HblUser.objects.get(email=email)
            except ObjectDoesNotExist:
                HblUser.objects.create(email=email)
        auth_url, state = yahoo_oauth.authorization_url(
            AUTHLIB_OAUTH_CLIENTS["yahoo"]["access_token_url"],
            email=request.POST.get("email"),
        )
        return HttpResponse(auth_url)

    def get(self, request):
        global email
        code = request.query_params["code"]
        token = yahoo_oauth.fetch_token(
            AUTHLIB_OAUTH_CLIENTS["yahoo"]["authorize_url"],
            authorization_response=AUTHLIB_OAUTH_CLIENTS["yahoo"]["redirect_uri"],
            code=code,
            client_secret=AUTHLIB_OAUTH_CLIENTS["yahoo"]["client_secret"],
        )
        if email:
            user = HblUser.objects.get(email=email)
            user.token = token["access_token"]
            user.refresh_token = token["refresh_token"]
            user.save()

        response = HttpResponse(
            f"""
                <body>
                    <script>
                        window.close();
                    </script>
                </body>
            """,
            status=200,
        )
        response.set_cookie(
            "hbl_token",
            token["access_token"],
            max_age=datetime.timedelta(seconds=3600),
            httponly=True,
            samesite="lax",
            domain=".yahoo.com",
        )
        return response
