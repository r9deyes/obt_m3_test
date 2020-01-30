from django.db import models


class Question(models.Model):
    text = models.CharField('text', max_length=255)
    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        models.CASCADE,
        verbose_name='question',
    )
    text = models.CharField('text', max_length=255)
    is_correct = models.BooleanField('is_correct', default= False)
    
    def __str__(self):
        return '%s (%scorrect)'%(self.text, '' if self.is_correct else 'not')
