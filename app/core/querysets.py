from .models import (
    TextModel
)


class Queryset:

    @staticmethod
    def create_row(request) -> TextModel:
        """
        Create an document with the text 
        :param request
        :return: TextModel
        """
        obj = TextModel.objects(
            text=request.get('text')
        ).first()

        if obj:
            obj.historical.append(dict(request))

        if not obj:
            obj = TextModel(**request)
            obj.historical.append(dict(request))

        return obj.save()   
