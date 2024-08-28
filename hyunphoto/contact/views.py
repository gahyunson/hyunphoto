from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from . import serializers


class ContactView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request, 'contact.html')
    
    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = serializers.ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            context = {
                'data': serializer.data
            }
            return redirect('/')
        context = {
            'data': 'not found'
        }
        return Response(context, status=400)
    
contactview = ContactView.as_view()