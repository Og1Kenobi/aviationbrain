import requests
from pathlib import Path
from tqdm import tqdm

DATA_DIR = Path("data/far_aim")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Corrected and verified FAA document links (June 2026)
DOCS = {
    "AIM_Basic_w_Chg_1_and_2_dtd_1-22-26.pdf": "https://www.faa.gov/air_traffic/publications/media/AIM_Basic_w_Chg_1_and_2_dtd_1-22-26.pdf",
    
    "FAA-H-8083-25C_PHAK.pdf": "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/faa-h-8083-25c.pdf",
    
    "FAA-H-8083-3C_Airplane_Flying_Handbook.pdf": "https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/airplane_handbook/00_afh_full.pdf",
    
    "FAA-H-8083-16B_Instrument_Procedures_Handbook.pdf": "https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/instrument_procedures_handbook/FAA-H-8083-16B.pdf",
    
    "FAA-H-8083-28B_Aviation_Weather_Handbook.pdf": "https://www.faa.gov/sites/faa.gov/files/FAA-H-8083-28B.pdf",
    
    "FAA-H-8083-2_Risk_Management_Handbook.pdf": "https://www.faa.gov/sites/faa.gov/files/2022-06/risk_management_handbook_2A.pdf",
    
    "FAA-H-8083-9_Aviation_Instructors_Handbook.pdf": "https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/aviation_instructors_handbook/aviation_instructors_handbook.pdf",
}

def download_file(url, filename):
    filepath = DATA_DIR / filename
    if filepath.exists():
        print(f"✅ Already exists: {filename}")
        return
    
    print(f"📥 Downloading {filename}...")
    try:
        response = requests.get(url, stream=True, timeout=120)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filepath, "wb") as f, tqdm(
            desc=filename[:40],
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024*1024):
                size = f.write(data)
                bar.update(size)
                
        print(f"✅ Downloaded: {filename}")
        
    except Exception as e:
        print(f"❌ Failed {filename}: {e}")

if __name__ == "__main__":
    print("🚀 Downloading core FAA documents...\n")
    
    for filename, url in DOCS.items():
        download_file(url, filename)
    
    print("\n🎉 All downloads finished!")
    print(f"Files are saved in: {DATA_DIR.resolve()}")
    print("\nNext step: Run `python ingest_faraim.py` to update your Aviation Brain.")