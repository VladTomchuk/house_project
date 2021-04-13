from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class Feedback(models.Model):
    img = models.ImageField(_('Image'), upload_to='photos/feedback/main_photo/%Y/%m/', blank=True)
    avatar = models.ImageField(_('Avatar'), upload_to='photos/feedback/avatar/%Y/%m/', blank=True)
    name = models.CharField(max_length=150, verbose_name=_('Name'), blank=True)
    reformed = models.CharField(max_length=150, verbose_name=_('Reformed'), blank=True)
    feedback = models.TextField(verbose_name=_('Feedback'), blank=True)
    country = models.CharField(max_length=150, verbose_name=_('Country'), blank=True)
    city = models.CharField(max_length=150, verbose_name=_('City'), blank=True)

    def get_absolute_url(self):
        return reverse('view_our_reforms', kwargs={"reforms_id": self.pk})

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)
    img = models.ImageField(_('Image'), upload_to='photos/main_photo/%Y/%m/', blank=True)
    sq = models.FloatField(_('Square'), max_length=4, default='1')
    stage = models.IntegerField(_('Stage'), default='1')
    bathroom = models.IntegerField(_('Bathroom'), default='1')
    rooms = models.IntegerField(_('Room'), default='1')
    price = models.IntegerField(_('Price'), default='1')
    CHOICES = (
        ('Rent', _('Rent')),
        ('Sale', _('Sale')),
    )
    deal = models.CharField(_('Deal'), max_length=14, choices=CHOICES, default='Rent')
    PROVINCE_CHOICE = (
        ('Barcelona', _('Barcelona')),
        ('Girona', _('Girona')),
        ('Lleida', _('Lleida')),
        ('Tarragona', _('Tarragona')),
    )
    province = models.CharField(_('Province'), max_length=100, choices=PROVINCE_CHOICE, default='Barcelona')
    is_published = models.BooleanField(_('Published'), default=True)

    def get_absolute_url(self):
        return reverse('view_property', kwargs={"property_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Propertys')
        ordering = ['-created_at']


class PropertyImages(models.Model):
    property_item = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='photos/secondary_photo/%Y/%m/', blank=True)

    def __str__(self):
        return self.property_item.title


class FeedbackImages(models.Model):
    feedback_item = models.ForeignKey(Feedback, default=None, on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='photos/feedback/all_photos/%Y/%m/', blank=True)