import os
import json
import csv

# Folder containing JSON files
folder_path = 'success_responses'

# CSV output file
output_csv = 'output.csv'

# Column names
columns = [
    'No', 'Date', 'Workspace', 'Portfolio', 'Password', 'Login link',
    'Login QR code image', 'Scale link', 'Scale QR code image',
    'Social media link', 'Social media QR code image',
    'Print link',  'Print QR code image', 'Email link',
    'Email QR code image', 'Stand link', 'Stand QR code image',
    'Report link', 'Report QR code image'
]

# Common values
workspace = "VOCAB"
login_link = "https://www.scales.uxlivinglab.online/api/voc/login/?workspace_name=VOCAB"

# Initialize CSV file
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()

    # Get and sort the list of files
    json_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.json')])

    # Iterate through each file in the sorted list
    for filename in json_files:
        with open(os.path.join(folder_path, filename), 'r') as jsonfile:
            data = json.load(jsonfile)
            response = data.get('response', {})
            
            # Extract values
            portfolio = response.get('portfolio')
            created_at = response.get('created_at')
            login_qr_code_image = response.get('login', {}).get('qrcode_image_url')
            
            links_details = response.get('links_details', [])
            report_link = response.get('report_link', {}).get('report_link')
            report_qr_code_image = response.get('report_link', {}).get('qrcode_image_url')

            # Assuming the links follow the order in the columns
            row = {
                'No': filename.replace('.json', ''),  # Use filename (without .json) as No
                'Date': created_at,
                'Workspace': workspace,
                'Portfolio': portfolio,
                'Password': '',
                'Login link': login_link,
                'Login QR code image': login_qr_code_image,
                'Scale link': links_details[0].get('scale_link') if len(links_details) > 0 else '',
                'Scale QR code image': links_details[0].get('qrcode_image_url') if len(links_details) > 0 else '',
                'Social media link': links_details[1].get('scale_link') if len(links_details) > 1 else '',
                'Social media QR code image': links_details[1].get('qrcode_image_url') if len(links_details) > 1 else '',
                'Print link': links_details[2].get('scale_link') if len(links_details) > 2 else '',
                'Print QR code image': links_details[2].get('qrcode_image_url') if len(links_details) > 2 else '',
                'Email link': links_details[3].get('scale_link') if len(links_details) > 3 else '',
                'Email QR code image': links_details[3].get('qrcode_image_url') if len(links_details) > 3 else '',
                'Stand link': links_details[4].get('scale_link') if len(links_details) > 4 else '',
                'Stand QR code image': links_details[4].get('qrcode_image_url') if len(links_details) > 4 else '',
                'Report link': report_link,
                'Report QR code image': report_qr_code_image
            }

            # Write the row to CSV
            writer.writerow(row)

print(f"Data has been written to {output_csv}")
