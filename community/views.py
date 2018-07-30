from django.shortcuts import render
from community.forms import Form, Article


# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'community/write.html', {'form': form})


def list(request):
    article_list = Article.objects.all()
    return render(request, 'community/list.html', {'article_list': article_list})


def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'community/view.html', {'article': article})
