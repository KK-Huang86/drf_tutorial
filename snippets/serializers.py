from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
        owner = serializers.ReadOnlyField(source='owner.username')

# ModelSerializer已有默認的 create 與 update的行為，除非有特殊邏輯與型態

    # def create(self, validated_data):
    #   #透過驗證實現的實例
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #   #更新實現的實例
    #     instance.title = validated_data.get('title', instance.title) #若前端沒有資料，則使用原來的instance.title
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance