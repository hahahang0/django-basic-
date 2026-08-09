from django.shortcuts import render
from .forms import UserForm


# Create your views here.
# def user_form(request):
#     form = UserForm()
#     return render(
#         request,
#         'accounts/user_form.html',
#         {
#             "form":form
#         }
#     )

#views with validation 

def user_form(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = UserForm()
    return render(
        request,
        "accounts/user_form.html",
        {
            "form" : form
        }
    )
    