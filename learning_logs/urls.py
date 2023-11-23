""" Defines URL patterns for learning_logs. """
from django.urls import path
from . import views # el . quiere decir que importe desde el mismo directorio que esta urls.py

app_name = "learning_logs" # Namespace
urlpatterns = [ # is a list of individual pages that can be requested from the learning_logs app.
    # Home page
    path('',views.index, name = "index"),
    # Page that shows all topics.
    path('topics/', views.topics, name = 'topics'),
    # Detail page for a single topic. 
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name = 'new_topic'),
]
""" path() take 3 arguments
    first: route the request URL to a view.
    second: specific function to call in views.py.
    third: provides the name "index" for this URL.
"""