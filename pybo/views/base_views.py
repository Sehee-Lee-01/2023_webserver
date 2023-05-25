from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Question


def index(request):
    """
    pybo 목록 출력
    """
    page = request.GET.get("page", "1")  # page
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(answer__content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    # return HttpResponse("안녕하세요! pybo에 오신 것을 환영합니다!")
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects. get(id = question_id)
    question = get_object_or_404(Question, pk=question_id)
    voted = False
    for voter in question.voter.all():
        if (request.user == voter):
            voted = True
    context = {'question': question, 'voted': voted}
    return render(request, 'pybo/question_detail.html', context)
