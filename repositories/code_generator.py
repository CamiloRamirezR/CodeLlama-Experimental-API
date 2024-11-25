from models import CodeGeneration


class CodeGenerationRepository:
    def create_prompt(self, prompt: str) -> CodeGeneration:
        raise NotImplementedError  # pragma: no cover

    def update_result(self, code_generation_id: str, result: str) -> CodeGeneration:
        raise NotImplementedError  # pragma: no cover

    def get_by_id(self, code_generation_id: str) -> CodeGeneration:
        raise NotImplementedError  # pragma: no cover
