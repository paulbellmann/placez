# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PointForm
from .models import Point


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        items = Point.objects.all().filter(owner=request.user).order_by('-date')
        context = {
            "title": "Home",
            "active": "home",
            "items": items
        }
        if not items:
            messages.add_message(request, messages.INFO,
                                 "Try adding new places with 'Add new'")
        return render(request, 'pages/home.html', context)
    else:
        return redirect('/accounts/login/')


@login_required
def add_new(request):
    if request.method == 'POST':
        form = PointForm(request.POST)
        if form.is_valid():
            Point.objects.create(
                title=form.cleaned_data['title'],
                street=form.cleaned_data['street'],
                city=form.cleaned_data['city'],
                lat=form.cleaned_data['lat'],
                lng=form.cleaned_data['lng'],
                visited=form.cleaned_data['visited'],
                owner=request.user
            )
            messages.add_message(request, messages.SUCCESS, "%s got saved." % form.cleaned_data['title'])
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
        item = Point.objects.get(pk=id)
        if form.is_valid() and item.owner == request.user:
            item.title = form.cleaned_data['title']
            item.street = form.cleaned_data['street']
            item.city = form.cleaned_data['city']
            item.lat = form.cleaned_data['lat']
            item.lng = form.cleaned_data['lng']
            item.visited = form.cleaned_data['visited']
            item.save()
            messages.add_message(request, messages.SUCCESS, "%s got edited." % form.cleaned_data['title'])
        return redirect('home')
    else:
        item = Point.objects.get(id=id)
        form = PointForm(initial={'title': item.title, 'street': item.street, 'city': item.city,
                                  'lat': item.lat, 'lng': item.lng, 'visited': int(item.visited)})
        context = {
            "form": form,
            "item": item,
            "title": "Edit Point",
            "mode": "edit",
        }
        if item.owner == request.user:
            return render(request, 'pages/point.html', context)
        else:
            return redirect('home')


@login_required
def show_all(request):
    items = Point.objects.all().filter(owner=request.user)
    context = {
        "title": "Show all",
        "active": "show_all",
        "items": items
    }
    return render(request, 'pages/show_all.html', context)


@login_required
def delete(request, id):
    point = Point.objects.get(pk=id)
    # if request.user.point_set.filter(pk=id).exists():
    if point.owner == request.user:
        point.delete()
        messages.add_message(request, messages.SUCCESS,
                             "%s got deleted." % point.title)
    return redirect('home')
