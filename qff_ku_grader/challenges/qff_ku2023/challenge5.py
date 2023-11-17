from typeguard import typechecked
from qff_ku_grader.grader import grade

from qiskit import QuantumCircuit, qasm3

@typechecked
def grade_challenge5a(answer1: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer1), "Challenge5a")
    
@typechecked
def grade_challenge5b(answer2: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer2), "Challenge5b")
    
@typechecked
def grade_challenge5c(answer3: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer3), "Challenge5c")
    
@typechecked
def grade_challenge5d(answer4: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer4), "Challenge5d")