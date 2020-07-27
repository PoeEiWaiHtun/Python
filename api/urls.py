from django.contrib import admin
from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, \
    GenericAPIView, ArticelViewSets, SnippetDetail, SnippetList, connectDatabase, GetUserData, Json
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register('modelViewSets', ArticelViewSets, base_name='article')


urlpatterns = [
    path('article_list/', article_list, name='article_list'),
    path('article_detail/<int:pk>/', article_detail, name='article_detail'),
    path('apiview_list/', ArticleAPIView.as_view(), name='ArticleAPIView'),
    path('apiview_detail/<int:id>/', ArticleDetails.as_view(), name='ArticleDetails'),
    path('generic_view/', GenericAPIView.as_view()),
    path('generic_view_detail/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    #path('viewset/<int:pk>/', include(router.urls)),
    path('generic_view/snippetdetail/<int:id>/', SnippetDetail.as_view()),
    path('generic_view/snippetlist/', SnippetList.as_view()),
    path('database/', connectDatabase),
    path('UserData/', GetUserData.as_view()),
    path('json/', Json)

    ]
#urlpatterns = format_suffix_patterns(urlpatterns)