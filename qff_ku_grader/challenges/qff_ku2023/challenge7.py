from typeguard import typechecked
from qff_ku_grader.grader import grade

from qiskit import QuantumCircuit

@typechecked
def grade_challenge7a(answer1: QuantumCircuit) -> None:
    grade(answer1.qasm(), "Challenge7a")
    
@typechecked
def grade_challenge7b(answer2: QuantumCircuit) -> None:
    grade(answer2.qasm(), "Challenge7b")
    
@typechecked
def grade_challenge7c(answer3: QuantumCircuit) -> None:
    grade(answer3.qasm(), "Challenge7c")
    
@typechecked
def grade_challenge7d(answer4: int) -> None:
    grade(answer4, "Challenge7d")