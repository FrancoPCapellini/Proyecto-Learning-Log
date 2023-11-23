from django.shortcuts import render, redirect 
from .models import Topic
from .forms import TopicForm # redirect y TopicForm se agregan con los forms, despues de crear forms.py

# Create your views here.
def index(request):
    """ The home page for Learning Log. """
    return render(request, "learning_logs/index.html")

def topics(request):
    """ Show all topics. """
    topics = Topic.objects.order_by("date_added")
    context = {'topics': topics}
    """
    A context is a dictionary in which the keys are names we'll use in the template to access 
    the data, and the values are the data we need to send to the template.
    """
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id): # accepts the value captured by the expression /<int:topic_id>/ .
    """ Show a single topic and all its entries. """
    # topic and entries are queries, for check if this is ok, test it in Django shell
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added') # the '-' sorts the results in reverse order. 
    context = {'topic':topic , 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Add a new topic. """
    # GET request is used for pages that only reed data from the server.
    # POST request when the user need to submit information through a form. 
    """
    The new_topic() function takes in the request object as a parameter. 
    When the user initially requests this page, their browser will send a GET request.
    Once the user has filled out and submitted the form, their browser will submit a POST request.
    Depending on the request, we'll know whether the user is requesting a blank form
    (a GET request) or asking us to process a completed form (a POST request).  
    """
    if request.method != 'POST': # The request method is a GET or POST
        # No data submitted; create a blank form. 
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data = request.POST)
        if form.is_valid(): # Checks that all required fields have been filled in and that the data                   
            form.save()     # entered matches the field type expected. ej: the length we specified in models.py .
            return redirect('learning_logs:topics') 
            # redirect is used to redirect the user back to the topics page after they submit their topic

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
