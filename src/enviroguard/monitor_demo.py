# src/enviroguard/monitor_demo.py
from enviroguard.monitor import detect_hazards, assess_risk
from enviroguard.rag import LocalRAG

def main():
    # run detection on sample image
    detections = detect_hazards('data/sample_image.tif')
    print('Detections:', detections)
    # assess risk for each detection
    risks = [assess_risk(d) for d in detections]
    print('Risk assessments:', risks)
    # query RAG for context
    rag = LocalRAG()
    ctx = rag.search('deforestation near river', top_k=2)
    print('Context snippets:', ctx)

if __name__ == '__main__':
    main()
