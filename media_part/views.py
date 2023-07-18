from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import APIView
from media_part.models import Post
from media_part.serializers import PostSeializer
from media_part.serializers import LikesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from users.permissions import IsOwnerPermission, IsOwnerPermissionClass







class PostViewSet(viewsets.ModelViewSet):
    '''API endpoint for viewing and modifying posts.'''
    queryset = Post.objects.all()
    serializer_class = PostSeializer
    permission_classes = [IsOwnerPermission,
                          ]
    filter_backends = [DjangoFilterBackend,
                       SearchFilter
                       ]
    authentication_classes = [JWTAuthentication,
                              ]
    search_fields = ['author__username']
    filter_fields = ['']




    def perform_create(self, serializer):
        serializer.save(author=self.request.user)





class EditPostView(viewsets.ModelViewSet):
    '''API endpoint for updating and deleting posts.'''
    queryset = Post.objects.all()
    serializer_class = PostSeializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsOwnerPermissionClass,]




class AddPostView(generics.GenericAPIView):
    '''API endpoint for creating new posts.'''
    queryset = Post.objects.all()
    serializer_class = PostSeializer
    permission_classes = [IsOwnerPermission,]
    authentication_classes = [JWTAuthentication,
                              ]



    def post(self, request):
        '''This API endpoint provides the "post" method for creating a new post
using the provided post data.'''
        if request.user.is_authenticated:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)
                return Response(
                    data={"ok"},
                    status=status.HTTP_200_OK,
                )
            return Response(data=serializer.errors())
        return Response("")





class LikesView(generics.ListAPIView):
    '''API endpoint for viewing likes on posts.'''
    serializer_class = LikesSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwnerPermission,]
    authentication_classes = [JWTAuthentication,]





class AddLikeView(APIView):
    '''API endpoint for creating likes on posts.'''
    serializer_class = LikesSerializer
    permission_classes = [IsOwnerPermission,]
    authentication_classes = [JWTAuthentication,]





    def post(self, request, pk):
        '''This API endpoint provides a "post" method for creating a like on a post
        using a POST request.'''
        post = Post.objects.get(pk=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post,
                            username=self.request.user,
                            )
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED,
                            )
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )


