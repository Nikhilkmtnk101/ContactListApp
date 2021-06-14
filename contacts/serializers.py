from rest_framework import serializers
from .models import Contacts


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contacts
        fields=['id','first_name','last_name','country_code','phone_number','email','contact_picture','is_favourite']

