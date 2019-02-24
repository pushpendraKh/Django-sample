from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('pub_date')
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_questions': latest_questions
    }
    # return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})
    # return HttpResponse('Pushpendra, this is the detail view of question of %s' % question_id)

def results(request, question_id):
    return HttpResponse('Pushpendra, there is the result view of question of %s' % question_id)

def vote(request, question_id):
    return HttpResponse('Pushpendra, this is the vote view of question of %s' % question_id)
