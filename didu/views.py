from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body :", request.body)
    #     print("request.POST :", request.POST) # 실제 product에선 logger 사용하기
    #     return super().dispatch(request, *args, **kwargs)

def post_list(request):
    # 2개 분기
    pass


def post_detail(request, pk):
    # request.method # => 3개 분기
    pass