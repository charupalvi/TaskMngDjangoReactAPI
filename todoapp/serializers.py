from todoapp.models import TodoListModel
from rest_framework import serializers

class TodoListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoListModel
        fields = ['id','title','description','is_completed']