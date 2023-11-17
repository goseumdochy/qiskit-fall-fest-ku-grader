from typeguard import typechecked
from qff_ku_grader.grader import grade

from typing import List
from qiskit import QuantumCircuit, qasm3
from qiskit_optimization import QuadraticProgram

@typechecked
def grade_challenge9a(answer1: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer1), "Challenge9a")
    
@typechecked
def grade_challenge9b(answer2: List[int]) -> None:
    grade(answer2, "Challenge9b")
    
@typechecked
def grade_challenge9c(answer3: QuadraticProgram) -> None:
    grade(str(answer3), "Challenge9c")
    
@typechecked
def grade_challenge9d(answer4: QuantumCircuit) -> None:
    grade(answer4.qasm(), "Challenge9d")