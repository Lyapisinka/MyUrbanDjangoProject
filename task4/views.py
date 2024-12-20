from django.shortcuts import render

from django.shortcuts import render


def index_view(request):
    return render(request, 'fourth_task/index.html')


def shop_view(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077']}
    return render(request, 'fourth_task/shop.html', context)


def cart_view(request):
    return render(request, 'fourth_task/cart.html')



def my_view(request):

    return render(request, 'fourth_task/home.html')