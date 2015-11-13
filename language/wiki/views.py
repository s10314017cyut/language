from django.shortcuts import render , redirect
from django.core.urlresolvers import reverse
'''
from wiki.forms import CategoryForm
'''
from wiki.models import Category, Page
import datetime


def wiki(request):

    categories = Category.objects.order_by('-likes')
    context = {'categories':categories}
    return render(request,'wiki/wiki.html',context)


def about(request):
    return render(request,'wiki/about.html')


def category(request, categoryName):
    context = {}
    try:
        category = Category.objects.get(name=categoryName)
        context['category'] = Category
        context['pages'] = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        pass
    return render(request, 'wiki/category.html', context)

'''
def addCategory(request):
    template = 'wiki/addCategory.html'
    if request.method=='GET'
        return render(request, template, {'form':CategoryForm()})
    # request.method='POST
    form = CategoryForm(request.POST)
    if not form.is_vaild():
        return render(request, template, {'form':form})
    form.save()
    return redirect(reverse('wiki:wiki'))
    return wiki(request)
'''
