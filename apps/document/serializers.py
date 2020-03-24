from rest_framework import serializers
from document.models import Document, SOURCE_CHOICES
from django.contrib.auth.models import User

class JSONSerializerField(serializers.Field):
    def to_internal_value(self, data):
        return data
    def to_representation(self, value):
        return value

class DocumentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField(required=True, max_length=100)
    source_type = serializers.ChoiceField(choices=SOURCE_CHOICES, default='WEB')
    source_id = serializers.CharField(required=False, max_length=50)
    input_meta_data = JSONSerializerField()
    owner = serializers.ReadOnlyField(source='export.username')

    def create(self, validated_data):
        return Document.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.source_type = validated_data.get('source_type', instance.source_type)
        instance.source_id = validated_data.get('source_id', instance.source_id)
        instance.input_meta_data = validated_data.get('input_meta_data', instance.input_meta_data)
        instance.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['owner'] = UserSerializer(instance.owner).data
        return response

    def clean_json(self, obj):
        return obj.input_meta_data

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']