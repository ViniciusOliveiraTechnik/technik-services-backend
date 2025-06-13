from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from django.db import models

import uuid

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the Account model.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and return a user with an email and password.

        Args:
            email (str): The email of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields to set on the user.
        
        Returns:
            Account: The created user instance.
        
        Raises:
            ValueError: If the email is not provided.
        """
        
        if not email:
            raise ValueError("O email deve ser passado!")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and return a superuser with an email and password.

        Args:
            email (str): The email of the superuser.
            password (str): The password for the superuser.
            **extra_fields: Additional fields to set on the superuser.
        
        Returns:
            Account: The created superuser instance.
        
        Raises:
            ValueError: If is_staff or is_superuser is not set to True.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=true")
        
        return self.create_user(email, password, **extra_fields)
    
class Account(AbstractUser):
    """ 
    Custom user model that extends AbstractUser.
    It uses email as the unique identifier instead of username.
    """
    class Meta:
        """
        Meta class for the Account model.
        """
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        constraints = [
            models.UniqueConstraint(
                name='Unique User',
                fields=['first_name', 'last_name', 'email', 'phone_number', 'hashed_cpf'], 
                violation_error_message='Não é possivel adicionar esse usuário'
                )
        ]

    class HierarchyOptions(models.TextChoices):
        """
        Enumeration for hierarchy levels.
        """
        APPRENTICE = 'Aprendiz'
        INTERN = 'Estagiário'
        COLLABORATOR = 'Colaborador'
        COORDINATOR = 'Cordenador'
        MANAGER = 'Gerente'
        DIRECTOR = 'Diretor'
    
    # fields
    username = None # Deactivating username

    id = models.UUIDField(verbose_name='ID do Usuário', primary_key=True, default=uuid.uuid4, unique=True, null=False, editable=False)
    
    first_name = models.CharField(verbose_name='Nome', max_length=80)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=80)
    
    job_title = models.CharField(verbose_name='Cargo', max_length=150, default='')
    hierarchy_level = models.CharField(verbose_name='Nível hierárquico', choices=HierarchyOptions.choices, max_length=20, default='') 

    email = models.EmailField(verbose_name="Email")

    otp_secret = models.BinaryField(verbose_name='Segredo OTP', blank=True, null=True)

    is_activated = models.BooleanField(verbose_name='Usuário ativo', default=False)
    is_authenticated = models.BooleanField(verbose_name='Usuário autenticado', default=False)

    encrypted_cpf = models.BinaryField(verbose_name="CPF Criptografado", null=True, blank=True)
    hashed_cpf = models.CharField(verbose_name="Hash do CPF", max_length=64, null=True, blank=True)

    phone_number = models.CharField(verbose_name='Contato', max_length=20)
    phone_number_region = models.CharField(verbose_name='Região', max_length=2, default='BR')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    # Manager
    objects = CustomUserManager()
    
    def __str__(self) -> str:

        return f"{self.first_name} {self.last_name}"
    
    # def set_cpf(self, cpf: str):

    #     if not cpf:

    #         raise ValueError('CPF is empty')
        
    #     cpf_util = CPFUtil()

    #     self.encrypted_cpf = cpf_util.encrypt(cpf)

    #     self.hashed_cpf = cpf_util.create_hash(cpf)

    # def check_cpf(self, cpf: str) -> bool:

    #     if not cpf:

    #         raise ValueError('CPF is empty')
        
    #     cpf_util = CPFUtil()

    #     return self.hashed_cpf == cpf_util.create_hash(cpf)