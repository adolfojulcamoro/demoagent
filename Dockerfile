# Agente de prueba mínimo: responde en el puerto 80 (agent_port de runtime_agentes).
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
ARG GIT_SHA=desconocido
ENV GIT_SHA=$GIT_SHA
EXPOSE 80
CMD ["python", "app.py"]
