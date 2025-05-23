import uuid

class CardUtil:

    @staticmethod
    def normalize_cards_params(cards: str):
        
        if not cards:

            return []
        
        validated_cards = []

        for card in cards.split(','):

            try:

                card = uuid.UUID(card.strip())

                validated_cards.append(card)
            
            except ValueError:

                continue

        return validated_cards