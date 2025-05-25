from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import os
app = FastAPI()
with open(os.path.join(os.path.dirname('E:/api/-vercel-python.json'),"q-vercel-python.json"), 'r') as f:
    marks = json.load(f)
@app.get("/api/")
async def get_marks(request: Request):
    names = request.query_params.get('names')
    result = [marks.get(name , None) for name in names]

    return JSONResponse(content=marks)