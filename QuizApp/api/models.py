from django.db import models
# from django.db.models.signals import post_save,pre_save,pre_init
# from django.dispatch import receiver

# Create your models here.

class Quiz(models.Model):

    name = models.CharField(max_length=122)
    total_question = models.IntegerField(default=10)
    time = models.IntegerField(default=30)
    subject = models.CharField(max_length=122)
    difficulty = models.CharField(max_length=122)
    isCompleted = models.BooleanField(default=False)
    total_marks = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name) or ' '

# @receiver(post_save,sender=Quiz)
# def Quiz_post_save(sender, instance,created,*args, **kwargs):
#     if created:
#         for i in range(instance.total_question):
#             Question.objects.create(name=instance)
#     else:
#         total = Question.objects.filter(name= instance)
#         if instance.total_question > len(total):
#             for i in range(len(total),instance.total_question):
#                 Question.objects.create(name=instance)



class Question(models.Model):
    type = (
        ("single","single"),
        ("multiple","multiple")
    )
    name = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='quiz_name')
    question = models.TextField()
    total_options = models.IntegerField(default=4)
    question_type = models.CharField(max_length=122,choices=type, default="single")
    total_answer = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.name) + " (Question - " + str(self.question) + ")" or ' '

# @receiver(post_save,sender=Question)
# def Question_option_post_save(sender, instance,created,*args, **kwargs):
#     if created:
#         for i in range(instance.total_options):
#             Option.objects.create(question=instance)
#     else:
#         option = Option.objects.filter(question= instance)
#         if instance.total_options > len(option):
#             for i in range(len(option),instance.total_options):
#                 Option.objects.create(question=instance)

class Option(models.Model):
    question = models.ForeignKey("api.Question",on_delete=models.CASCADE,related_name='options')
    option = models.CharField(max_length=122)

    def __str__(self) -> str:
        return str(self.question.question) or ' '

# @receiver(post_save,sender=Question)
# def Question_answer_post_save(sender, instance,created,*args, **kwargs):
#     if created:
#         for i in range(instance.total_answer):
#             Answer.objects.create(question=instance)
#     else:
#         answers = Answer.objects.filter(question= instance)
#         if instance.total_answer > len(answers):
#             for i in range(len(answers),instance.total_answer):
#                 Answer.objects.create(question=instance)

class Answer(models.Model):
    question = models.ForeignKey("api.Question",on_delete=models.CASCADE,related_name='answer')
    answer = models.CharField(max_length=122)

    def __str__(self) -> str:
        return str(self.question.question) or ' '
    

class CurrentAnswer(models.Model):
    question = models.ForeignKey("api.Question",on_delete=models.CASCADE,related_name="current_answer")
    answer = models.CharField(max_length=122)

    def __str__(self) -> str:
        return ' current answer:- ' + self.answer