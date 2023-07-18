from rest_framework import serializers
from .models import User
from phonenumber_field.modelfields import PhoneNumberField





class RegisUserSerializer(serializers.ModelSerializer):
    '''Serializer for creating new user instances.'''
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(min_length=4, write_only=True)
    phone = serializers.CharField(min_length=5)


    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone']

    def validate(self, attrs):
        '''The "validate" method checks if the provided email already exists in the
database, and raises a "ValueError" if it does.'''
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValueError('Такая почта уже используется!')
        return super().validate(attrs)

    def create(self, validated_data):
        ''' "create" method
creates a new user instance using the provided data, and sets the user's
password using the `set_password` method.'''
        password = validated_data.pop('password')
        user = super().create(validated_data)


        user.set_password(password)

        user.save()
        return user



class ProfileSerializer(serializers.ModelSerializer):
    '''Serializer for user profiles.'''
    email = serializers.EmailField(min_length=5,
                                   max_length=40,
                                   )
    username = serializers.CharField(min_length=1,
                                     max_length=10
                                     )
    phone = PhoneNumberField()



    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "phone",
                  ]


