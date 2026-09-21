from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True
        