from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def homepage(request):
    context = {}
    context["name"] = "Arstan"
    posts_list = Post.objects.all()
    context["posts"] = posts_list
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
def shorts_list(request):
    shorts = Shorts.objects.all()
    context = {'shorts': shorts}
    return render(request, 'shorts_list.html', context)

def shorts_detail(request, id):
    shorts = Shorts.objects.get(id=id)
    context = {'shorts': shorts}
    return render(request, 'shorts_detail.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', context)

def category_detail(request, id):
    category = Category.objects.get(id=id)
    context = {'category': category}
    return render(request, 'category_detail.html', context)


def contacts(request):
    return HttpResponse("Наши контакты!")

def about_us(request):
    return HttpResponse("Информация о нас!")



