from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def homepage(request):
    context = {}
    context["name"] = "Arstan"
    posts_list = Post.objects.all()
    context["posts"] = posts_list
    shorts_list = Shorts.objects.all()
    context["shorts"] = shorts_list
    category_list = Category.objects.all()
    context["categories"] = category_list
    return render(request, "home.html", context)

def post_detail(request, id):
    context = {}
    post_object = Post.objects.get(id=id)
    context["post"] = post_object
    return render(request, "post_info.html", context)

def profile_detail(request, id):
    context = {}
    context['profile'] = Profile.objects.get(id=id)
    return render(request, 'profile_detail.html', context)

def shorts_detail(request, id):
    context = {}
    shorts_object = Shorts.objects.get(id=id)
    context['short'] = shorts_object
    return render(request, 'shorts_list.html', context)

def category_detail(request, id):
    context = {}
    category_object = Category.objects.get(id=id)
    context['category'] = category_object
    return render(request, 'category_detail.html', context)

def contacts(request):
    return HttpResponse("Наши контакты!")

def about_us(request):
    return HttpResponse("Информация о нас!")



