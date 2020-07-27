from django.shortcuts import render
from .serializers import ArticleSerializer, PersonDataSerializer, HyperSerializer
from .models import Article
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
import pyodbc
import json


# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticelViewSets(viewsets.ModelViewSet):
    serializer_class = HyperSerializer
    queryset = Article.objects.all()

# class ArticelViewSets(viewsets.ModelViewSet):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()

class GenericAPIView(generics.ListAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id'
    #authentication_classes = [SessionAuthentication, BasicAuthentication] # If admin login
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

class ArticleAPIView(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)

        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# #@csrf_exempt
# @api_view(['GET', 'POST', 'DELETE'])
#
# def article_list(request):   # , format=None
#
#     if request.method == 'GET':
#         articles = Article.objects.all().order_by('title')
#         serializer = ArticleSerializer(articles, many=True)
#        # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         #data = JSONParser().parse(request)
#         #serializer = ArticleSerializer(data=data)
#         serializer = ArticleSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             #return JsonResponse(serializer.data, status=201)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         #return JsonResponse(serializer.errors, status=400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method =='DELETE':
#         articles = Article.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt

def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all().order_by('title')
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method =='DELETE':
        articles = Article.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'Delete'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'Delete'])
def Json(data):
    data = json.loads(data.body)

    return Response(data)


def connectDatabase(request):

    #def get(self, request):

    cnxn = pyodbc.connect("Driver={SQL Server};"
                          "Server=DESKTOP-4ST4IQP;"
                          "Database=B2B;"
                          "Trusted_Connection=yes;")

    cursor = cnxn.cursor()
    cursor.execute('SELECT t1,t2 FROM UVM012 where t2=?;',
                       ('Admin')
                       )

    result = cursor.fetchall()
    content = {
    "object": result
    }
    return render(request, 'test.html', content)

class GetUserData(APIView):

    def get(self, request):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                          "Server=DESKTOP-4ST4IQP;"
                          "Database=B2B;"
                          "Trusted_Connection=yes;")

        ti
        cursor = cnxn.cursor()
        # cursor.execute('SELECT * FROM UVM012 where t2=?;',
        #                ('Admin')
        #                )

        cursor.execute("SELECT syskey,createdDate,t1,t2,t5 FROM UVM012")

        result = cursor.fetchall()
        serializer = PersonDataSerializer(result, many=True)
        return Response(serializer.data)


