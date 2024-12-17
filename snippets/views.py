from django.core.serializers import serialize
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    """
    列出所有的snippets或者創建一個新的snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    """
    檢索某一個snippet，或者更新、刪除
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)