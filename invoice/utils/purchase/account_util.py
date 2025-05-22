import uuid

class AccountUtil:
    
    @staticmethod
    def normalize_accounts_params(accounts: str):

        if not accounts:

            return []
        
        validated_uuid = []

        for account in accounts.split(','):

            try:

                account = uuid.UUID(account.strip())

                validated_uuid.append(account)
            
            except ValueError:

                continue

        return validated_uuid