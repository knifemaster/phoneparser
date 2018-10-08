from rest_framework import serializers
from phones.models import Phone


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ('id','model_name', 'url', 'price', 'description')
 