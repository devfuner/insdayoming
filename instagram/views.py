from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from instagram.forms import Form, Article


# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-cdate')
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        print('PageNotAnInteger')
        articles = paginator.page(1)
    except EmptyPage:
        print('EmptyPage')
        articles = paginator.page(paginator.num_pages)

    return render(request, 'instagram/index.html', {'articles': articles})


def upload(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            new_form = Article(name=request.POST['name'],
                               photo=request.FILES['photo'],
                               contents=request.POST['contents'])
            new_form.save()
            return redirect('/instagram/')
    else:
        form = Form()

    return render(request, 'instagram/upload.html', {'form': form})
