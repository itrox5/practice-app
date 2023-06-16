from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def january(request):
    return HttpResponse('Always do push ups')

def february(request):
    return HttpResponse('Always do squats')

def monthly_challenge(request, month):
  challenge_text = None
  if month == 'march':
    challenge_text = 'Go veggie'
  elif month == 'april':
    challenge_text = 'Walk 20 minutes a day'
  else:
    return HttpResponseNotFound('This month is not supported')
  return HttpResponse(challenge_text)




