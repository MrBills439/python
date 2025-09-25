import requests
from datetime import datetime

def get_aws_status():
    url = "https://status.aws.amazon.com/data.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "✅ AWS status page reachable"
        else:
            return "⚠️ AWS status page returned non-200"
    except Exception as e:
        return f"❌ Error: {str(e)}"
def write_report(content):
    date = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"reports/{date}.md"
    with open(filename, "w") as f:
        f.write(f"# Cloud Status Report - {date}\n\n")
        f.write(content)
