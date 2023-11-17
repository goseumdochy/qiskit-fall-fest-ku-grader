import json

from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from qiskit import execute
from qiskit_ibm_provider.job import IBMCircuitJob as IBMQJob

from .api import (
    get_submission_endpoint,
    send_request
)

from .common import (
    ValidationResult,
    calc_depth,
    get_provider,
    serialize_answer
)

def grade(
    answer: Any,
    question: Union[str, int],
    **kwargs: Any
):
    serialized_answer = serialize_answer(answer, **kwargs)

    endpoint = get_submission_endpoint(question)
    if endpoint == None:
        return
    
    payload = {'answer': serialized_answer}
    if serialized_answer is not None and endpoint:
        grade_answer(
            payload,
            endpoint
        )
    else:
        handle_grade_response('failed')
        
        
def grade_answer(
    payload: Dict[str, str],
    endpoint: str
):
    try:
        answer_response = send_request(
            endpoint,
            payload=payload
        )
        
        # For challenge 2
        if answer_response["grading_validation"] != "Valid" and answer_response["grading_validation"] != "Invalid":
            a = answer_response["grading_validation"]
            print(f"\nYour Challenge2 score is {a}")
        
        # For rest challenge
        else:
            handle_grade_response(answer_response["grading_validation"])
        
    except Exception as err:
        print(f'Failed: {err}')
        return False, None, str(err)

def handle_grade_response(status: Optional[str]) -> None:
    if status == 'Valid':
        print('\nCongratulations 🎉! Your answer is correct.')
    else:
         print(f'\nOops 😕! Your answer is incorrect')