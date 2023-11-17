from typeguard import typechecked
from qff_ku_grader.grader import grade

from qiskit import QuantumCircuit

@typechecked
def grade_challenge8a(answer1: QuantumCircuit) -> None:
    grade(answer1.qasm(), "Challenge8a")
    
@typechecked
def grade_challenge8b(answer2: QuantumCircuit) -> None:
    grade(answer2.qasm(), "Challenge8b")
    
@typechecked
def grade_challenge8c(answer3: QuantumCircuit) -> None:
    grade(answer3.qasm(), "Challenge8c")
    
@typechecked
def grade_challenge8d(answer4: QuantumCircuit) -> None:
    grade(answer4.qasm(), "Challenge8d")