from django.contrib import admin
from .models import *


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('press',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'title',)


class RolePersonAdmin(admin.TabularInline):
    model = RolePerson
    extra = 1


@admin.register(PersonAlias)
class PersonAliasAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(LocationAlias)
class LocationAliasAdmin(admin.ModelAdmin):
    pass


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    inlines = (RolePersonAdmin,)
    search_fields = ('title', 'container', 'institution', 'series_title', 'doi')