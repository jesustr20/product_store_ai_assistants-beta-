import requests
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from products.models import Product
from stock.models import Stock
from ..core.langchain_setup import LangChainSetup
from .prompts.prompt_loader import load_prompt

class ProductManagerAssistant:
    #PRODUCT_STORE_API = "http://127.0.0.1:8000/api/products/"

    def __init__(self):
        langchain_setup = LangChainSetup()
        self.llm = langchain_setup.get_model()

        template_text = load_prompt("product_manager_prompt.txt")
        self.template = PromptTemplate(
            input_variables=["product_name"],
            template=template_text
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.template)


    def adjust_prices(self, percentaje):
        products = Product.objects.all()
        for product in products:
            product.price *=  (1 + percentaje / 100)
            product.save()
        return {"status": "Prices updated"}

    def update_stock(self, product_id, amount):
        stock = Stock.objects.filter(product_id=product_id).first()
        if stock:
            stock.amount += amount
            stock.save()
            return {"status": "Stock updated"}
        return {"error": "Stock not found"}
    
    def generate_product_insights(self, product_name):
        return self.chain.run(product_name)