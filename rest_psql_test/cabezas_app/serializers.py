from rest_framework import serializers
from .models import Pix

class CabezasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pix 
        fields = ['pk']
        st = ['number_'+str(x) for x in range(256)]
        fields.extend(st)
        fields.extend(['subject', 'slice'])
        #fields = ['pk', '0-255', 'subject', 'slice']
