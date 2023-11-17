from typeguard import typechecked

from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.quantum_info import Operator
import numpy as np

from typing import List

from qff_ku_grader.grader import grade

@typechecked
def grade_challenge1a(answer1: list) -> None:
    grade(answer1, 'Challenge1a')
    
@typechecked
def grade_challenge1b(answer2: Statevector) -> None:
    grade(answer2.data, 'Challenge1b')
    
@typechecked
def grade_challenge1c(answer3: List[np.ndarray]) -> None:
    grade(answer3, 'Challenge1c')
    
@typechecked
def grade_challenge1d(answer4: List[str]) -> None:
    grade(answer4, 'Challenge1d')
    
@typechecked
def grade_challenge1e(answer5: List[Operator]) -> None:
    answer5_1 = answer5[0].data
    answer5_2 = answer5[1].data
    grade([answer5_1, answer5_2], 'Challenge1e')
    
@typechecked
def grade_challenge1f(answer6: Operator) -> None:
    grade(answer6.data, 'Challenge1f')
    
@typechecked
def grade_challenge1g(answer7:np.ndarray) -> None:
    grade(answer7, 'Challenge1g')