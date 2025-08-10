# src/api/app.py
from fastapi import FastAPI, HTTPException
from enviroguard.monitor import detect_hazards, assess_risk

app = FastAPI(title='EnviroGuard AI - Demo API')

@app.get('/monitor')
def monitor(region: str = 'DemoRegion'):
    try:
        dets = detect_hazards('data/sample_image.tif')
        risks = [assess_risk(d) for d in dets]
        return {'status':'ok','detections':dets,'risks':risks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
