from django.shortcuts import render


def home(request):
    return render(request, 'store/home.html')


def shop(request):
    return render(request, 'store/shop.html')


def faqs(request):
    return render(request, 'store/faqs.html')


def about(request):
    return render(request, 'store/about.html')


def contact(request):
    return render(request, 'store/contact.html')