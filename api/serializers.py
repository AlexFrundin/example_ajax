from rest_framework import serializers
from first.models import Comment
class CommentSerializers(serializers.Serializer):
    comment = serializers.CharField(style={'base_template':'textarea.html'})
    quantity = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        #validated_data - словарь данных, который прошел проверку -
        # во views.py (вызов is_valid)
        return Comment.objects.create(**validated_data)
