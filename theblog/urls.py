from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, AddCommentView


urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]
