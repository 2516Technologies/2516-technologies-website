import requests
from supabase import create_client

# Your Supabase credentials
SUPABASE_URL = "https://kgfmwlpqyxrvlitzjrml.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtnZm13bHBxeXhydmxpdHpqcm1sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njg4NDQ3NTMsImV4cCI6MjA4NDQyMDc1M30.MR0zZeRdglsSrbK8jxmZL6fx79Ca4WEangbr7OARbMU"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def pull_nonprofits():
    print("Pulling nonprofits for California...")
    
    url = "https://projects.propublica.org/nonprofits/api/v2/search.json"
    page = 0
    total_inserted = 0
    
    while True:
        params = {
            "state[id]": "CA",
            "per_page": 100,
            "page": page
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"API error: {response.status_code}")
            break
            
        data = response.json()
        organizations = data.get("organizations", [])
        
        if not organizations:
            print("No more organizations found")
            break
            
        print(f"Page {page}: Found {len(organizations)} organizations")
        
        for org in organizations:
            record = {
                "ein": str(org.get("ein", "")),
                "name": org.get("name", ""),
                "city": org.get("city", ""),
                "state": org.get("state", ""),
                "ntee_code": org.get("ntee_code", ""),
                "subsection_code": str(org.get("subsection_code", "")),
                "income_amount": org.get("income_amount", 0),
                "asset_amount": org.get("asset_amount", 0),
                "revenue_amount": org.get("revenue_amount", 0)
            }
            
            try:
                supabase.table("propublica_nonprofits").upsert(record, on_conflict="ein").execute()
                total_inserted += 1
            except Exception as e:
                print(f"Error inserting {record['name']}: {e}")
        
        print(f"Total inserted so far: {total_inserted}")
        page += 1
        
        if page >= 40:
            print("Reached 40 page limit — stopping")
            break
    
    print(f"Done! Total records inserted: {total_inserted}")

pull_nonprofits()
