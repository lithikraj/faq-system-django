from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache

class FAQList(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return Response(cached_data)
        
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'lang': lang})
        data = serializer.data
        cache.set(cache_key, data, timeout=60 * 15)  # 15 minutes cache timeout
        return Response(data)