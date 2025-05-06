from .models import User , GlucoseTableLvels
from rest_framework import serializers
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = "__all__"


class GlucoseLevelsSerializer(serializers.ModelSerializer):
    class Meta :
        model = GlucoseTableLvels
        fields ="__all__"
    
        