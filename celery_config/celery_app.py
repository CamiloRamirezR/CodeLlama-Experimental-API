from celery import Celery
from environment import REDIS_WORKER

# Configuración de Celery
celery_app = Celery(
    "code_generation",
    broker=f"{REDIS_WORKER}",  # Dirección del broker Redis
    backend=f"{REDIS_WORKER}",  # Backend para resultados
)

# Configuración adicional
celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)
