from typeguard import typechecked
from qff_ku_grader.grader import grade

from qiskit import QuantumCircuit

@typechecked
def grade_challenge3a(answer1: QuantumCircuit) -> None:
    grade(answer1.qasm(), "Challenge3a")
    
@typechecked
def grade_challenge3b(answer2) -> None:
    grade(answer2.qasm(), "Challenge3b")