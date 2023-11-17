from typeguard import typechecked
from qff_ku_grader.grader import grade

from qiskit import QuantumCircuit, qasm3

@typechecked
def grade_challenge6a(answer1: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer1), "Challenge6a")
    
@typechecked
def grade_challenge6b(answer2: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer2), "Challenge6b")
    
@typechecked
def grade_challenge6c(answer3: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer3), "Challenge6c")