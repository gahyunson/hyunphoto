from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.id') # need to recheck
    
    class Meta:
        model = Contact
        # fields = ('user', 'message')