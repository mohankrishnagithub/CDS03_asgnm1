from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tasks
# Create your views here.

def homePage(request):
    queryset = Tasks.objects.all().order_by('-id')
    context = {'tasks': queryset, }

    return render(request, 'index.html', context=context)

@csrf_exempt
def create(request):
    title = request.POST.get('title', False)
    print('Recieved->', title)

    if title and len(title.split()):  # This line ensures no Empty data is being saved to the database
        query = Tasks(Title=title)
        query.save()

        return render(request, 'partials/singletask.html', context={'task': query})
    else:
        print('Declined')
    return HttpResponse('Done')

@csrf_exempt
def update(request, task_id):
    queryset = Tasks.objects.get(id=task_id)

    if request.POST.get('perform_update', False):
        new_data = request.POST.get('title')
        if len(new_data):
            queryset.Title = new_data
            queryset.save()

        response = HttpResponse('')
        response["HX-Redirect"] = reverse('home')
        return response

    return render(request, 'partials/editForm.html', context={'task': queryset})

@csrf_exempt
def delete(request, task_id):
    query = Tasks.objects.get(id=task_id)
    query.delete()
    print('Deleted !!!')

    return HttpResponse('Deleted Succesfully!!!')


@csrf_exempt
def mark_completed(request, task_id):
    query = Tasks.objects.get(id=task_id)
    query.Completed = True
    query.save()

    return render(request, 'partials/singletask.html', context={'task': query})

'''
Django + DTL + HTMX
'''

# This new line is added online from giuthub
# This is a new line added from local repo
# This line for master branch
