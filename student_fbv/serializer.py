from rest_framework import serializers
from django.contrib.auth.models import User
from student_fbv.models import Student


class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = ['id', 'name', 'score', 'owner']


class UserSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'students']
