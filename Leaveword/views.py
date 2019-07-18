from django.shortcuts import render

# Create your views here.
def leaveword(req):
    return render(req,"leave_word.html",locals())