from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


admin.site.site_title = "Tel Zone Админ"
admin.site.site_header = "Tel Zone"
admin.site.index_title = "Tel Zone Админ"
admin.site.site_brand = "Tel Zone"
admin.site.welcome_sign = "Tel Zone"
admin.site.copyright = "Tel Zone"
admin.site.unregister(Group)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'first_name', 'role', 'is_active']
    list_display_links = ('id', 'username', 'first_name')
    list_editable = ('is_active',)
    search_fields = ('username', 'first_name')
    list_filter = ('is_active', 'role')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
