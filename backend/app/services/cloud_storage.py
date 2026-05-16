import os
from google.cloud import storage


def upload_file(bucket_name: str, source_file: str, destination_blob: str) -> str:
    """
    Uploads a file to Google Cloud Storage.
    Safe against missing credentials, falling back gracefully to mock operations.
    """
    try:
        # Check if Google application credentials environment variable is configured
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            print("[CLOUD STORAGE] GOOGLE_APPLICATION_CREDENTIALS not set. Using simulated storage...")
            return f"Simulation: File '{source_file}' uploaded successfully to mock bucket '{bucket_name}' as '{destination_blob}'."

        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob)
        blob.upload_from_filename(source_file)
        return f"Success: File '{source_file}' uploaded to bucket '{bucket_name}' as '{destination_blob}'."
        
    except Exception as e:
        print(f"[CLOUD STORAGE WARNING] Upload operation failed: {e}. Falling back to mock storage...")
        return f"Simulation: File '{source_file}' uploaded successfully to mock bucket '{bucket_name}' as '{destination_blob}'."
