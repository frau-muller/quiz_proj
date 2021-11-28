from django.db import models
import random

DIFF_CHOICES = (
    ('лёгка', 'лёгка'),
    ('сярэдняя ', 'сярэдняя '),
    ('цяжка ', 'цяжка'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Працягласць віктарыны ў хвілінах")
    required_score_to_pass = models.IntegerField(help_text="патрабаваны бал у %")
    difficluty = models.CharField(max_length=10, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Вiктарыны'