from django.contrib import admin
from .models.faq import FAQ
# Register your models here.

@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question','answer']