# send_otel_log.py
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
import logging

# ... (Configuração OTel) ...

logger_provider = LoggerProvider()
set_logger_provider(logger_provider)

# OTLP Collector porta 4318
otlp_exporter = OTLPLogExporter(endpoint="http://localhost:4318/v1/logs")
logger_provider.add_log_record_processor(BatchLogRecordProcessor(otlp_exporter))

handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
logging.getLogger().addHandler(handler)

app_logger = logging.getLogger("payment_service_v3")
app_logger.setLevel(logging.INFO)

print("--- LogSage OTel Simulation: Sending logs to Collector (4318) ---")
app_logger.critical("Log Bruto 1: CRITICAL: Ocorreu um erro 500 na rota /checkout.")
app_logger.warning("Log Bruto 2: Tentativa de login suspeita detectada no IP 203.0.113.45.")

# CRUCIAL: Força o envio do lote de logs
logger_provider.force_flush() 

logger_provider.shutdown() 
print("Logs OTLP enviados.")