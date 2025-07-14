from fastapi import FastAPI, UploadFile, File
from cheque_info.uploadIMGRoute import uploadIMG
from fill_llm.fillLLMRoute import  productsLLM
from cheque_info.ChequeInfo import ChequeInfo

app = FastAPI()
app.include_router(uploadIMG)
app.include_router(productsLLM)


@app.get("/")
def root():
    return {"Main page"}



    

