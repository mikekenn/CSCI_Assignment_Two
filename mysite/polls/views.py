"""Required libraries"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Create your views here.
def detail(request, question_id):
    """Function to return question number"""
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    """Function to return results of a question"""
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """Function to provide end-user information on the question they are voting on."""
    return HttpResponse("You're voting on question %s." % question_id)