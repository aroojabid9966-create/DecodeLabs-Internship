from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = "__all__"
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Age cannot be negative."
            )
        return value
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Name cannot be empty"
            )
        return value
    