import requests
import time
from supabase import create_client

SUPABASE_URL = "https://kgfmwlpqyxrvlitzjrml.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtnZm13bHBxeXhydmxpdHpqcm1sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njg4NDQ3NTMsImV4cCI6MjA4NDQyMDc1M30.MR0zZeRdglsSrbK8jxmZL6fx79Ca4WEangbr7OARbMU"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def update_financials():
    print("Fetching EINs from Supabase...")
    
    result = supabase.table("propublica_nonprofits").select("ein, name").execute()
    orgs = result.data
    print(f"Found {len(orgs)} organizations to update")
    
    for i, org in enumerate(orgs):
        ein = org["ein"]
        name = org["name"]
        
        url = f"https://projects.propublica.org/nonprofits/api/v2/organizations/{ein}.json"
        
        try:
            response = requests.get(url)
            
            if response.status_code != 200:
                print(f"Skipping {name}: HTTP {response.status_code}")
                continue
                
            data = response.json()
            org_data = data.get("organization", {})
            filings = data.get("filings_with_data", [])
            
            income = 0
            assets = 0
            revenue = 0
            
            if filings:
                latest = filings[0]
                income = latest.get("totrevenue", 0) or 0
                assets = latest.get("totassetsend", 0) or 0
                revenue = latest.get("totrevenue", 0) or 0
            
            update = {
                "income_amount": income,
                "asset_amount": assets,
                "revenue_amount": revenue
            }
            
            supabase.table("propublica_nonprofits").update(update).eq("ein", ein).execute()
            print(f"[{i+1}/{len(orgs)}] Updated: {name} — Assets: ${assets:,}")
            
        except Exception as e:
            print(f"Error on {name}: {e}")
        
        time.sleep(0.5)
    
    print("Done!")

update_financials()
