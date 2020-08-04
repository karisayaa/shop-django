from django.shortcuts import render
from .models import Product


def index(request):
    product1 = Product()
    product1.name = 'Slim Shirt'
    product1.brand = 'Rebook'
    product1.price = 5000
    product1.rating = 4.6
    product1.img = 'd1.png'

    product2 = Product()
    product2.name = 'Slim Trouser'
    product2.brand = 'Nike'
    product2.price = 6000
    product2.rating = 4.0
    product2.img = 'd5.jpg'

    product3 = Product()
    product3.name = 'Big Slim Shirt'
    product3.brand = ' Nike - Rebook'
    product3.price = 9000
    product3.rating = 3.6
    product3.img = 'd7.jpg'

    product4 = Product()
    product4.name = 'Big Slim Shirt'
    product4.brand = ' Nike '
    product4.price = 9000
    product4.rating = 3.6
    product4.img = 'd6.jpg'

    product = [product1, product2, product3, product4]

    return render(request, 'index.html', {'product': product})
