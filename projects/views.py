from django.shortcuts import render
from django.http import HttpResponse

all_projects=[
    {
        'id':'1',
        'title':'portfolio website',
        'description':'cool stuff'

    },
    {
        'id':'2',
        'title':'Ecommerce website',
        'description':'cool stuff'

    },
    {
        'id':'3',
        'title':'Social network',
        'description':'cool stuff'

    }
]

def projects(request):
    msg='Hello'
    number=1

    context={"msg":msg, "num":number, 'projects':all_projects}
    return render(request,'projects/projects.html',context)

def project(request, pk):
    projectObj= None
    for i in all_projects:
        if i['id']==pk:
            projectObj=i
    return render(request, 'projects/single-project.html', {"project":projectObj})


