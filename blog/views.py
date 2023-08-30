from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category, Comment, Message, Like
from django.core.paginator import Paginator
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, ArchiveIndexView, YearArchiveView
from django.urls import reverse_lazy
from .mixins import LoginRequiredMixin


# Create your views here.
def article_detail(request, slug):
    parent_id = request.POST.get('parent_id')
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)

    context = {
        'article': article,
    }
    return render(request, 'blog/article_detail.html', context)


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    context = {
        'articles': articles,
    }
    return render(request, "blog/article_list.html", context)


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 4)
    object_list = paginator.get_page(page_number)
    context = {
        'articles': object_list,
    }
    return render(request, "blog/article_list.html", context)


class HomePageRedirect(RedirectView):
    # url = "/articles/list"
    pattern_name = "blog:article_detail"
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(self.request.user.username)
        return super().get_redirect_url(*args, **kwargs)


class UserList(ListView):
    queryset = User.objects.all()
    template_name = "blog/user_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.likes.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 4
    queryset = Article.objects.filter(published=True)


class MessageView(CreateView):
    model = Message
    fields = ("title", "text", "date", "age")
    success_url = reverse_lazy("home:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        print(self.object)
        return super(MessageView, self).get_success_url()


class MessagesListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'text', 'age')
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('blog:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('blog:message_list')


class ArchiveIndexArticleView(ArchiveIndexView):
    model = Article
    date_field = "updated"


class YearArchiveArticleView(YearArchiveView):
    model = Article
    date_field = "pub_date"
    make_object_list = True
    allow_future = True


def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
        return JsonResponse({"response": "unliked"})
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
        return JsonResponse({"response": "liked"})
