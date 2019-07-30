# Rest framework imports
from rest_framework import serializers

# Application imports
# Base imports

# Model imports
from users.models import User


class CommonSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @staticmethod
    def get_common_exclude_fields():
        return [
            "is_active",
            "created_at",
            "modified_at",
            "deleted_at",
        ]


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar',
            'is_active',
            'created_at'
        )