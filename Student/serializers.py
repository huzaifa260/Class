from rest_framework import serializers
from .models import Student, user


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    # it is use to serialize id field

    class Meta:
        model = Student
        fields = "__all__"


#  Created serializers for Student Model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = "__all__"
