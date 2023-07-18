from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import RegisUserSerializer
from users.serializers  import ProfileSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate
from users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication






class SignUp(generics.GenericAPIView):
    '''API endpoint for registering a new user.'''
    serializer_class = RegisUserSerializer

    def post(self, request):
        '''The `post` method is used to create a new user instance
using the provided user data.'''
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"Пользователь успешно зарегестрирован!",
                "data":serializer.data

            }

            return Response(data=response)
        return Response(data=serializer.errors)



class SignIn(APIView):
    '''API endpoint for signing in and checking the status of a user's session.'''

    def post(self, request:Request):
        ''' "post" for signing in a user using their email and password '''
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email,
                            password=password)

        if user is not None:
            refresh = RefreshToken().for_user(user)
            response = {
                "Сообщение": "Вы успешно вошли в систему!",
                "tokens": {"refresh": str(refresh),
                           "access": str(refresh.access_token)},
                "user": user.username
            }
            return Response(data=response)
        else:
            return Response(data={"Сообщение":"Вы не аторизованы! \nЗарегестрируйтесь!"})


    def get(self, request:Request):
        ''' "get" for checking the status of a user's session'''
        context = {
            "user":str(request.user),
            "auth":str(request.auth),
        }
        return Response(data=context)






class ProfileView(APIView):
    '''A view for displaying the user's profile information.'''
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]


    def get(self, request):
        '''Retrieve and return the user's profile information.'''
        user = request.user
        return Response({'username': user.username,
                         'email': user.email,
                         })






class EditProfile(generics.RetrieveUpdateDestroyAPIView):
    '''API endpoint for updating and deleting a user's profile.'''
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]














