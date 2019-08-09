from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "djUI/index.html", context={
        "insert_me": "Insert me variable value."
    })
