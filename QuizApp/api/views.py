from rest_framework.decorators import APIView
from .models import Quiz,Question,Option,CurrentAnswer
from .serializers import QuizSerializer,AllQuestionSerializer,OptionSerializer,CurrentAnswerSerializer
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import MyRateThrottling
import random
class CustomPagination(PageNumberPagination):
    page_size = 1 # number of records to return per page
    page_size_query_param = 'page_size' 
    max_page_size = 1 # maximum number of records that can be returned in a page
    

class QuizHome(APIView):
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    def get(self,request,*args,**kwargs):
        data = Quiz.objects.all()
        serializer = QuizSerializer(data,context={'request': request},many=True)
        return Response(serializer.data)
    
    def post(self,request,*args, **kwargs):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    


class QuizView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        data = Question.objects.filter(name=pk)
        curr_ans_data = CurrentAnswer.objects.filter(question__in = data)
        excluded_data = Question.objects.filter(name=pk).exclude(id__in=curr_ans_data.values('question')).order_by('?')

        paginated_queryset = CustomPagination().paginate_queryset(excluded_data, request)
        serializer = AllQuestionSerializer(paginated_queryset,many=True)
        # serializer = AllQuestionSerializer(data,many=True)
        return Response(serializer.data)
    
    def patch(self,request,*args, **kwargs):
        pk = self.kwargs.get('pk')
        data1 = Quiz.objects.get(pk=pk)
        serializer = QuizSerializer(data1,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=400,data = serializer.errors)
    
    def post(self,request,*args, **kwargs):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  

class OptionsView(APIView):
    def get(self,request,*args,**kwargs):
        data = Option.objects.all().order_by('?')
        serializer = OptionSerializer(data,context={'request': request},many=True)
        return Response(serializer.data)
    

class CurrentAnswerView(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        data = CurrentAnswer.objects.filter(id=pk)
        serializer = CurrentAnswerSerializer(data)
        return Response(serializer.data)
    
    def post(self,request,*args, **kwargs):
        serializer = CurrentAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request, *args, **kwargs):
        delete_all = request.headers.get('delete')
        if delete_all:
            data = CurrentAnswer.objects.all()
            data.delete()
            return Response()
        pk = kwargs.get('pk')
        data = CurrentAnswer.objects.filter(id=pk)
        data.delete()
        return Response()
    
class AllCurrentAnswerView(APIView):

    def get(self,request,*args,**kwargs):
        data = CurrentAnswer.objects.all()
        serializer = CurrentAnswerSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args, **kwargs):
        serializer = CurrentAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)