from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
  "january" : "always do push up - dictionary",
  "february" : "always do squats - dictionary",
  "march" : "always do push up - dictionary",
  "april" : "always do push up - dictionary",
  "may" : "always do push up - dictionary",
  "june" : "always do push ups in June - dictionary",
  "july" : "always do push up - dictionary",
  "august" : "always do push up - dictionary",
  "september" : "always do push up - dictionary",
  "october" : "always do push up - dictionary",
  "november" : "always do push up - dictionary",
  "december" : "always do push up - dictionary"
}

def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())

  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month-challenge", args=[month])
    # Generate new string for every month 
    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"



  response_data = f"<ul>{list_items}</ul>"
 
  return HttpResponse(response_data)

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

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month.lower()]
    return render(request, "challenges/challenge.html", {

      "text": challenge_text,
      "month_name": month
      
    })
   
  except:
    return HttpResponseNotFound("<h1>This is not a month</h1>")