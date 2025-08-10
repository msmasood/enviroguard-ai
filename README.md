# EnviroGuard AI — Autonomous Environmental Monitoring & Response (Demo)

**Overview**
EnviroGuard AI monitors satellite imagery and IoT sensor data to detect environmental hazards like deforestation, flooding, and pollution. This demo repository includes a runnable pipeline that performs:
- Sample satellite image segmentation (using a lightweight pre-trained model or placeholder)
- Risk scoring & prioritization
- Action workflow simulation (alerts / webhook stub)
- Local FAISS-based RAG for historical incidents/context

**What's included**
- `src/` : core modules (imagery processing, detection, risk assessment, rag, api)
- `notebooks/` : demo notebook for image analysis and monitoring flow
- `data/` : small sample raster (placeholder), sensor CSVs, sample docs for RAG
- `docker/` : Dockerfile + docker-compose for local run
- `requirements.txt`, `LICENSE`, `.gitignore`
- `.github/workflows/ci.yml` : basic CI

**Demo notes**
- The image processing uses a lightweight torchvision model stub; to run full deep learning inference, ensure PyTorch is installed and use appropriate GPU drivers.
- No external API keys required for the demo; FAISS is used locally for RAG context.

---

## Quickstart (Local)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run monitoring demo
python src/enviroguard/monitor_demo.py

# Start API
uvicorn src.api.app:app --reload --port 8200
# then open http://127.0.0.1:8200/monitor?region=DemoRegion
```

## Docker (optional)
```bash
cd docker
docker-compose up --build
# then visit http://localhost:8200/monitor?region=DemoRegion
```
