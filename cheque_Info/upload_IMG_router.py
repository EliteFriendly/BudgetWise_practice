from fastapi import UploadFile, File, APIRouter
from cheque_Info.сheque_info import ChequeInfo
import os




uploadIMG = APIRouter(prefix = "/api/qr_put",tags=["Send this into a API wich take items from cheque"])
QRreader = ChequeInfo()


@uploadIMG.post("/uploadIMG")
def  sendToChequeInfo(file:UploadFile):
    #Save file
    file_path = f"{file.filename}"
    with open(file_path, "wb") as tmpF:
        tmpF.write(file.file.read())
    
    #Send information from cheque to LLM
    QRreader.setQRImage(fileName=file_path)
    os.remove(file_path)
    return {"message": "File read successfully"}
    

@uploadIMG.get("/showProductsList")
def getProductList():
    return QRreader.getDistProducts()

