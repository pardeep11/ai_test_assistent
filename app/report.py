from datetime import datetime


def generate_report(results, output_file="report.html"):
    html = f"""
    <html>
    <head>
        <title>AI Test Failure Report</title>
    </head>
    <body>
        <h2>AI Test Failure Analysis Report</h2>
        <p>Generated: {datetime.now()}</p>
        <table border="1">
            <tr>
                <th>Test Name</th>
                <th>Error</th>
                <th>Root Cause</th>
                <th>Fix</th>
                <th>Severity</th>
            </tr>
    """

    for r in results:
        html += f"""
        <tr>
            <td>{r['test_name']}</td>
            <td>{r['error']}</td>
            <td>{r['analysis']['root_cause']}</td>
            <td>{r['analysis']['fix']}</td>
            <td>{r['analysis']['severity']}</td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    with open(output_file, "w") as f:
        f.write(html)

    print(f"Report generated: {output_file}")

