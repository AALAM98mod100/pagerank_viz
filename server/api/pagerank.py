class PageRank():
    """This is a class to run the pagerank algorithm
    The graph is of form dict {node: [neighbors]}
    """

    def __init__(self, graph: dict, damping_factor: float = 0.85, max_iterations: int = 100, tolerance: float = 1e-6):
        """Constructor of the PageRank class

        Parameters
        ----------
        graph : dict
            The graph is of form dict {node: [neighbors]}
        damping_factor : float, optional
            The damping factor, by default 0.85
        max_iterations : int, optional
            The maximum number of iterations, by default 100
        tolerance : float, optional
            The tolerance, by default 1e-6
        """
        self.graph = graph
        self.damping_factor = damping_factor
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def run(self) -> dict:
        """Run the pagerank algorithm

        Returns
        -------
            dict
        """
        nodes = list(self.graph.keys())
        n = len(nodes)
        pr = {node: 1 / n for node in nodes}
        new_pr = {node: 0 for node in nodes}

        for _ in range(self.max_iterations):
            diff = 0
            for node in nodes:
                new_pr[node] = (1 - self.damping_factor) / n + self.damping_factor * sum(
                    pr[neighbor] / len(self.graph[neighbor]) for neighbor in self.graph if node in self.graph[neighbor]
                )
                diff += abs(new_pr[node] - pr[node])
            pr = new_pr.copy()
            if diff < self.tolerance:
                break

        return pr