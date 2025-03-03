from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..assistants.customer_support_assistant import CustomerSupportAssistant
from ..assistants.product_manager_assistant import ProductManagerAssistant
from ..assistants.content_marketing_assistnat import ContentMarketingAssistant

from ..core.database import search_faq
from ..models.faq import FAQ
from .serializers import FAQSerializer

class CustomerSupportView(APIView):
    """Endpoint para el asistente de atención al cliente"""
    def post(self, request):
        data = request.data
        question = data.get("question")
                
        if not question:
            return Response({
                "error": "No se proporcionó una pregunta"},
                status=status.HTTP_400_BAD_REQUEST
            )

        assistant = CustomerSupportAssistant()
        ai_response = assistant.get_response(question)

        faq_obj, created = FAQ.objects.get_or_create(
            question=question,
            defaults={"answer": [ai_response]}
            )
        if not created:
            responses = faq_obj.answer if isinstance(faq_obj.answer, list) else [faq_obj.answer]
            responses.append(ai_response)
            faq_obj.answer = responses
            faq_obj.save()

        return Response({"answer": ai_response}, status=status.HTTP_200_OK)
    
class FAQListView(APIView):
    """Endpoint para listar y agregar FAQs"""

    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductManagerView(APIView):
    def post(self, request):
        command = request.data.get("command")
        product_name = request.data.get("product_name")
        assistant = ProductManagerAssistant()

        if not command:
            return Response({"error":"No se proporcionó un comando"}, status=status.HTTP_400_BAD_REQUEST)
        
        if "precio" in command:
            try:
                percentage = float(command.split()[-1].replace("%", ""))
                response = assistant.adjust_prices(percentage)
            except ValueError:
                response = {"error": "Formato de comando incorrecto. Ejemplo: 'Aumentar precio 10%'"}
        elif "insight" in command and product_name:
            response = {"insight": assistant.generate_product_insights(product_name)}
        else:
            response = {"error": "Comando no reconocido"}
        return Response(response, status=status.HTTP_200_OK)
    
class ContentMarketingView(APIView):
    def post(self, request):
        data = request.data
        product_name = data.get("product_name")
        category = data.get("category")

        if not product_name or not category:
            return Response(
                {"error": "Se requieren 'product_name' y 'category'"},
                status=status.HTTP_400_BAD_REQUEST
            )
        assistant = ContentMarketingAssistant()
        response = assistant.generate_description(product_name, category)
        return Response({"description": response}, status=status.HTTP_200_OK)
