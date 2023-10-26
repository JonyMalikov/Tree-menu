from django.shortcuts import render


def index(request, id=None):
    context = {
        'id': id,
    }
    return render(request, 'trees/index.html', context)
