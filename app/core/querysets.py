from .models import (
    TextModel
)


class Queryset:
    @staticmethod
    def create_row(request) -> TextModel:
        """
        Create a document with the text or update an existing one
        :param request: Dictionary containing text and other fields
        :return: TextModel instance
        """
        obj = TextModel.objects(text=request.get('text')).first()

        if obj:
            historical_entry = dict(request)
            obj.historical.append(historical_entry)
        else:
            obj = TextModel(**request)
            historical_entry = dict(request)
            obj.historical.append(historical_entry)

        return obj.save()
    
    @staticmethod
    def get_encrypt_data(encrypted_text) -> TextModel:
        
        obj = TextModel.objects.get(encrypted_text=encrypted_text)

        return obj
