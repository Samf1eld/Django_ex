"""from django.http import HttpResponse

def index(request):
    return HttpResponse("Done! Check more later!")"""
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.utils import timezone
import openai
API_KEY = open("API_KEY.txt", "r").read()
ORG_KEY = open("ORG_KEY.txt", "r").read()
openai.organization = ORG_KEY
openai.api_key = API_KEY

def index(request):
    latest_questions_list = Question.objects.order_by('-q_date_req')[:6]
    return render(request, 'openai_15/list.html', {'latest_questions_list': latest_questions_list})

def detail(request, question_id):
    try:
        q = Question.objects.get(id = question_id)
    except:
        raise Http404("Question was not found")

    return render(request, 'openai_15/detail.html', {'Question': q})

def back2main(request, question_id):
    return HttpResponseRedirect(reverse('openai:index',))

def new_question(request):
    return HttpResponseRedirect( reverse('openai:new_question_detail', ))

def new_question_detail(request):
    try:
        time = timezone.now()
    except:
        raise Http404("Statements was not found")

    return render(request, 'openai_15/new_question_detail.html', {'curtime': time})

def new_question_ask(request):
    a = Question.objects.create(q_name=request.POST['title'], q_request=request.POST['content'], q_date_req=timezone.now())

    airesponse = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": request.POST['content']}
        ]
    )

    additional_response = airesponse['choices'][0]['message']['content']
    a.q_response = additional_response.strip("\n").strip()
    a.q_date_res = timezone.now()
    a.save()

    return HttpResponseRedirect(reverse('openai:detail', args=(a.id,)))

