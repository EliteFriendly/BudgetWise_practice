from fastapi import FastAPI, UploadFile, File
from cheque_Info.upload_IMG_router import uploadIMG
from fill_Llm.fill_llm_router import productsLLM

app = FastAPI()
app.include_router(uploadIMG)
app.include_router(productsLLM)


@app.get("/")
def root():
    return {"Main page"}



    

