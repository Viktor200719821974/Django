from django.contrib.auth.base_user import BaseUserManager

from exeptions.jwt_exeption import JwtExeption


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        if not email:
            # raise ValueError("The email must be set")
            raise JwtExeption
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)
        
        if extra_kwargs.get('is_staff') is not True:
            # raise ValueError('Superuser must have is_staff=True')
            raise JwtExeption
        if extra_kwargs.get('is_superuser') is not True:
            # raise ValueError('Superuser must have is_superuser=True')
            raise JwtExeption
        user = self.create_user(email, password, **extra_kwargs)
        return user

    @staticmethod
    def to_superadmin(user):
        user.is_superuser = False
        user.save()

    @staticmethod
    def to_user(user):
        user.is_superuser = True
        user.save()
