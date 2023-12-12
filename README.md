# Quantum Computation and Error Correction

This is a [course at the University of Basel](https://vorlesungsverzeichnis.unibas.ch/de/home?id=278317), given by [Dr James Wootton of IBM Research](https://researcher.watson.ibm.com/researcher/view.php?person=zurich-JWO).

This repository reflects the version of the course given in 2023. For the 2020, 2021 and 2022 version see [here](https://github.com/quantumjim/Quantum-Computation-course-Basel/tree/2022).

The lecture videos for this course are all on [YouTube](https://www.youtube.com/playlist?list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-) for you to view at any time.


## Course Content

Quantum information theory is the basis of multiple emerging technologies, such as quantum computation and quantum crypotography. It allows us to understand how quantum effects in physical systems may be harnessed for new forms of information processing. The course will also feature some hands on experience with quantum technology, via the open-source Qiskit framework for quantum computing.


## Course Text

The course will be based on the [Qiskit textbook](https://github.com/NCCR-SPIN/qiskit-textbook/blob/main/content/preface.ipynb). Note that this link is to the Jupyter notebook source files of the textbook. The latest version of Qiskit learning materials can be found [here](https://learning.quantum-computing.ibm.com/).


## Lectures

Most of the course will be done as a 'flipped classroom'. Lecture videos will be provided 1 week early. In-person sessions take place from 14:15-16:00 on Tuesdays. This will be used for questions from students, working together through exercises, and covering additional topics. 

Below are links to the lecture videos for the lectures so far. For links to the corresponding sections of the textbook, see the video description.

* Lecture 1: [The Atoms of Computation and What is Quantum](https://youtu.be/myzcjukQUFc) and [Python, Qiskit and Hello Qiskit](https://youtu.be/mMJtw-vFXC4)
    - In-class lecture: [The Unique Properties of Qubits](extra_resources/unique-properties-qubits.ipynb)
    - In-class exercise: [Quantum Logic Gates](exercises_2022/Exercise2.ipynb)

 
* Lecture 2: [Representing Single Qubit States and Gates](https://www.youtube.com/watch?v=GdRt8vO9xY8)
    - In-class exercises: [Playing with Paulis](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises_2022/Exercise3.ipynb), [More playing with Paulis](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises_2022/Exercise4.ipynb)

* Lecture 3: [Multi qubit States and Circuit Identities](https://www.youtube.com/watch?v=pzkeypXaQ-Q)
     - In-class lecture: [Density matrices](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/2_The_Qubit.pdf), [partial trace](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/3_Quantum_Information.pdf) and [Schmidt decomposition](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/6_Quantum_Correlations_part_1.pdf).

* Lecture 4: [Fun with matrices](https://www.youtube.com/watch?v=e7NTozZMRqk)

* Lecture 5: [Circuits and Universality](https://www.youtube.com/watch?v=E53mfGrV8ek)
    - In-class lecture: [Proof that Clifford + t is universal](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/extra_resources/Lecture%206%20(2013%20version).pdf)
    - In-class exercise: [Real quantum computing](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises_2022/Exercise7.ipynb)
 
* Lecture 6: [Basic Algorithms and Protocols](https://www.youtube.com/watch?v=fNOEVXQKv9M)
    - In-class lecture: [Relative Entropy and Entanglement Sharing](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/7_Quantum_Correlations_part_2.pdf)
    - In-class exercise: [Trotters and Garbage](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises_2022/Exercise6.ipynb)
 
* Lecture 7: [From the Fourier Transform to Shor's Algorithm](https://www.youtube.com/watch?v=WqgNu8ZziPQ)
    - In-class lecture [Quantum key distribution](https://github.com/NCCR-SPIN/qiskit-textbook/blob/main/content/ch-algorithms/quantum-key-distribution.ipynb)
    - In-class exercise: [The order finding operator](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises_2019/Exercise8.pdf)
 
* Lecture 8: [Grover's Algorithm and why we can't yet run it](https://www.youtube.com/watch?v=YfFp3K4cAF4)
    - In-class lecture: [Quantum noise](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/8_Quantum_Noise.pdf) and [Stabilizer formalism](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/QI_course/9_Stabilizer_Formalism.pdf)

* Lecture 9: [Introduction to QEC 1: The repetition code](https://www.youtube.com/watch?v=AuDfq7j_W7E&list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-&index=10)
    - In-class lecture: [Decoding 1: Running Circuits and Interpreting Outputs](https://github.com/quantumjim/qec_lectures/blob/main/lecture-1.ipynb)
 
* Lecture 10: [Introduction to QEC 2: The surface code](https://www.youtube.com/watch?v=IdZkxX-Qank&list=PLaU1vYImkPDxyqJ6zHAs8W92fYKsfXsV-&index=11)
    - In-class lecture: [Decoding 2: Correcting Errors](https://github.com/quantumjim/qec_lectures/blob/main/lecture-2.ipynb)

* Lecture 11: *No video lecture*
    - In-class lecture: [Toric code](https://en.wikipedia.org/wiki/Toric_code) and [LDPC codes](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/extra_resources/LDPC-codes.pdf)
    - In-class exercises: [Shor code](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises_2019/Exercise7.pdf)
 
* Lecture 12: *No video lecture*
    - In-class lecture: [Decoding 3: Programming and Using a Matching Decoder](https://github.com/quantumjim/qec_lectures/blob/main/lecture-3.ipynb)

* Lecture 13: *No video lecture*
    - In-class lecture: [Decoding 4: Programming HDRG Decoders](https://github.com/quantumjim/qec_lectures/blob/main/lecture-4.ipynb)

## Exercises

### In-Class Exercises

Exercises covered in class will be drawn from the big pile of all the exercises used in previous versions of this course.

### Take-Home Exercises

Take-home exercises set on 17th Oct, 7th Nov and 28th Nov. There will be hints sessions at 16:15 on those dates. Solutions will be presented at 16:15 on 31st Oct, 21st Nov and 12th Dec.

* [Exercise sheet 1](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises/Exercise1.ipynb): Set 17th Oct. Hint session and hand-in instructions at 16:15.

* [Exercise sheet 2](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises/Exercise2.ipynb): Set 7th Nov. Hint session and hand-in instructions at 16:15 (on Zoom).

* [Exercise sheet 3](https://github.com/quantumjim/Quantum-Computation-course-Basel/blob/main/exercises/Exercise3.ipynb): Set 28th Nov. Hint session and hand-in instructions at 16:15.

**Note: These exercises form 50% of your final grade**

## Final Project

As in previous years, we'll have a final project instead of a standard exam. The main aim of this is for you to demonstrate understanding of the topics in the course. The format is fairly free to allow you to do this in a way that suits you best. Collaboration will be fine. But everyone needs something unique to submit.

### Important dates

You have until 15th January to hand-in your final projects (to me, by email). That gives you around 3 weeks after the hand-in of your final set of exercises (not including the Christmas break). You are expected to put a similar amount of time and effort in to the final project as you would put into two sets of exercises.

You have until 21st December to email me and ask for feedback on project ideas, and to give guidelines for what would be expected for them.

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

**Note: This project forms 50% of your final grade**
