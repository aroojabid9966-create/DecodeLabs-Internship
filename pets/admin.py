from django.contrib import admin
from .models import Pet



@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "species",
        "breed",
        "age",
        "gender",
        "status",
    )

    list_filter = ("species", "gender", "status")

    search_fields = ("name", "breed", "species")
