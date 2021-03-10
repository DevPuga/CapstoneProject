from django.shortcuts import render, redirect
from .forms import UGGraduation

#Used in navbar to check if user is faculty
userGroup = ''

def checkIf(group, request):
    if request.user.groups.filter(name="%s"%group).exists():
        global userGroup
        userGroup = group
        return True
    else:
        return False

def get(request):
  checkIf("Faculty", request)
  checkIf("Student", request)
  requestedPage = (request.path).strip("/")
  if request.user.is_authenticated:
      if requestedPage == "":
          requestedPage = "dashboard"

      # Only allow faculty to access faculty page
      if requestedPage == "faculty":
          if checkIf("Faculty", request):
              pass
          else:
              return redirect('/error')

      # Set tab as active and render faculty tab if faculty
      context = {"%s_page"%requestedPage: "active", "userGroup": userGroup}

      return render(request, 'DeanProject/%s.html'%requestedPage, context)
  else:
      return redirect('/login')

def error(request):
    return render(request, 'DeanProject/error.html')
