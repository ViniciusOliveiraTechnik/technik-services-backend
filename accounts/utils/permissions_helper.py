class PermissionsHelper:

    def __init__(self, user):
        
        self.user = user

    def check_internal(self) -> bool:

        return self.user.groups.filter(name='Internals').exists()