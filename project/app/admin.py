from django.contrib import admin
from .models import Category, Model
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    model = Category


class ModelAdmin(TranslationAdmin):
    model = Model


admin.site.register(Model)
admin.site.register(Category)
