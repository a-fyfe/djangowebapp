from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

# . . .

@login_required(redirect_field_name='next', login_url='/user_auth/')
def vote(request, question_id):

    """This method will be used to allow users to vote in website polls

    :returns: Selecting valid poll option returns poll results
    """

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
        pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
# Always return an HttpResponseRedirect after successfully
# dealing with POST data. This prevents data from being
# posted twice if a
# user hits the Back button.
        return HttpResponseRedirect(
            reverse('vote:results', args=(question_id,))
        )

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """This method will be used to show users poll resulst

    :returns: Shows users current results from a specific poll
    """

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})