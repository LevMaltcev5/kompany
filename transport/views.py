from django.shortcuts import render
from .models import *
# Create your views here.
def transport(request):
    transport_images = TransImage.objects.filter(is_main=True, transport__is_active=True)
    return render(request, 'landings/Transport.html', locals())

def evertrans(request, transport_id):
    transport = Trans.objects.get(id=transport_id)

    return render(request, 'products/product.html', locals())
