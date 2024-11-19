from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
import time
import asyncpg
import os

# Função para obter a conexão com o banco de dados PostgreSQL
async def get_database():
    DATABASE_URL = os.environ.get("PGURL", "postgres://postgres:postgres@db:5432/jogos") 
    return await asyncpg.connect(DATABASE_URL)

# Inicializar a aplicação FastAPI
app = FastAPI()

# Modelo para adicionar novas tarefas
class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    materia: str
    data_conclusao: str
    progresso: str
    dificuldade: int

class TarefaBase(BaseModel):
    titulo: str
    materia: str
    data_conclusao: str
    progresso: str
    dificuldade: int