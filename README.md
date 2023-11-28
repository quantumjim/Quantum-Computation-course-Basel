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

More information regarding the final project can be found [here](https://github.com/quantumjim/Quantum-Computation-course-Basel/tree/2022#examfinal-project).

**Note: This project forms 50% of your final grade**
