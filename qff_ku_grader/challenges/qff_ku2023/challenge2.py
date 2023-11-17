from typeguard import typechecked
from qff_ku_grader.grader import grade

@typechecked
def grade_challenge2(answer: list) -> None:
    answer[14] = answer[14].qasm()
    grade(answer, "Challenge2")