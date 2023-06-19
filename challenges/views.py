from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
  "january" : "always do push up - dictionary",
  "february" : "always do squats - dictionary",
  "march" : "always do push up - dictionary",
  "april" : "always do push up - dictionary",
  "may" : "always do push up - dictionary",
  "june" : "always do push up - dictionary",
  "july" : "always do push up - dictionary",
  "august" : "always do push up - dictionary",
  "september" : "always do push up - dictionary",
  "october" : "always do push up - dictionary",
  "november" : "always do push up - dictionary",
  "december" : "always do push up - dictionary"
}

def january(request):
  return HttpResponse('Always do push ups')

def february(request):
  return HttpResponse('Always do squats')

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

# If months intiger intered is more than 12
  if month > len(months):
    return HttpResponseNotFound("Invalid month")

  redirect_month = months[month - 1] #list item are 0,1,2 etc so to represent correct month we gotta go back by 1
  redirect_path = reverse("month-challenge", args=[redirect_month]) # builds full path /challenge/january
  return HttpResponseRedirect(redirect_path)
  #return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month.lower()]
    response_data = f"<h1>{challenge_text}</h1>"
   # return HttpResponse(challenge_text)
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("<h1>This is not a month</h1>")
 

# Long if statement version
# def monthly_challenge(request, month):
#   challenge_text = None
#   month = month.lower()
#   if month == 'march':
#     challenge_text = 'Go veggie'
#   elif month == 'april':
#     challenge_text = 'Walk 20 minutes a day'
#   elif month == 'may':
#     challenge_text = 'Swim twice a week'
#   elif month == 'june':
#     challenge_text = 'Always stretch every day'
#   else:
#     return HttpResponseNotFound('This month is not supported')
#   return HttpResponse(challenge_text)
