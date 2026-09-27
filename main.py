from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone

app = FastAPI(
    title="Industrial Edge-to-Cloud API",
    description="POC API for receiving production data from Site 01",
    version="1.0"
)


class ProductionData(BaseModel):
    site_id: str
    tag: str
    value: float


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Industrial Edge-to-Cloud API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/api/production")
def receive_production(data: ProductionData):

    timestamp = datetime.now(timezone.utc).isoformat()

    print(
        f"[{timestamp}] "
        f"{data.site_id} | "
        f"{data.tag} = {data.value}"
    )

    return {
        "status": "received",
        "site_id": data.site_id,
        "tag": data.tag,
        "value": data.value,
        "timestamp": timestamp
    }
