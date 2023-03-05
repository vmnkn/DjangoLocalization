from .models import Category, Model
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Model)
class ModelTranslationOptions(TranslationOptions):
    fields = ('name', )
