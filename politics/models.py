from django.db import models
from django.urls import reverse

class Debate(models.Model):
    username = models.CharField(max_length =20 , blank=True, default='')
    description = models.CharField(max_length =300 , blank=True, default='')
    title = models.CharField(max_length = 200, blank=True, default='')
    date = models.CharField(max_length =10, blank=True, default='')
    genre = models.CharField(max_length = 20, blank=True, default='')
    
    pfp = models.CharField(max_length =12, blank=True, default='')
    
    def __str__(self):
        return self.title + ' - ' + self.username
    
    def get_absolute_url(self):
        return reverse('politics:detail', kwargs={'pk': self.pk})
        
    
                                                                                                                                                        

class Comment(models.Model):
    post = models.ForeignKey('Debate',
    on_delete=models.CASCADE, related_name='comments', null=True)
    user = models.CharField(max_length=250)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved= models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    
    def approved(self):
        self.approved = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('comment-add', kwargs={'content':self.content})
        
   
   