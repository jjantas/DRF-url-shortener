import string
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404, redirect

def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

class CreateShortURL(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['original_url']

            # check if shortcut already exists, if yes then do not create new
            existing = ShortURL.objects.filter(original_url=original_url).first()
            if existing:
                return Response({
                    "short_url": f"http://localhost:8000/shrt/{existing.short_code}/"
                }, status=status.HTTP_200_OK)
            
            
            code = generate_code()
            while ShortURL.objects.filter(short_code = code).exists():
                code = generate_code()
            
            shorturl = ShortURL.objects.create(
                original_url=original_url,
                short_code=code)
            
            return Response(
                {"short_url": f"http://localhost:8000/shrt/{shorturl.short_code}/"},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RedirectShortURL(APIView):
    def get(self, request, code):
        short_url = get_object_or_404(ShortURL, short_code=code)
        return redirect(short_url.original_url)