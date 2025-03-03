from django.db import models
from ..core.database import add_faq

class FAQ(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = models.JSONField(default=dict)

    def save(self, *args, **kwargs):
        """Al guardar en Django, también guardamos en ChromaDB"""
        super().save(*args, **kwargs)
        add_faq(self.question, self.answer)
    
    def __str__(self):
        return self.question