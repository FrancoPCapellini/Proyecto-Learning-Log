from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """ A topic the user is learning about. """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """ Return a string representation of the model. """
        return self.text
    
class Entry(models.Model):
    """ Something specific learned about a topic. """
    # ForeingKey is the code that conect each entry to a specific topic
    # each topic is assigned a key or ID when it's created.
    # on_delete=models.CASCADE when a topic is deleted, all the entries associated with ...
    # ... that topic should be deleted as well. (cascading delete)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) # It allows to present entries in the order they were created
    
    class Meta:
        verbose_name_plural = "entries"
        
    def __str__(self):
        """ Return a string representation of the model. """
        return f"{self.text[0:50]}..."