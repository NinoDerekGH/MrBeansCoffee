from django.shortcuts import render


def home_out(request):
    return render(request, 'store/user_out/home_out.html')


def shop_out(request):
    return render(request, 'store/user_out/shop_out.html')


def faqs_out(request):
    return render(request, 'store/user_out/faqs_out.html')


def about_out(request):
    return render(request, 'store/user_out/about_out.html')


def contact_out(request):
    return render(request, 'store/user_out/contact_out.html')


def home_in(request):
    return render(request, 'store/user_in/home_in.html')


def shop_in(request):
    return render(request, 'store/user_in/shop_in.html')


def faqs_in(request):
    return render(request, 'store/user_in/faqs_in.html')


def about_in(request):
    return render(request, 'store/user_in/about_in.html')


def contact_in(request):
    return render(request, 'store/user_in/contact_in.html')


def cart_in(request):
    return render(request, 'store/user_in/cart_in.html')

