from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage
from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('QA OK')


def question_list(request, popular=False):
    if popular:
        questions = Question.objects.all().order_by('-rating')
    else:
        questions = Question.objects.all().order_by('-added_at', '-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except InvalidPage:
        raise Http404
    return render(request, 'qa/index.html', {'page': page})


def question_list_pop(request):
    return question_list(request, popular=True)


def question_detail(request, question_id=None):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/question_detail.html',
                  {'question': question,
                   'answers': question.answer_set.all()})
