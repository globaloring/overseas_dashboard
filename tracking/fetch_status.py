import json
import os

def fetch_shipment_status(hbl_number):
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'mock_tracking.json')
    
    with open(path, 'r') as f:
        data = json.load(f)

    shipment = data.get(hbl_number)

    if not shipment:
        print(f"No data found for HBL: {hbl_number}")
        return

    print(f"\n📦 Tracking for HBL {shipment['HBL']}")
    for event in shipment['events']:
        print(f"- {event['event']}: {event['date']}")


# Test it
if __name__ == "__main__":
    hbl = input("Enter HBL number: ").strip()
    fetch_shipment_status(hbl)
