from django.shortcuts import render

# Create your views here.

def home(request):

    """This method will be used take users to the home page

    :returns: The home.html doc within the /pages/templates/ folder
    """

    return render(request, "home.html")

def media(request):

    """This method will be used take users to the media page

    :returns: The media.html doc within the /pages/templates/ folder
    """

    return render(request, "media.html")
