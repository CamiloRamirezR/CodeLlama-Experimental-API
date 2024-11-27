from uuid import uuid4
from repositories import CodeGenerationRepository
from models import CodeGeneration, StatusEnum
from db import db

class CodeGenerator(CodeGenerationRepository):
    def __init__(self) -> None:
        self.db = db

    def create_prompt(self, prompt: str) -> CodeGeneration:
        code_generation = CodeGeneration(
            id=str(uuid4()),
            prompt=prompt,
            result="",
            status=StatusEnum.PENDING.value,
        )
        self.db.session.add(code_generation)
        self.db.session.commit()
        return code_generation

    def update_result(self, code_generation_id: str, result: str) -> CodeGeneration:
        code_generation = self.get_by_id(code_generation_id)
        code_generation.result = result
        code_generation.status = StatusEnum.SUCCESS.value
        self.db.session.commit()
        return code_generation

    def get_by_id(self, code_generation_id: str) -> CodeGeneration:
        return CodeGeneration.query.get(code_generation_id)

    def get_all(self) -> list[CodeGeneration]:
        return CodeGeneration.query.all()

    def delete_all(self) -> None:
        CodeGeneration.query(CodeGeneration).delete()
        self.db.session.commit()