import json
from app.parser import extract_failures
from app.llm import analyze_error
from app.report import generate_report


def analyze_with_retry(error_text, retries=3):
    for _ in range(retries):
        result = analyze_error(error_text)
        try:
            data = json.loads(result)
            if all(k in data for k in ["root_cause", "fix", "severity"]):
                return data
        except:
            continue

    return {
        "root_cause": "Unable to analyze",
        "fix": "Manual investigation needed",
        "severity": "Unknown"
    }


def run_pipeline(xml_file):
    failures = extract_failures(xml_file)

    results = []

    for f in failures:
        print(f"Analyzing: {f['test_name']}")

        analysis = analyze_with_retry(f["error"])

        results.append({
            "test_name": f["test_name"],
            "error": f["error"],
            "analysis": analysis
        })

    generate_report(results)

