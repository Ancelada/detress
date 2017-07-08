from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages

from . import models
from .properties import Properties

import json
import requests

def vk(request):

    code = request.GET.get('code', False)

    if code:

        vk_settings['code'] = code

        link = '{token_url}client_id={id}&client_secret={secret}&redirect_uri={redirect}&code={code}'.format(**Properties().vk_settings)
        data = json.loads(requests.get(link).text)
        link = 'https://api.vk.com/method/{0}?user_id={1}&access_token={2}'.format('users.get', data['user_id'], data['access_token'])
        data = json.loads(requests.get(link).text)

        first_name = data['response'][0]['first_name']
        last_name = data['response'][0]['last_name']
        full_name = '{0} {1}'.format(last_name, first_name)

        models.User.objects.update_or_create(
            name=full_name,
            oauth_type='VK'
        )

        request.session['authorized'] = True
        request.session['name'] = full_name

        return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        return HttpResponse('Error')


def fb(request):
    code = request.GET.get('code', False)
    if code:
        fb_settings['code'] = code

        link = '{token_url}client_id={id}&redirect_uri={redirect}&client_secret={secret}&code={code}'.format(**Properties().fb_settings)
        data = json.loads(requests.get(link).text)

        link = 'https://graph.facebook.com/v2.9/me?access_token={0}'.format(data['access_token'])
        data = json.loads(requests.get(link).text)

        models.User.objects.update_or_create(
            name=data['name'],
            oauth_type='FB'
        )

        request.session['authorized'] = True
        request.session['name'] = data['name']

        return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        return HttpResponse('Error')


def gp(request):
    code = request.GET.get('code', False)
    if code:
        link = 'https://accounts.google.com/o/oauth2/token'
        params = {
            'client_id' : Properties().gp_settings['id'],
            'client_secret' : Properties().gp_settings['secret'],
            'redirect_uri' : Properties().gp_settings['redirect'],
            'grant_type' : 'authorization_code',
            'code' : code,
        }
        data = json.loads(requests.post(link, params).text)
        params['access_token'] = data['access_token']

        link = 'https://www.googleapis.com/oauth2/v3/userinfo'
        data = json.loads(requests.get(link, params).text)

        models.User.objects.update_or_create(
            name=data['name'],
            oauth_type='G+'
        )

        request.session['authorized'] = True
        request.session['name'] = data['name']

        return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        return HttpResponse('Error')


def ya(request):
    code = request.GET.get('code', False)
    if code:
        link = 'https://oauth.yandex.ru/token'
        params = {
            'client_id' : Properties().ya_settings['id'],
            'client_secret' : Properties().ya_settings['secret'],
            'grant_type' : 'authorization_code',
            'code' : code,
        }
        data = json.loads(requests.post(link, params).text)

        token = data['access_token']

        link = 'https://login.yandex.ru/info?format=json&with_openid_identity=true&oauth_token={0}'.format(token)
        data = json.loads(requests.get(link).text)

        return HttpResponse(data['id'])

        models.User.objects.update_or_create(
            name=data['real_name'],
            oauth_type='YA'
        )



        request.session['authorized'] = True
        request.session['name'] = data['real_name']

        return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        return HttpResponse('Error')
