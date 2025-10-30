# Quantum Computation and Error Correction

This is a [course at the University of Basel](https://vorlesungsverzeichnis.unibas.ch/de/vorlesungsverzeichnis?periode=2025004&keyword=wootton&hid=&search=1#searchResults), given by Dr James Wootton, Pierre Fromholz and Daniel Bultrini of [Moth Quantum](https://mothquantum.com/).

## Course Content

This course is an introduction to quantum computation, with a focus in the last third on quantum error correction. It is suitable for students with a physics, nanoscience, computer science or mathematical background. Theologians and philosophers have also been known to try it out!

The language of instruction is English.

## Course Text

The course will be based on the [Qiskit textbook](https://github.com/NCCR-SPIN/qiskit-textbook/blob/main/content/preface.ipynb). Links to specific pages will be given for each lecture. Note that this textbook is no longer maintained, and so does not reflect the most recent version of Qiskit.

## Lectures

The course consists of the following set of lectures. We will aim to do slightly more than one per week. All lectures will be given in person (14:15, Physik, Alter Hörsaal 2, 1.22), but [video versions](https://www.youtube.com/playlist?list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-) of many lectures are available also. For those, links to the pertinent parts of the Qiskit textbook can be found in the video descriptions. **Let me know if any link doesn't work!**

* 16/09: [The Atoms of Computation and What is Quantum](https://youtu.be/myzcjukQUFc)
* 23/09: [Representing Single Qubit States and Gates](https://www.youtube.com/watch?v=GdRt8vO9xY8)
* 30/09: [Multi qubit States and Circuit Identities](https://www.youtube.com/watch?v=pzkeypXaQ-Q)
* 07/10: [Fun with matrices](https://www.youtube.com/watch?v=e7NTozZMRqk)
* 14/10: [Circuits and Universality](https://www.youtube.com/watch?v=E53mfGrV8ek) [Notes available on ADAM]
* 21/10: [Basic Algorithms and Protocols](https://www.youtube.com/watch?v=fNOEVXQKv9M) [Notes available on ADAM]
* 28/10: [From the Fourier Transform to Shor's Algorithm](https://www.youtube.com/watch?v=WqgNu8ZziPQ)
* 04/11: [Grover's Algorithm and why we can't yet run it](https://www.youtube.com/watch?v=YfFp3K4cAF4) [Notes available on ADAM]
* 11/11: Notion of entanglement theory: checking that what we are doing is indeed quantum [Notes available on ADAM], [application notebooks available](https://github.com/quantumjim/Quantum-Computation-course-Basel/tree/main/extra_resources/Entanglement_extra)
* 18/11: The main obstacle to fault-tolance: noise in Quantum computers [Notes available on ADAM]
* 25/11: Mitigating noise: being right at a cost [May change]
* 02/12: [Introduction to QEC 1: The repetition code](https://www.youtube.com/watch?v=AuDfq7j_W7E&list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-&index=10) and [Introduction to QEC 2: The surface code](https://www.youtube.com/watch?v=IdZkxX-Qank&list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-&index=11)
* 09/12: NISQ-compatible algorithms [May change]
* 16/12: Final Project brainstorming (1 hour only)


## Extra Topics

For some lectures there is also some extra content. We'll cover it if there is time. Otherwise, you can expect to see it in the exercises.

* [The Unique Properties of Qubits](extra_resources/unique-properties-qubits.ipynb)
* [Python, Qiskit and Hello Qiskit](https://youtu.be/mMJtw-vFXC4)
* [Density matrices](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/2_The_Qubit.pdf), [partial trace](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/3_Quantum_Information.pdf) and [Schmidt decomposition](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/6_Quantum_Correlations_part_1.pdf). (Largely included in the "Notion of Entanglement" lecture)
* [Proof that Clifford + t is universal](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/extra_resources/Lecture%206%20(2013%20version).pdf)
* [Relative Entropy and Entanglement Sharing](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/7_Quantum_Correlations_part_2.pdf) (Largely included in the "Notion of Entanglement" lecture)
* [Quantum key distribution](https://github.com/NCCR-SPIN/qiskit-textbook/blob/main/content/ch-algorithms/quantum-key-distribution.ipynb)
* [Quantum noise](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/8_Quantum_Noise.pdf) (Largely included in the "noise in Quantum Computer" lecture) and [Stabilizer formalism](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/9_Stabilizer_Formalism.pdf)


## Exercises

### Take-Home Exercises

Four sets of take-home exercises set throughout the course. There will be hints sessions at 16:15 on the dates that these are set. Solutions will be presented after the exercises have been graded.

* [Exercise 1](exercises/Exercise1.ipynb): Set 30/09, due 14/10.
* [Exercise 2](exercises/ex2_graded.pdf): Set 21/10, due 4/11.
* Exercise 3: Set 11/11, due 25/11.
* Exercise 4: Set 02/12, due 16/12.

**Note: These exercises form the final grade for the [2 practical credit points](https://vorlesungsverzeichnis.unibas.ch/en/course-directory?id=297199)**

### Practice Exercises

We will also have practice exercises that are not handed in and not graded. The TA will take you through hints and solutions.

* [Practice Exercises 1](practice/Practice1.ipynb): set 7/10, solutions 14/10.
* [Practice Exercises 2](practice/PracticeExercise2): set 14/10, solutions 21/10.
* [Practice Exercises 3](practice/PracticeExercise3): set 28/10, solutions 04/10.


## Final Project

As in previous years, we'll have a final project instead of a standard exam. The main aim of this is for you to demonstrate understanding of the topics in the course. The format is fairly free to allow you to do this in a way that suits you best. Collaboration will be fine. But everyone needs something unique to submit.

**Note: These project forms the final grade for the [4 lecture credit points](https://vorlesungsverzeichnis.unibas.ch/en/course-directory?id=294582)**


### Important dates

You have until TDB January to hand-in your final projects (to me, by email). You are expected to put a similar amount of time and effort in to the final project as you would put into two sets of exercises.

You have until TBD December to email me and ask for feedback on project ideas, and to give guidelines for what would be expected for them. We will also use the lecture on 16th December as a brainstorming session.

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
