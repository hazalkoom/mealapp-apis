from rest_framework import serializers

class EmailVerSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()