from django.contrib import admin
from .models import Derector,Category,Move

# Register your models here.
admin.site.register(Derector)
admin.site.register(Category)

@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    search_fields = ['name','desc']
    list_filter = ['director','category']