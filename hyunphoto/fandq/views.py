from django.shortcuts import render
from .models import Fandq

def fandq(request):
    fandq = Fandq.objects.all()
    context = {
        'fandq': fandq
    }

    return render(request, 'fandq.html', context)

