from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html')


def rules(request):
    return render(request, 'pages/rules.html')


def err_403(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def err_404(request, exception):
    return render(request, 'pages/404.html', status=404)


def err_500(request):
    return render(request, 'pages/500.html', status=500)
