from django.contrib.auth.backends import ModelBackend
from rest_framework.authtoken.models import Token


class PhoneBackend(ModelBackend):
    def authenticate(self, hash_token):
        try:
            token = Token.objects.get(key=hash_token)
            return token.user
        except Token.DoesNotExist:
            return None
