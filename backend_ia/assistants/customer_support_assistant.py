import requests
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.memory import ConversationBufferMemory
from products.models import Product
from orders.models import Order
from stock.models import Stock
from ..core.langchain_setup import LangChainSetup
from .prompts.prompt_loader import load_prompt

class CustomerSupportAssistant:    

    def __init__(self):
        langchain_setup = LangChainSetup()
        self.llm = langchain_setup.get_model()
        self.vector_db = langchain_setup.get_vector_db()

        # Configurar la memoria de conversación
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Usar una implementación concreta de RetrievalQA con memoria
        self.chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vector_db.as_retriever(),
            memory=self.memory
        )

        # Cargar el prompt que ahora usa "user_input" y "chat_history"
        template_text = load_prompt("customer_support_prompt.txt")
        self.prompt = PromptTemplate(
            input_variables=["user_input", "chat_history"],
            template=template_text
        )

        # Cadena LLM que utiliza el prompt y la memoria
        self.llm_chain = LLMChain(llm=self.llm, prompt=self.prompt, memory=self.memory)

    def get_order_status(self, order_id):
        order = Order.objects.filter(id=order_id).first()
        return order.to_dict() if order else "No se encontró información sobre el pedido."
    
    def get_product_info(self, product_name):
        product = Product.objects.filter(name__icontains=product_name).first()
        return product.to_dict() if product else "No se encontró información sobre ese producto."

    def get_store_summary(self):
        products = Product.objects.all()
        if products:
            product_list = [p.name for p in products]
            return "Productos disponibles: " + ", ".join(product_list)
        else:
            return "Actualmente no tenemos productos disponibles."

    def get_response(self, question):
        # Obtener el historial de conversación
        chat_history = self.memory.load_memory_variables({}).get("chat_history", "")

        # Si la pregunta solicita información sobre lo que se vende, inyectar el resumen de productos
        if "lo que vendes" in question.lower() or "infórmame sobre lo que vendes" in question.lower():
            store_summary = self.get_store_summary()
            # Combinar la pregunta y el resumen en una sola variable
            user_input = f"{question}\n{store_summary}"
        else:
            user_input = question
        
        # Ejecutar la cadena LLM usando las dos variables: user_input y chat_history
        inputs = {
            "user_input": user_input,
            "chat_history": chat_history,
        }
        answer = self.llm_chain.run(inputs)
        # Si no se obtiene una respuesta válida, reintenta
        if not answer or answer.strip() == "Lo siento, no encontré una respuesta.":
            answer = self.llm_chain.run(inputs)
        return answer