from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_to_activate_account(access_token, user_email):

    activate_link = f'http://localhost:5173/activate-account/?auth={access_token}'

    subject = 'Verificação de atividade de conta'

    message = f'Clique no link para ativar a sua conta: {activate_link}'

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])