# log_processor.py
from fastapi import FastAPI
import datetime
import requests
import json
import pandas as pd 

app = FastAPI(title="LogSage Motor Inteligente - Processador")
# Porta 9200 do Elasticsearch
ELASTICSEARCH_URL = "http://localhost:9200/" 

@app.get("/processar-novos-logs")
def process_logs_pipeline():
    """ Simula a busca, o enriquecimento/ML e a reindexação dos logs. """
    
    # SIMULAÇÃO: Logs Brutos (Em produção, aqui haveria uma query no ES)
    log_bruto_1 = "CRITICAL: Ocorreu um erro 500 na rota /checkout. Latência > 5s."
    log_bruto_2 = "Tentativa de login suspeita detectada no IP 203.0.113.45."

    processed_logs = []
    def classify_log(message):
        # Lógica de ML simulada
        if "CRITICAL" in message or "erro 500" in message:
            return "HIGH", "OPERATIONS", True 
        if "login suspeita" in message:
            return "HIGH", "SECURITY", True 
        return "INFO", "GENERAL", False

    for raw_message in [log_bruto_1, log_bruto_2]:
        severity, log_type, is_anomaly = classify_log(raw_message)
        contexto_deploy = "Prod-A" if "checkout" in raw_message else "Auth-B" 
        
        processed_log = {
            "@timestamp": datetime.datetime.now().isoformat(),
            "raw_message": raw_message,
            "severity": severity,
            "log_type": log_type,
            "is_anomaly": is_anomaly,
            "deployment_context": contexto_deploy,
            "processed_by_logsage": True
        }
        processed_logs.append(processed_log)
        
    # RE-INDEXAÇÃO: Salva no índice enriquecido (logsage_enriched)
    index_name = "logsage_enriched"
    
    for log in processed_logs:
        requests.post(
            f"{ELASTICSEARCH_URL}{index_name}/_doc/",
            data=json.dumps(log),
            headers={'Content-Type': 'application/json'}
        )

    return {"status": "success", "count": len(processed_logs), "index": index_name}

@app.get("/")
def read_root():
    return {"Project": "LogSage MVP", "Motor_Status": "Ready"}