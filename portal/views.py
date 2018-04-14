# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .forms import NameForm, PointForm
from .models import Item, ItemForm, Point

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        items = Point.objects.all().filter(owner=request.user)
        context = {
            "title": "Home",
            "active": "home",
            "items": items
        }
        return render(request, 'pages/home.html', context)
    else:
        return redirect('/accounts/login/')

@login_required
def add_new(request):
    if request.method == 'POST':
        form = PointForm(request.POST)
        if form.is_valid():
            Point.objects.create(
                street=form.cleaned_data['street'],
                city=form.cleaned_data['city'],
                lat=form.cleaned_data['lat'],
                lng=form.cleaned_data['lng'],
                owner=request.user
            )
        return redirect('home')
    else:
        form = PointForm()
        context = {
            "title": "Add new",
            "form": form,
            "active": "add_new",
            "mode": "new",
        }
        return render(request, 'pages/point.html', context)


@login_required
def edit_point(request, id):
    if request.method == 'POST':
        form = PointForm(request.POST)
        if form.is_valid() and request.user.point_set.filter(pk=id).exists():
            item = Point.objects.get(pk=id)
            item.street=form.cleaned_data['street']
            item.city=form.cleaned_data['city']
            item.lat=form.cleaned_data['lat']
            item.lng=form.cleaned_data['lng']
            item.save()
        return redirect('home')
    else:
        item = Point.objects.get(id=id)
        form = PointForm({'street':item.street, 'city':item.city, 'lat':item.lat, 'lng':item.lng})
        context = {
            "form": form,
            "item": item,
            "title": "Edit Point",
            "mode": "edit",
        }
        return render(request, 'pages/point.html', context)


@login_required
def show_all(request):
    items = Point.objects.all().filter(owner=request.user)
    context = {
        "title": "Show all",
        "active": "show_all",
        "items": items
    }
    return render(request, 'pages/show_all.html', context)