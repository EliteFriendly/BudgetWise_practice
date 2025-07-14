from fastapi import APIRouter
from fill_Llm.auto_fill_llm import AutoFillLLM
from input_Protect.validation_input import ReqProductsLLM



productsLLM = APIRouter(prefix = "/api/autofill_llm",tags=["Send this into a AutoFillLLM"])
autoFillLLM = AutoFillLLM()


#Router
@productsLLM.post("/setCategory")
def sendToChequeInfo(reqProductsLLM: ReqProductsLLM):
    categories = autoFillLLM.getCategory(reqProductsLLM)
    return categories


@productsLLM.post("/setProductsTypes")
def sendToChequeInfo(reqProductsLLM: ReqProductsLLM):
    productType = autoFillLLM.getProductType(reqProductsLLM)
    return productType



