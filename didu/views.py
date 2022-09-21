from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# generic 사용
# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer


class PublicPostListAPIView(APIView):
    def get(selfs, request):
        qs = Post.objects.filter(is_public=True)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


public_post_list = PublicPostListAPIView.as_view()

# 함수 기반 뷰로 구현
# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        # serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body :", request.body)
    #     print("request.POST :", request.POST) # 실제 product에선 logger 사용하기
    #     return super().dispatch(request, *args, **kwargs)


# def post_list(request):
#     # 2개 분기
#     pass


# def post_detail(request, pk):
#     # request.method # => 3개 분기
#     pass





