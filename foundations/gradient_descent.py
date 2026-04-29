class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer = init

        for _ in range(iterations):
            minimizer = minimizer - learning_rate* (2*minimizer)
        return round(minimizer,5)
