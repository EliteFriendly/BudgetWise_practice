from pydantic import BaseModel, Field




#Thing which uses to send info in ChequeInfo
class ReqImgLLM(BaseModel):
    userToken: str = Field(description="Token?")
    userID: int = Field(default=...)
    qrInfo: str = Field(description="Info/code getted by scanning cheque")



#Thing which uses to send info in auto_fill_LLM, especially items from cheque
class ReqProductsLLM(BaseModel):
    userToken: str = Field(default=...,description="Access token")
    userID: int = Field(default=...)
    items: list = [
        {"name": str,  
        "productType": str,
        "quantity": int,
        "price": float,
        "sum": float}
        ]