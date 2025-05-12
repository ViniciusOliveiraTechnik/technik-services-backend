from rest_framework.exceptions import NotFound

def get_object(pk):

    from accounts.models import Account

    try:
        return Account.objects.get(id=pk)

    except Account.DoesNotExist:
        raise NotFound(detail='Usuário não encontrado')