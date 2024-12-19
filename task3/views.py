from django.shortcuts import render


def index_view(request):
    return render(request, 'third_task/index.html')


def shop_view(request):
    items = {'items': ['Товар 1', 'Товар 2', 'Товар 3']}
    return render(request, 'third_task/shop.html', items)


def cart_view(request):
    return render(request, 'third_task/cart.html')

