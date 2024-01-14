from django.contrib import admin
from .models import Social, Member

class SocialInline(admin.TabularInline):
    model = Social
    extra = 1  # Number of empty forms to display

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created', 'updated')
    search_fields = ('name', 'role')
    readonly_fields = ('created', 'updated')
    inlines = [SocialInline]

admin.site.register(Member, MemberAdmin)
admin.site.register(Social)