#!/usr/bin/env python3

import json
import logging
import os
import sys
import urllib.request
import urllib.error
import urllib.parse
from typing import Optional, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_token_info(access_token: str) -> Optional[Dict]:
    """
    Retrieve token information from Google OAuth2 endpoint.

    Args:
        access_token (str): The access token to validate

    Returns:
        Optional[Dict]: Token information if successful, None otherwise
    """
    base_url = "https://oauth2.googleapis.com/tokeninfo"
    params = urllib.parse.urlencode({'access_token': access_token})
    url = f"{base_url}?{params}"

    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        logger.error(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        logger.error(f"URL Error: {str(e)}")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"JSON Decode Error: {str(e)}")
        return None

def main() -> None:
    """
    Main function to process the access token and retrieve token information.
    """
    access_token = os.getenv('CLOUDSDK_AUTH_ACCESS_TOKEN')

    if not access_token:
        logger.error('Please set token using CLOUDSDK_AUTH_ACCESS_TOKEN env variable')
        sys.exit(1)

    token_info = get_token_info(access_token)

    if token_info:
        logger.info("Token Information:")
        logger.info(json.dumps(token_info, indent=2))
    else:
        logger.error("Failed to retrieve token information")
        sys.exit(1)

if __name__ == "__main__":
    main()

