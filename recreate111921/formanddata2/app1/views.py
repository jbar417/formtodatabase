from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CommentDataForm
from django.views import View
# Create your views here.

class functionview1(View):
    def get(self, request):
        form = CommentDataForm()
        return render(request, "app1/forms1.html", {
            "formkey": form
        })
    def post(self, request):
        form = CommentDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/submitted")
        return render(request, "app1/forms1.html", {
            "formkey": form
        })

def functionsubmitted(request):
    return render(request,"app1/submitted.html")
