from typeguard import typechecked
from qff_ku_grader.grader import grade

from typing import List
from qiskit import QuantumCircuit

@typechecked
def grade_challenge4a(answer1: QuantumCircuit) -> None:
    grade(answer1.qasm(), "Challenge4a")
    
@typechecked
def grade_challenge4b(answer2: QuantumCircuit) -> None:
    grade(answer2.qasm(), "Challenge4b")
    
@typechecked
def grade_challenge4c(answer3: bool) -> None:
    grade(answer3, "Challenge4c")

@typechecked
def grade_challenge4d(answer4: List[int]) -> None:
    grade(answer4, "Challenge4d")
    
@typechecked
def grade_challenge4e(answer5: QuantumCircuit) -> None:
    grade(answer5.qasm(), "Challenge4e")