Fullstack Take Home Assignment
(PageRank)
We are on a mission to build an ac1onable and interoperable AI products with cu7ng edge
deep learning and NLP.
Below is the work sample. Ideally, please try to spend up to 4 hours total; however, we
understand that it may take a liDle more 1me. Let us know if you have any ques1ons, and
hope you have some fun with it!

Graph Visualiza-on
Graphs (i.e., nodes, edges, etc.) are a major component of data science, and in par1cular, a
central underpinning of the technology we are building.
Objec-ve:
For this project, the goal is to build a quick graph implementa-on and visualiza-on,
implement a func1on that calculates the PageRank of a node, and write tests of their
func1onality.
While many graph libraries exist, we would like you to write a simple graph implementa-on
that allows users to, via a frontend interface:
Add nodes to a graph
Add edges to a graph
Get neighboring nodes given a node (directed or undirected as you prefer)
(Op1onal) Remove nodes and edges from the graph
Please document your func1ons/classes, in the same manner you would when working with
many collaborators.
Addi1onally, please write a func1on that consumes an instance of your graph (and likely
other parameters) and returns the result of a PageRank calcula1on.
There are many corner cases, op1miza1ons, and subtle1es for a fully produc1on-ready
implementa1on of PageRank. Your implementa1on does not need to solve all of them. Please
start with a simple implementa1on and men1on known limita1ons in your README.

Finally, please write unit tests for the public func1onality of your graph (those men1oned
above) and for your PageRank implementa1on. For the PageRank test, you only need to
provide a single test that shows its usage and expected output. Our preference is for you to
use an exis1ng unit tes1ng framework, but a script that makes the relevant asser1ons is also
acceptable.
Please include instruc1ons for how to run your tests.
Deliverables:
Private Github repo with README Design Doc detailing your design decisions, resul1ng
tradeoffs, and limita1ons of your implementa1ons.
A simple graph implementa1on with the public func1onality men1oned above.
An implementa1on of PageRank.
A front end interface allowing visualiza1on of nodes and their PageRank weights given a
graph structure (please use any format for graph data you would like)
Unit tests for all public func1ons.
Notes:
Feel free to use the language of your choice for the backend processing

Python or
Javascript preferred). Please use a component-based library for the front end
(preferably React)
Please use good object-oriented design where applicable, including separa1on of
public/private func1onality and extensibility for future usecases (e.g., expect someone
to subclass your graph objects to implement addi1onal func1onality).
Please write clear documenta1on so someone can quickly learn how to use your classes
and func1ons.
Engineering Principles to keep in mind:
Simple. As simple as possible, but no simpler.
Prescient. An1cipates future needs.
Flexible. Separable and replaceable code.
Intui-ve. Good naming conven1ons, well-scoped methods, clear documenta1on
describing important details, etc.