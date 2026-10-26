# services/nlp_parser.py
import re

def parse_natural_query(query: str) -> dict:
    parsed = {}
    q = query.upper()
    
    years = re.findall(r'\b(200\d|201\d|202[0-6])\b', q)
    if years:
        parsed['year'] = int(years[0])
        
    price_match = re.findall(r'(\d+(?:\.\d+)?)\s*(?:L|LAKH|LAKHS)', q)
    if price_match:
        parsed['present_price'] = float(price_match[0])
        
    km_match = re.findall(r'(\d+)\s*(?:K\s*KM|K\s*KMS|KMS|KM|K\b)', q)
    if km_match:
        val = int(km_match[0])
        parsed['kms_driven'] = val * 1000 if val < 1000 else val
        
    if "DIESEL" in q:
        parsed['fuel_type'] = "Diesel"
    elif "PETROL" in q:
        parsed['fuel_type'] = "Petrol"
    elif "CNG" in q:
        parsed['fuel_type'] = "CNG"
        
    if any(k in q for k in ["AUTOMATIC", "AUTO", "AT", "CVT", "DCT"]):
        parsed['transmission'] = "Automatic"
    elif any(k in q for k in ["MANUAL", "MT"]):
        parsed['transmission'] = "Manual"
        
    cities = ["CHENNAI", "BANGALORE", "MUMBAI", "DELHI", "HYDERABAD", "PUNE", "KOLKATA"]
    for city in cities:
        if city in q:
            parsed['city'] = city.title()
            break
            
    return parsed
