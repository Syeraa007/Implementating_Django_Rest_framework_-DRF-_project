from rest_framework import serializers

# create your serializers here.
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    # New Error handling and validation
    def validate_title(self, value):
        if 'bad_word' in value:
            raise serializers.ValidationError('Bad word not allowed.')
        return value