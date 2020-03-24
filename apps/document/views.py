from rest_framework import generics
# from rest_framework import mixins
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from document.models import Document
from document.serializers import DocumentSerializer, UserSerializer

class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    
class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer