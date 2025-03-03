import requests
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from products.models import Product
from orders.models import Order
from stock.models import Stock
from ..core.langchain_setup import LangChainSetup
from .prompts.prompt_loader import load_prompt

class ContentMarketingAssistant:
    #PRODUCT_STORE_API = "http://127.0.0.1:8000/api/products/"

    def __init__(self):
        langchain_setup = LangChainSetup()
        self.llm = langchain_setup.get_model()

        template_text = load_prompt("content_marketing_prompt.txt")
        template = PromptTemplate(
            input_variables=["product_name", "category", "details"], 
            template=template_text)
        
        self.chain = LLMChain(llm=self.llm, prompt=template)

    def get_product_details(self, product_name):
        #response = requests.get(self.PRODUCT_STORE_API, params={"name": product_name})
        product = Product.objects.filter(name=product_name).first()
        #if response.status_code == 200:
        #    products = response.json()
        #    return products[0] if products else None
        return product if product else None
    
    def generate_description(self, product_name, category):
        #product_details = self.get_product_details(product_name)
        product = self.get_product_details(product_name)
        details = product.description if product else "No disponible"
        return self.chain.run({"product_name": product_name, "category": category, "details": details})