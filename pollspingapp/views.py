from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


# Create your views here.

# Similarly, the ListView generic view uses a default template called <app name>/<model name>_list.html;
class IndexView(generic.ListView):
    template_name = 'pollspingapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html. I
class DetailView(generic.DetailView):
    model = Question
    template_name = 'pollspingapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pollspingapp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pollspingapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pollspingapp:results', args=(question.id,)))
