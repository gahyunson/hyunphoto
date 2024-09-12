from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from . import serializers
from .forms import ContactForm


class ContactView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'contact.html')
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.data)
        # data = request.data 
        if form.is_valid():
            print('form is valid!')
            serializer = serializers.ContactSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                print('serializer is valid!')
                serializer.save(user=request.user)
                context = {
                    'data': serializer.data
                }
                return redirect('/')
            else:
                print('not valid serializer')
        print('not valid forms')
        context = {
            'data': 'not found'
        }
        return Response(context, status=400)
    
contactview = ContactView.as_view()