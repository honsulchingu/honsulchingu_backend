# Kernel base(Python 3.12.7)
# cmd pip install fastapi
# cmd pip install uvicorn
# cmd cd honsulchingu_fast_api
# cmd uvicorn Fast_API_Server_Runner:app --host 0.0.0.0 --port 8000 --reload
# EC2 보안 그룹 8000 포트 개방 (http://퍼블릭 IP 접속:8000)
# http://127.0.0.1:8000 (접속)
# http://127.0.0.1:8000/docs (문서)
# http://127.0.0.1:8000/openapi.json (성능)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# FastAPI 앱 생성
app = FastAPI()

# 요청 데이터 형식을 정의할 Pydantic 모델 (Pydantic은 Python 데이터 검증 및 설정 관리 라이브러리)
class InputData(BaseModel):
    text: str

# http://. . . . :/ 경로
@app.get("/")
def home():
    return {"message": "FastAPI 서버가 정상 작동 중입니다."}

# http://. . . . :/chat 경로
@app.post("/chat")
def chat(data: InputData):
    user_input = data.text
    if not user_input:
        raise HTTPException(status_code=400, detail="텍스트를 입력하세요.")
    
    response = user_input + "에 대한 응답입니다."
    return {"response": response}

# http://. . . . :/ai 경로
@app.post("/ai")
def ai(data: InputData):
    user_input = data.text
    if not user_input:
        raise HTTPException(status_code=400, detail="텍스트를 입력하세요.")
    
    response = user_input + "에 대한 AI응답입니다."
    return {"response": response}