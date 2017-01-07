from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

class UserMiddleware(object):
    def process_request(self, request):
        #print("Hello")
        TOKEN_NAME = "token"
        token = request.GET.get(TOKEN_NAME)
        if token is not None:
            user = authenticate(hash_token=token)
            #print(user)
            if user is not None:
                login(request, user)
                return redirect("./")
                #print("user : "+ request.user.username)
            else:
                print('No such user')

    def process_response(self, request, response):
        return response
