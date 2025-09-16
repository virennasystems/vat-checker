# app/api.py
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from app.core.vies import validate_vat
from app.core.pdf import build_report_pdf

app = FastAPI(title="VAT Checker")

class VatRequest(BaseModel):
    country: str
    number: str

@app.post("/validate")
async def validate(req: VatRequest):
    result = await validate_vat(req.country, req.number)  # wraps VIES / provider
    return result

@app.post("/batch")
async def batch(file: UploadFile):
    # parse CSV -> enqueue jobs -> return job_id
    ...

@app.get("/report/{job_id}")
def report(job_id: str):
    pdf_bytes = build_report_pdf(job_id)
    return Response(pdf_bytes, media_type="application/pdf")
