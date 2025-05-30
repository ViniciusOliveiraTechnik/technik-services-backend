from celery import shared_task

from accounts.models import Account

from django.core.mail import send_mail
from django.conf import settings

@shared_task()
def send_email_to_reset_password(access_token, user_email):

    reset_link = f'http://localhost:5173/forgot-password-confirm/?auth={access_token}'
    
    subject = 'Solicitação de recuperação de senha'
    message = f'Clique no link para recuperar a sua senha: {reset_link}'

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])

@shared_task()
def send_email_to_notify_password_change(user_id):

    try:

        user = Account.objects.get(id=user_id)

        subject = 'Notificação de redefinição de senha'
        message = f'Olá {user.first_name} {user.last_name}, sua solicitação de redefinição de senha foi concluída com sucesso. \nEntre com sua conta para acessar os recursos disponíveis'

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

    except Account.DoesNotExist:
        return