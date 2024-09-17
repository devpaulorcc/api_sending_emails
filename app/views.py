from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.email_service import send_email

# Create your views here.

@api_view(['GET'])
def index(request):
    if request.method == "GET":
        return Response("200")
    
@api_view(['GET'])
def send(request, sender, password_app, recipient, subject, message):
    if request.method == "GET":
        message_text = message
        send_email(sender, password_app, recipient, subject, message_text)
        
        return Response("Envio concluído.")
    