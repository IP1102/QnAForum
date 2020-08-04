from django.shortcuts import render
from .models import Forum, Questions
# Create your views here.



def home(request):
    text = 'Welcome'
    return render (request, 'home.html', {'message':text})

def result(request):
    name = request.POST['name']
    quest = request.POST['quest']
    ans = request.POST['ans']

    forum = Forum(name=name,ans = ans, quest=quest)
    forum.save()

    # que = Questions()
    # cont = ['Is Shawshank Redemption the greatest movie of all time? Please explain.',
    #     'Is Django better than NodeJS?',
    #     'Where Nordic Gods real?']

    # for c,con in enumerate(cont):
    #     que.quest_content = con
    #     que.quest_id = 'quest'+(c+1)
    #     que.save()
    forum_test = Forum.objects.get(id=forum.id)

    return render(request, 'results.html', {
        'name':forum_test.name,
        'question':forum_test.quest,
        'answer': forum_test.ans
    })