from django.shortcuts import render, HttpResponseRedirect
from .forms import RegMailClient, RegPhoneClient
# Create your views here.


def landing(request):
    return render(request, 'landings/main.html', locals())

def about(request):
    return render(request, 'landings/About.html', locals())

def regmail(request):
    form = RegMailClient(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()
        return HttpResponseRedirect('../thx')
    return render(request, 'landings/registermail.html', locals())

def regphone(request):
    form = RegPhoneClient(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()
        return HttpResponseRedirect('../thx')
    return render(request, 'landings/registerphone.html', locals())

def thx(request):
    return render(request, 'landings/thx.html', locals())

def zimniki(request):
    return render(request, 'zimniki.html', locals())

def perevozki(request):
    return render(request, 'perevori.html', locals())

def perevoz(request):
    return render(request, 'transportirovka.html', locals())
