from rest_framework import serializers
from .models import Article, PersonData
#from .Userdata import
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email', 'date']

class HyperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['url', 'title', 'author', 'email', 'date']

class PersonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonData
        fields = [
            'syskey',
            'createdDate',
            't1',
            't2',
            't5'
        ]