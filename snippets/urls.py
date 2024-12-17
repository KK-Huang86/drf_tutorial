from snippets import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include



urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    path('user',views.UserList.as_view()),
    path('^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
