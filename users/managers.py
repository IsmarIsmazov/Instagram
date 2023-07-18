from django.contrib.auth.base_user import BaseUserManager



class CustomUseManager(BaseUserManager):
    '''Custom manager for the user model.'''


    def create_user(self, email, password, **extra_fields):
        '''The "create_user" method normalizes the email, creates a new user '''
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)



        if extra_fields.get("is_staff") is not True:
            raise ValueError("Администратор не имеет привелегий!")



        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Администратор не имеет разрешений!")

        return self.create_user(email=email, password=password, **extra_fields)
