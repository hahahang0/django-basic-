from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# def home(request):
#     return HttpResponse("hello world ! hangthim is back. ")

from django.shortcuts import render

# def home(request):
#     return render(request,'home.html')


#passing data 

# def home(request):
#     context = {
#         'username' : 'hangthim'
#     }

#     return render(request,'home.html',context)


#passing multiple vairables 

# def home(request):
#     context = {
#         'username' : 'hangthim',
#         'age' : 22,
#         'address' : 'birtamode,jhapa'
#     }

#     return render(request,'home.html',context)


### passing the data in the lists 

context = {
    'user' : [
        'hangtim','limbu',22,'birtamode, jhapa'
    ],
    'games': ['call of duty','meccha chamoelan','the walking dead']
}

def home(request):
    return render(request,'home.html',context)