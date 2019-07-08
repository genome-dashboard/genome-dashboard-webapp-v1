# -*- coding: utf-8 -*-

# from django.http import HttpResponse
# from django.http import Http404
# from django.template import loader
# from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


"""
# Superceded by IndexView class.
def index(request):
    # Simple View - basic response.
    # return HttpResponse("Hello, world. You're at the polls index.")

    # Complex view - question list.
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # Templated view.
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))

    # Templated view using shortcut.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {'latest_question_list': latest_question_list}
    return render(request, template, context)
"""

# """
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return the last five published questions.
        return Question.objects.order_by('-pub_date')[:5]
# """


"""
# Superceded by DetailView class.
def detail(request, question_id):
    # Simple View - basic response.
    # return HttpResponse("You are looking at question %s." % question_id)

    # Complex view - with error handling.
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    # return render(request, 'polls/detail.html', {'question': question})

    # Using shortcut for 404 error.
    template = 'polls/detail.html'
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, template, context)
"""

# """
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
# """


# No superceding view.
def vote(request, question_id):
    # Simple View - basic response.
    # return HttpResponse("You are voting on question %s." % question_id)

    # Complex response using form.
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


"""
# Superceded by ResultsView class.
def results(request, question_id):
    # Simple View - basic response.
    # response = "You are looking at the results of question %s."
    # return HttpResponse(response % question_id)

    # Complex response to form.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""

# """
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
# """
