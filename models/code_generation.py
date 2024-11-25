# mypy: ignore-errors
from db import db
from .status import StatusEnum


class CodeGeneration(db.Model):
    __tablename__ = "code_generation"

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    result = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(StatusEnum), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now(),
        onupdate=db.func.now(),
    )
