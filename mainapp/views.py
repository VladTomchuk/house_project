from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Property, PropertyImages, Feedback, FeedbackImages
from .filters import PropertyFilter
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.translation import gettext as _

def home(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message_comment = request.POST['message-comment']
        ctx = {
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
            'message_comment': message_comment,
        }
        text_content = get_template('mainapp/mail/mail.txt').render(ctx)
        html_content = get_template('mainapp/mail/valuate-property/email-valuate-property.html').render(ctx)
        subject = 'Запрос оценки недвижимости'
        from_email = settings.EMAIL_HOST_USER
        to = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render(request, 'mainapp/mail/valuate-property/web-page-valuate-property.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
            'message_comment': message_comment,
            'title': 'Thank you for request!'
        })
    else:

        props = Property.objects.order_by('-updated_at')

        p = Paginator(props, 4)  # paginated_filtered_flats
        page_number = request.GET.get('page')
        property_page_obj = p.get_page(page_number)
        title = _("House Project - real estate services and integral reforms in Barcelona")
        return render(request, 'mainapp/home/home.html', {'props': property_page_obj, 'title': title})


def services(request):
    feedback = Feedback.objects.all()

    return render(request, 'mainapp/services/services.html', {'feedback': feedback, 'title': 'Services'})


def contacts(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message_comment = request.POST['message-comment']
        ctx = {
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
            'message_comment': message_comment,
        }
        text_content = get_template('mainapp/mail/mail.txt').render(ctx)
        html_content = get_template('mainapp/mail/contact-us/email-contact-us.html').render(ctx)
        subject = 'Запрос на обратную связь'
        from_email = settings.EMAIL_HOST_USER
        to = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render(request, 'mainapp/mail/contact-us/web-page-contact-us.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
            'message_comment': message_comment,
            'title': 'Thank you for request!'
        })
    else:
        return render(request, 'mainapp/contacts/contacts.html', {'title': 'Contacts'})


def all_property_search(request):
    context = {'title': 'Property'}

    filtered_propertys = PropertyFilter(
        request.GET,
        queryset=Property.objects.order_by('-updated_at')
    )

    context['filtered_propertys'] = filtered_propertys

    p = Paginator(filtered_propertys.qs, 6)  # paginated_filtered_flats
    page_number = request.GET.get('page')
    property_page_obj = p.get_page(page_number)

    context['property_page_obj'] = property_page_obj
    return render(request, 'mainapp/property/property.html', context=context)


def our_reforms(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        ctx = {
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
        }
        text_content = get_template('mainapp/mail/mail.txt').render(ctx)
        html_content = get_template('mainapp/mail/request_quote/email-request-quote.html').render(ctx)
        subject = 'Новый запрос на расчёт стоимости ремонтных работ'
        from_email = settings.EMAIL_HOST_USER
        to = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render(request, 'mainapp/mail/request_quote/web-page-request-quote.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
            'title': 'Thank you for request!'
        })
    else:
        all_reforms = Feedback.objects.all()

        p = Paginator(all_reforms, 6)  # paginated_filtered_flats
        page_number = request.GET.get('page')
        reforms_page_obj = p.get_page(page_number)
        title = _("Integral reforms in Barcelona")
        return render(request, 'mainapp/reforms/reforms.html',
                      {'all_reforms': all_reforms, 'reforms_page_obj': reforms_page_obj, 'title': title})


def view_our_reforms(request, reforms_id):
    feedback_item = Feedback.objects.get(pk=reforms_id)
    photos = FeedbackImages.objects.filter(feedback_item=feedback_item)
    return render(request, 'mainapp/reforms/inc/_view-our-reforms.html', {
        'feedback_item': feedback_item,
        'photos': photos,
        'title': feedback_item.name + '`s feedback'
    })


def view_property(request, property_id):
    property_item = Property.objects.get(pk=property_id)

    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message_comment = request.POST['message-comment']
        ctx = {
            "property_item": property_item,
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
            'message_comment': message_comment,
        }
        text_content = get_template('mainapp/mail/mail.txt').render(ctx)
        html_content = get_template('mainapp/mail/visit-request/email-visit-request.html').render(ctx)
        subject = 'Запрос на просмотр'
        from_email = settings.EMAIL_HOST_USER
        to = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render(request, 'mainapp/mail/visit-request/web-page-visit-request.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message_phone': message_phone,
            'message_comment': message_comment,
            "property_item": property_item,
            "title": 'Thank you for request!'
        })
    else:
        # property_item = Property.objects.get(pk=property_id)
        photos = PropertyImages.objects.filter(property_item=property_item)
        return render(request, 'mainapp/view_property/view_property.html', {
            "property_item": property_item,
            "photos": photos,
            "title": property_item.title
        })


def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
