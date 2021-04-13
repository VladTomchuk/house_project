from modeltranslation.translator import translator, TranslationOptions
from .models import Property, Feedback


class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class FeedbackTranslationOptions(TranslationOptions):
    fields = ('name', 'feedback', 'country', 'city', 'reformed')


translator.register(Property, PropertyTranslationOptions)
translator.register(Feedback, FeedbackTranslationOptions)
