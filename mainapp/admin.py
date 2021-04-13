from django.contrib import admin
from .models import Property, PropertyImages, Feedback, FeedbackImages


class FeedbackImagesInline(admin.StackedInline):
    model = FeedbackImages


class FeedbacksImagesAdmin(admin.ModelAdmin):
    pass


class PropertyImagesInline(admin.StackedInline):
    model = PropertyImages


class PropertyImagesAdmin(admin.ModelAdmin):
    pass


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'git description')
    inlines = [PropertyImagesInline]
    # list_display = ('id', 'created_at', 'updated_at', 'is_published')
    # list_display_links = ('id',)
    # search_fields = ('title', 'description')
    exclude = ['title', 'description']

    class Meta:
        model = Property


class FeedbackAdmin(admin.ModelAdmin):
    inlines = [FeedbackImagesInline]
    exclude = ['name', 'feedback', 'country', 'city', 'reformed']

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Property, PropertyAdmin)
