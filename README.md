# Quantum Computation and Error Correction

This is a [course at the University of Basel](https://vorlesungsverzeichnis.unibas.ch/de/semester-planung?id=286075), given by Dr James Wootton of Moth Quantum.

## Course Content

This course is an introduction to quantum computation, with a focus in the last third on quantum error correction. It is suitable for students with a physics, nanoscience, computer science or mathematical background. Theologians and philosophers have also been known to try it out!

The language of instruction is English.

## Course Text

The course will be based on the [Qiskit textbook](https://github.com/NCCR-SPIN/qiskit-textbook/blob/main/content/preface.ipynb). Links to specific pages will be given for each lecture. Note that this textbook is no longer maintained, and so does not reflect the most recent version of Qiskit.

## Lectures

The course consists of the following set of lectures. We will aim to do slightly more than one per week. All lectures will be given in person (14:15, [Seminarzimmer 4.1](https://vorlesungsverzeichnis.unibas.ch/ajax/room.cfm?id=8210)), but [video versions](https://www.youtube.com/playlist?list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-) of many lectures are available also. For those, links to the pertinent parts of the Qiskit textbook can be found in the video descriptions. **Let me know if any link doesn't work!**

* 10/09: [The Atoms of Computation and What is Quantum](https://youtu.be/myzcjukQUFc)
* 17/09: [Representing Single Qubit States and Gates](https://www.youtube.com/watch?v=GdRt8vO9xY8)
* 24/09: [Multi qubit States and Circuit Identities](https://www.youtube.com/watch?v=pzkeypXaQ-Q)
* 01/10: [Fun with matrices](https://www.youtube.com/watch?v=e7NTozZMRqk)
* 08/10: [Circuits and Universality](https://www.youtube.com/watch?v=E53mfGrV8ek)
* 15/10: [From the Fourier Transform to Shor's Algorithm](https://www.youtube.com/watch?v=WqgNu8ZziPQ)
* 22/10: [Basic Algorithms and Protocols](https://www.youtube.com/watch?v=fNOEVXQKv9M)
* 29/10: [Grover's Algorithm and why we can't yet run it](https://www.youtube.com/watch?v=YfFp3K4cAF4)
* 5/11: [Introduction to QEC 1: The repetition code](https://www.youtube.com/watch?v=AuDfq7j_W7E&list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-&index=10)
* 12/11: [Introduction to QEC 2: The surface code](https://www.youtube.com/watch?v=IdZkxX-Qank&list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-&index=11) and the [Stabilizer formalism](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/9_Stabilizer_Formalism.pdf)
* 19/11: [Classical Coding](extra_resources/Classical%20Coding.pdf) and Decoded Quantum Interferometry (based on [this talk](https://www.youtube.com/watch?v=mA4kdOPOFLM&list=PLgKuh-lKre10gQ2WmHimdr4Bqa3uE8yhX&index=3) and [this blog post](https://dabacon.org/pontiff/2024/10/29/new-quantum-algorithm-dance-dqi-edition/))
* 26/11: Entanglement: [Part 1](QI_Course/7_Quantum_Correlations_part_2) [Part 2](QI_Course/7_Quantum_Correlations_part_2)
* 03/12: ZX Calculus: [Part 1](extra_resources/ZX.pdf) [Part 2](extra_resources/Wootton-QNLP2023.pdf)
* 10/12: Benchmarking
* 17/12: Final Project brainstorming (1 hour only)


## Extra Topics

For some lectures there is also some extra content. We'll cover it if there is time. Otherwise, you can expect to see it in the exercises.

* [The Unique Properties of Qubits](extra_resources/unique-properties-qubits.ipynb)
* [Python, Qiskit and Hello Qiskit](https://youtu.be/mMJtw-vFXC4)
* [Density matrices](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/2_The_Qubit.pdf), [partial trace](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/3_Quantum_Information.pdf) and [Schmidt decomposition](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/6_Quantum_Correlations_part_1.pdf).
* [Proof that Clifford + t is universal](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/extra_resources/Lecture%206%20(2013%20version).pdf)
* [Relative Entropy and Entanglement Sharing](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/7_Quantum_Correlations_part_2.pdf)
* [Quantum key distribution](https://github.com/NCCR-SPIN/qiskit-textbook/blob/main/content/ch-algorithms/quantum-key-distribution.ipynb)
* [Quantum noise](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/8_Quantum_Noise.pdf) and [Stabilizer formalism](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/9_Stabilizer_Formalism.pdf)


## Exercises

### Take-Home Exercises

Four sets of take-home exercises set throughout the course. There will be hints sessions at 16:15 on the dates that these are set. Solutions will be presented after the exercises have been graded.

* [Exercise 1](exercises/Exercise1.ipynb): Set 01/10/2024, due 15/10/2024, Anatolii as TA.
* [Exercise 2](exercises/Exercise2.ipynb): Set 15/10/2024, due 29/10/2024, Anatolii as TA.
* [Exercise 3](exercises/Exercise3.ipynb): Set 29/10/2024, due 12/11/2024, Kacper as TA.
* [Exercise 4](exercises/Exercise4.ipynb): Set 12/11/2024, due 26/11/2024, Kacper as TA.



**Note: These exercises form 50% of your final grade**

## Final Project

As in previous years, we'll have a final project instead of a standard exam. The main aim of this is for you to demonstrate understanding of the topics in the course. The format is fairly free to allow you to do this in a way that suits you best. Collaboration will be fine. But everyone needs something unique to submit.

**Note: This project forms 50% of your final grade**

### Important dates

You have until 13th January to hand-in your final projects (to me, by email). You are expected to put a similar amount of time and effort in to the final project as you would put into two sets of exercises.

You have until 20th December to email me and ask for feedback on project ideas, and to give guidelines for what would be expected for them. We will also use the lecture on 17th December as a brainstorming session.

### Project ideas

Below are examples of the different kinds of project you can choose from. Examples of existing work are given to give you and idea of what you can produce. A list of specific projects that you can do (for those of you that don't want to come up with your own) can be found at the end.

#### Write an explanation of a topic of your choice

You can write about one of the topics covered in the lectures, or about something that wasn't covered. You can include relevant example code in Qiskit, or you can avoid the programming and just have text and images

##### Examples

* [Qiskit Textbook section on Phase Kickback](https://qiskit.org/textbook/ch-gates/phase-kickback.html).
* [Qiskit Textbook section on Berstein-Vazirani](https://qiskit.org/textbook/ch-algorithms/bernstein-vazirani.html).
* [An attempt at a popular science article on quantum non-locality](https://bullshit.ist/some-quantum-weirdness-with-the-simplest-maths-possible-446d33046cf7).


#### Make a game using quantum programming

Throughout the history of computing, people have been making simple games to help understand the new technology. Now we can do the same thing with quantum computing. I wrote a whole article on this idea, which you can find [here](https://medium.com/@decodoku/games-computers-and-quantum-84bfdd2c0fe0).

Basically, reasons why we might make a quantum game are:
* To provide a simple and accessible example of a quantum program in action.
* To educate people about quantum computing.
* To start looking for ways in which quantum computing might actually be useful for games.

**Remember: don't just use quantum for a random number generator!**

##### Examples

* [Hello Qiskit](https://qiskit.org/textbook/ch-ex/hello-qiskit.html): a game that teaches quantum computing.
* [Quantum Awesomeness](https://github.com/decodoku/A_Game_to_Benchmark_Quantum_Computers/blob/master/README.md): a game that gives insight into real devices (and [featured in the NZZ](https://www.nzz.ch/wissenschaft/games-with-james-ld.1367435)).
* [QPong](https://www.youtube.com/watch?v=a1NZC5rqQD8): A game that implements the core game mechanic with a (simulation of).
* [Q Avrai](https://github.com/quantumjim/Q_Avrai/blob/master/papers/CoG/main.pdf): using quantum computing for map generation.


#### Run benchmarks on prototype devices

You can access real quantum hardware at [IBM Quantum](quantum-computing.ibm.com/), [Quantum Inspire](https://www.quantum-inspire.com/) and other places. But how well do they actually work? Many people have run various different types of quantum circuit and analyzed the results to give some insight into this.

You can come up with your own method for benchmarking, or reproduce something that has already been done on a different device. The easiest way is to implement repetition codes using [Qiskit-QEC]([https://github.com/quantumjim/TopologicalCodesTutorial/blob/main/README.md](https://github.com/qiskit-community/qiskit-qec/blob/main/README.md)). But since this package (hopefully) makes it easy, you'll need to try out more than just a single code on a single device

##### Examples

* [Quantum Awesomeness](https://github.com/Qiskit/qiskit-community-tutorials/blob/master/games/quantum_awesomeness.ipynb): a game that gives insight into real devices (and [featured in the NZZ](https://www.nzz.ch/wissenschaft/games-with-james-ld.1367435)).
* [Decoherence of entangled states](https://arxiv.org/abs/1712.07080): A paper looking at decoherence in GHZ states.
* [Repetition Codes](https://arxiv.org/abs/2004.11037): This uses Qiskit's old `topological_codes` module, now available in Qiskit QEC.

#### Specific project ideas

* Write a decoder for the qudit or non-Abelian decoding problems shown in [Decoding 4: Programming HDRG Decoders](https://github.com/quantumjim/qec_lectures/blob/main/lecture-4.ipynb).
    - Explain your method
    - Provide your code
    - Provide threshold graphs for different values of `k`
* A recent scheme for benchmarking known as the [layer fidelity](https://arxiv.org/abs/2311.05933) has some similarities to my old game-based benchmark, [Quantum Awesomeness](https://github.com/decodoku/A_Game_to_Benchmark_Quantum_Computers/blob/master/README.md).
    - Explain the two approaches and discuss their similarties and differences.
    - Propose a new 'Quantum Awesomeness', that uses some ideas from the layer fidelity.
    - Produce and explain some of the basic circuits required for your idea.
