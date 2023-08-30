from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('list', views.ArticleListView.as_view(), name='article_list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search_articles'),
    path('contactus/', views.MessageView.as_view(), name='contactus'),
    path('redirect/<slug:slug>', views.HomePageRedirect.as_view(), name='redirect'),
    path('message', views.MessagesListView.as_view(), name='message_list'),
    path('message/edit/<int:pk>', views.MessageUpdateView.as_view(), name='message_edit'),
    path('message/delete/<int:pk>', views.MessageDeleteView.as_view(), name='message_delete'),
    path('archive', views.ArchiveIndexArticleView.as_view(), name='archive'),
    path('archive/<int:year>', views.YearArchiveArticleView.as_view(), name='archive_year'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),
]