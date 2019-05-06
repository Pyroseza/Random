from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def basic(request):
    from User.torn_api import lookup_user
    title = "this is a basic profile page"
    return render(request, "basic.html", {"title": title, "user_data": lookup_user()})
