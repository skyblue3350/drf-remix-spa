from django.contrib import admin

from .models import Entry, User

# Register your models here.
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
