from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings

from .forms import ContactForm
from .models import (Contacts, Post, Cat)


def indx_view(request):
    if request.method == 'POST':
        previous_page = request.get_full_path()

        form = ContactForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            msg = Contacts.objects.create(name=name, email=sender, message=message)
            msg.save()

            return render(request, 'redir/thanks.html', {'save_contact': True, 'previous_page': previous_page })
        else:
            return render(request, 'redir/form_error.html', {'save_contact': True, 'previous_page': previous_page })
    else:
        form = ContactForm()

    return render(request, 'redir/index.html', {'form': form })


def blog(request):
    cats = Cat.objects.all()
    posts = Post.objects.all()
    return render(request, 'redir/blog.html', {'cats': cats, 'posts': posts, 'blog': True })


def thanks(request):
    return render(request, 'registration/thanks.html')


def quotes(request):
    return render(request, 'redir/quotes.html')


def quotes_api(request):
    return render(request, 'redir/quotes_api.html')


def weather(request):
    return render(request, 'redir/weather.html')


def wikipedia(request):
    return render(request, 'redir/wikipedia.html')


def page_not_found(request):
    return render(request, template_name='redir/404.html', context=None, content_type=None, status=404, using=None)


def jonas_salk(request):
	return render(request, 'redir/jonas_salk.html')


def permission_denied(request):
    return render(request, template_name='redir/403.html', context=None, content_type=None, status=403, using=None)


def server_error(request):
    return render(request, template_name='redir/500.html', context=None, content_type=None, status=500, using=None)


def bad_request(request):
    return render(request, template_name='redir/400.html', context=None, content_type=None, status=400, using=None)
