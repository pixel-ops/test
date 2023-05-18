from rest_framework import serializers
from .models import Quiz,Question,Option,Answer,CurrentAnswer
from django.urls import reverse

class QuizSerializer(serializers.ModelSerializer):
    total_marks = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    
    class Meta:
        model = Quiz
        fields = (
            'url',
            'name',
            'id',
            'total_question',
            'time',
            'subject',
            'difficulty',
            'total_marks',
        )
    
    def get_total_marks(self,object):
        marks = object.total_question*2
        return marks
    
    def get_url(self,obj): 
        request = self.context.get('request')
        if request is None:
            return None
        url = reverse("quiz-detail",kwargs={"pk":obj.id})
        return url
        
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            # 'question',
            'option',
        )
    # def to_representation(self, instance): 
    #     representation = super().to_representation(instance)
    #     representation['question'] = instance.question.question
    #     return representation

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            # 'question',
            'answer',
        )

class CurrentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentAnswer
        fields =(
            'id',
            'question',
            'answer',
        )


class AllQuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True,read_only=True)
    answer = AnswerSerializer(many=True,read_only=True)
    current_answer = CurrentAnswerSerializer(many=True,read_only=True)
    class Meta:
        model = Question
        fields =(
            'id',
            'name',
            'question',
            'total_options',
            'question_type',
            'options',
            'answer',
            'current_answer',
        )

    def to_representation(self, instance): 
        representation = super().to_representation(instance)
        representation['name'] = instance.name.name
        return representation


