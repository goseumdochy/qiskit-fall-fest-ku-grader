from typeguard import typechecked
from qff_ku_grader.grader import grade

from qiskit import QuantumCircuit, qasm3

@typechecked
def grade_challenge10a(answer1: QuantumCircuit) -> None:
    grade(answer1.qasm(), "Challenge10a")
    
@typechecked
def grade_challenge10b(answer2: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer2), "Challenge10b")
    
@typechecked
def grade_challenge10c(answer3: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer3), "Challenge10c")
    
@typechecked
def grade_challenge10d(answer4: QuantumCircuit) -> None:
    grade(qasm3.dumps(answer4), "Challenge10d")