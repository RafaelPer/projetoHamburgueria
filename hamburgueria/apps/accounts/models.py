from django.db import models
from apps.tipoFuncionario.models import tipoFuncionario
from apps.funcionarios.models import Funcionario
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password = None, is_active = True, is_admin = False, is_staff = False):
        if not email:
            raise ValueError("O USUARIO PRECISA TER UM EMAIL")
        if not password:
            raise ValueError("O USUARIO PRECISA TER UMA SENHA")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        print("create user "+str(user_obj));
        print("create user save "+str(user_obj.save(using = self._db)));
        user_obj.save(using = self._db)
        return user_obj

    def create_staffuser(self, email, password = None):
        user = self.create_user(
            email, 
            password = password,
            is_staff = True,
        )
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password = None):
        user = self.create_user(
            email, 
            password = password,
            is_admin = True,
            is_staff = True,
        )
        print("create superuser "+str(user));
        print("create superuser email "+str(email));
        print("create superuser password "+str(password));
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length = 100)
    nome = models.CharField(max_length = 100)
    sobrenome = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100, unique = True)
    active = models.BooleanField(default = True)
    usuarioTipoUsuario = models.ForeignKey(tipoFuncionario, on_delete=models.CASCADE, blank = True, null = True)
    usuarioFuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, blank = True, null = True)
    admin = models.BooleanField(default = False)
    staff = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_nome(self):
        return self.nome
    
    def get_sobrenome(self):
        return self.sobrenome

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)