from django.shortcuts import render
from .models import Info


def home(request):

    context = {
        "info": Info.objects.all()
    }
    return render(request, "base/base.html", context)
