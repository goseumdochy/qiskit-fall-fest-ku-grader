import os
import requests

from urllib.parse import urljoin

from typing import Dict, List, Mapping, Optional, Union

#from qc_grader import __version__
from .common import MaxContentError, normalize_slash

submission_endpoints: List[str] = [
    'http://127.0.0.1:8000', #여기에 서버 이름 추가
    'http://3.34.129.140:8000'
]

_api_submit_url: Optional[str] = os.getenv('QC_GRADING_ENDPOINT')

def get_submission_endpoint(
    question_id: Union[str, int]
    ) -> Optional[str]:
    # https://challenges-api-dev.quantum-computing.ibm.com
    global _api_submit_url
    if not _api_submit_url:
        for endpoint in submission_endpoints:
            try:
                response = requests.get(url=endpoint)
                response.raise_for_status()
                if response.status_code == 200:
                    _api_submit_url = endpoint
                    break
            except Exception as err:
                pass

    if not _api_submit_url:
        print('Could not find a valid API server or '
              'the API servers are down right now.')
        return None

    return f'{normalize_slash(_api_submit_url)}answers/{question_id}'

def send_request(
    endpoint: str,
    payload: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    response = requests.post(
        endpoint,
        json=payload
    )
    
    if response.status_code != 200:
        if response.status_code == 403:
            result = f'Unable to access service ({response.reason})'
        else:
            try:
                result = response.json()
                if 'error' in result:
                    result = result['error']
                if 'message' in result:
                    result = result['message']
            except Exception:
                result = f'Not Successful - {response.reason}'
        raise Exception(result)
    return response.json()