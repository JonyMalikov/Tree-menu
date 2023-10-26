from django.contrib import admin

from .models import ChieldMenu, Menu


@admin.register(ChieldMenu)
class ChieldMenuAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "chield_name",
        "father_name",
    )
    list_editable = (
        "chield_name",
        "father_name",
    )
    empty_value_display = "-пусто-"


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    list_editable = ("name",)
    search_fields = ("name",)
