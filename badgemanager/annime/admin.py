from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from .models import User, AnnimeVideo


class UserAdmin(DjangoUserAdmin):
    # Code depuis UserAdmin de django UserAdmin
    DjangoUserAdmin.list_display += (
        "job",
        "has_starter",
        "has_pionner",
        "has_collector",
    )
    DjangoUserAdmin.fieldsets += ((_("User info"), {"fields": ("job", "picture")}),)


class AnnimeVideoAdmin(admin.ModelAdmin):
    """Admin View for AnnimeVideo"""

    list_display = (
        "photo_portrait",
        "title",
        "author",
        "created_at",
        "number_of_views",
    )
    list_display_links = ("title", "author")
    list_filter = (
        "title",
        "author",
    )

    fieldsets = (
        ("Select User", {"fields": ("author",)}),
        (
            "Annime",
            {
                "fields": (
                    "title",
                    "description",
                    "number_of_views",
                )
            },
        ),
        ("Video", {"fields": ("portrait", "file")}),
    )

    search_fields = ("author",)
    date_hierarchy = "created_at"
    ordering = ("created_at",)

    def photo_portrait(self, obj):
        if obj.portrait:
            return mark_safe(
                f'<img src="{obj.portrait.url}" style="height:60px; width:60px">'
            )
        else:
            return "Aucun fichier"

    def video_annime(self, obj):
        if obj.file:
            # return mark_safe(f'<img src="{obj.portrait.url}" style="height:60px; width:60px">')
            return mark_safe(
                f'<video width="100px" height="200px" controls><source src="{obj.file.url}" type="video/mp4"></video>'
            )
        else:
            return "Aucun fichier"

    video_annime.short_description = "Vidéo"


admin.site.register(User, UserAdmin)
admin.site.register(AnnimeVideo, AnnimeVideoAdmin)
