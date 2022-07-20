from django.shortcuts import render


def home(request):
    return render(request, 'store/non_user/home.html')


def shop(request):
    return render(request, 'store/non_user/shop.html')


def faqs(request):
    return render(request, 'store/non_user/faqs.html')


def about(request):
    return render(request, 'store/non_user/about.html')


def contact(request):
    return render(request, 'store/non_user/contact.html')


def cart(request):
    return render(request, 'store/user_interface/cart.html')

