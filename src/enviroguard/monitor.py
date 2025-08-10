# src/enviroguard/monitor.py
import os, random
from typing import List, Dict

def detect_hazards(image_path: str):
    # Placeholder: simulate detections with random choices
    sample = [
        {'type':'deforestation','bbox':[0,0,100,100],'confidence':0.92},
        {'type':'flood','bbox':[50,50,150,150],'confidence':0.78}
    ]
    return sample

def assess_risk(detection: Dict) -> Dict:
    # Simple risk scoring by type and confidence
    base = {'deforestation': 0.7, 'flood': 0.9, 'pollution': 0.6}
    score = base.get(detection['type'],0.5) * detection.get('confidence',0.5)
    level = 'High' if score>0.75 else 'Medium' if score>0.55 else 'Low'
    return {'type':detection['type'],'score':round(score,2),'level':level}
