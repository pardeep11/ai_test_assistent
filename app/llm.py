import ollama


def analyze_error(error_text, model="phi3"):
    prompt = f"""
    Analyze this API/Test failure:
    {error_text}

    Return STRICT JSON:
    {{
        "root_cause": "...",
        "fix": "...",
        "severity": "Low/Medium/High"
    }}
    """

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

