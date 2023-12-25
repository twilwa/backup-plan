import os
import requests
import time
import getpass


# Set environment variables for FAL credentials
os.environ["FAL_KEY_ID"] = getpass("Enter your FAL key ID: ")
os.environ["FAL_KEY_SECRET"] = getpass("Enter your FAL key secret: ")

# Define the headers for authorization
headers = {
    "Authorization": f"Key {os.environ['FAL_KEY_ID']}:{os.environ['FAL_KEY_SECRET']}",
    "Content-Type": "application/json"
}

# Define the payload for the request
payload = {
    "prompt": "an island near sea, with seagulls, moon shining over the sea, light house, boats in the background, fish flying over the sea",
    "image_url": "https://storage.googleapis.com/falserverless/model_tests/lcm/source_image.png",
    "strength": 0.8,
    "negative_prompt": "cartoon, illustration, animation. face. male, female",
    "seed": 42,
    "guidance_scale": 1,
    "num_inference_steps": 4,
    "sync_mode": 0,
    "num_images": 1,
    "enable_safety_checks": True,
    "request_id": ""
}

# Submit the request to the FAL service's queue
submit_url = "https://110602490-lcm-sd15-i2i.gateway.alpha.fal.ai/fal/queue/submit"
response = requests.post(submit_url, headers=headers, json=payload)

# Check if the request was successfully accepted for processing
if response.status_code == 200:  # Check for 200 status code
    response_data = response.json()
    request_id = response_data["request_id"]
    print(f"Request ID: {request_id}")

    # Poll the status of the request
    status_url = f"https://110602490-lcm-sd15-i2i.gateway.alpha.fal.ai/fal/queue/requests/{request_id}/status"
    completed = False
    while not completed:
        status_response = requests.get(status_url, headers=headers)
        if status_response.status_code in [200, 202]:  # Check for 200 or 202 status code
            status_data = status_response.json()
            if status_data['status'] == 'COMPLETED':
                completed = True
                print("Request completed successfully.")
                # Retrieve the result if the request is completed
                response_url = f"https://110602490-lcm-sd15-i2i.gateway.alpha.fal.ai/fal/queue/requests/{request_id}/response"
                result_response = requests.get(response_url, headers=headers)
                if result_response.status_code == 200:
                    result_data = result_response.json()
                    print(result_data)
                else:
                    print(f"Failed to get request result: {result_response.status_code}")
            elif status_data['status'] in ['IN_PROGRESS', 'IN_QUEUE']:
                print(f"Request is {status_data['status']}...")
                time.sleep(5)  # Wait for 5 seconds before checking again
        else:
            print(f"Failed to get request status: {status_response.status_code}")
            break
else:
    print(f"Failed to submit request: {response.status_code}")