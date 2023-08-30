from django.shortcuts import render
from blog.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all().order_by('-updated')[:3]
    context = {
        'articles': articles,
    }

    return render(request, 'home/home.html', context)


def sidebar(request):
    context = {
        'name': 'saeed',
    }
    return render(request, 'includes/sidebar.html', context)