from datetime import datetime

from mongoengine.fields import (
    StringField,
    DictField,
    DateTimeField,
    ListField
)
from mongoengine import Document


class BaseDocument:
    """Document base to inherit all models

    Attributes:
        updated_at (datetime.datetime)
        created_at (datetime.datetime)
        deleted_at (datetime.datetime)
        deleted_by (DictField)
    """
    updated_at = DateTimeField(required=False)
    created_at = DateTimeField(default=lambda: datetime.now())
    deleted_at = DateTimeField(required=False)
    deleted_by = DictField(required=False)

    def update(self):
        self.updated_at = datetime.now()
        self.save()


class TextModel(BaseDocument, Document):
    meta = {
        "collection": "text",
        "indexes": ["text", "encrypted_text"]
    }

    text = StringField(default="")
    encrypted_text = StringField(default="")
    total_time = StringField(default="")
    cpu_percent = StringField(default="")
    memory_percent = StringField(default="")
    historical = ListField(default=[])

    def to_json(self):

        return {
            "text": self.text,
            "encrypted_text": self.encrypted_text,
            "total_time": self.total_time,
            "cpu_percent": self.cpu_percent,
            "memory_percent": self.memory_percent,
            "historical": [row.to_json() for row in self.historical]
        }
