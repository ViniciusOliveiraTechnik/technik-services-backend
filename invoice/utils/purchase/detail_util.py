class DetailUtil:

    def __init__(self, request_user):
        
        self.request_user = request_user

    def show_sensitive(self, obj):

        if self.request_user == obj.card.account:

            return True
        
        if self.request_user.is_staff:

            return True
        
        return False
    
    def mask_value(self, value):

        string = str(value).strip()

        return ''.join('*' if char != '.' else '.' for char in string)
    
    def mask_description(self, description):

        string = str(description).strip()

        return ''.join('*' if char != ' ' else ' ' for char in string)