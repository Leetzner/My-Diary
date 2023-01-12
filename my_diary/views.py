from django.shortcuts import render

def frontpage(request):
    return render(request, 'my_diary/frontpage.html')
