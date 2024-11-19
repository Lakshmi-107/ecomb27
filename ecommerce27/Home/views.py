from django.shortcuts import render

# Create your views here.


def work(request):

    context = {
        "Programming_language": "Python",
        "Assignment": "Assignment_7",
    }
    return render(request, 'Assign.html', context)
