from django.shortcuts import render


def photoshoots_frontpage_view(request):
    return render(request, 'photoshoots_frontpage_view.jade')
