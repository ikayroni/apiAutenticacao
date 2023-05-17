from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Estrutura de dados simulando um banco de dados
users = {
    "usuario": "senha"
}

# Model para dados de login
class Login(BaseModel):
    username: str
    password: str

# Rota de validação de login
@app.post("/login")
def login(login: Login):
    username = login.username
    password = login.password

    # Verifica as credenciais do usuário
    if username in users and users[username] == password:
        return {"message": "Login bem-sucedido"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

print("Iniciando o servidor FastAPI na porta 8080...")
uvicorn.run(app, host="0.0.0.0", port=8080)
