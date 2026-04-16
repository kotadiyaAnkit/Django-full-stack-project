# serializers.py
from rest_framework import serializers
# from .models import Member
from django.core.validators import RegexValidator


class Member(serializers.ModelSerializer):
  
    firstname = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
#   email = serializers.EmailField(null=False, regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')   
    email = serializers.CharField(
        validators=[RegexValidator(
            regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Enter a valid email address.',
        )]
    )

    

# class MemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member
#         fields = ['firstname', 'lastname', 'email']  

#     def validate_email(self, value):
#         if not value.endswith('@example.com'):
#             raise serializers.ValidationError("Email must end with @example.com")
#         return value
