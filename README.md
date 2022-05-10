# Quantum Information

This is a [course at the University of Basel](https://vorlesungsverzeichnis.unibas.ch/en/semester-planning?id=264654), given by James Wootton of [IBM Research](https://researcher.watson.ibm.com/researcher/view.php?person=zurich-JWO).

The course begins on 22nd Feb 2022 and will have weekly lectures and exercises.

## Course Content

Quantum information theory is the basis of multiple emerging technologies, such as quantum computation and quantum crypotography. It allows us to understand how quantum effects in physical systems may be harnessed for new forms of information processing. The course will also feature some hands on experience with quantum technology, via the open-source Qiskit framework for quantum computing.

## Course Text

The course will be based on the [Qiskit textbook](https://qiskit.org/textbook/preface.html).

## Lectures

In-person lectures will be held when possible. However, since the lectures will follow the same format as in 2021, pre-recorded lectures will be available for all who cannot attend for any reason.

* Lecture 1, March 1: The Atoms of Computation and What is Quantum
* Lecture 2, March 8: Python, Qiskit and Hello Qiskit
* Lecture 3, March 15: Representing Single Qubit States and Gates
* Lecture 4, March 22: Multi-qubit States and Circuit Identities
* Lecture 5, March 29: Fun with Matrices
* Lecture 6, April 5: Circuits and Universality
* Lecture 7, April 12: Basic Algorithms and Protocols
* Lecture 8, April 19: From the Fourier Transform to Shor's Algorithm
* Lecture 9, April 26: Grover's Algorithm (and why we can't yet run it)
* Lecture 10, May 3: Introduction to Quantum Error Correction
* Lecture 11, May 10: Quantum Error Correction: Surface Codes
* Lecture 12, May 17: Quantum Games
* Lecture 13, May 24: tbc
* Lecture 14, May 31: tbc

## Exercises

Some exercises will be in the form of Jupyter notebooks. These can be run locally by installing [Python 3](https://www.python.org/downloads/), [Jupyter](https://jupyter.org/) and [Qiskit](https://qiskit.org/). They can also be run online without any installation using the [IBM Quantum Lab](https://quantum-computing.ibm.com/lab). When you are on the files menu of the lab, you can click on the 'upload file' icon to upload notebooks.

The easiest way to to download the exercises is to download the whole repository using [this link](https://github.com/quantumjim/Quantum-information-course-Basel/archive/master.zip).

The exercises will make up 50% of the final grade. On each of the exercises you can score a value between 0 and 1, where 1 is the best score.

Exercises are due on Tuesdays at 4:15pm and can be handed it as a hand-written piece of paper or via email to the corresponding teaching assistant (TA). If the exercise is a python notebook (.ipynb file), please send the .ipynb file as well as a pdf-version of that file by email.

The TAs of this course are Maria (maria.spethmann@unibas.ch), Bence (bence.hetenyi@unibas.ch), Pierre (pierre.fromholz@unibas.ch) and Even (even.thingstad@unibas.ch).

Here is the provisional list with the due dates for all exercises and the corresponding TAs:

* Exercise 1,  due on March 15, hand in to Maria
* Exercise 2,  due on March 22, hand in to Bence
* Exercise 3,  due on March 29, hand in to Pierre
* Exercise 4,  due on April 05, hand in to Pierre
* Exercise 5,  due on April 12, hand in to Even
* Exercise 6,  due on April 19, hand in to Even
* Exercise 7,  due on April 26, hand in to Maria
* Exercise 8,  due on May 03, hand in to Bence
* Exercise 9,  due on May 10, hand in to Pierre
* Exercise 10, due on May 17, hand in to Maria

The solutions of the exercises are presented at the exercise course a week after. Further, the TAs will give a few hints about the next exercise. If you cannot come to the exercise but would like to know the hints, please send an email to the corresponding TA.

## Exam/Final Project

Like in 2020 and 2021, we'll have a final project instead of a standard exam.

The main aim of this is for you to demonstrate understanding of the topics in the course. The format is fairly free to allow you to do this in a way that suits you best. Collaboration will be fine. But everyone needs something unique to submit.

Below are the different kinds of project you can choose from. Examples of existing work are given to give you and idea of what you can produce.

You can start whenever you like. The deadline is 13th June. To submit, send it to me by email.


### Write an explanation of a topic of your choice

You can write about one of the topics covered in the lectures, or about something that wasn't covered. You can include relevant example code in Qiskit, or you can avoid the programming and just have text and images

#### Examples

* [Qiskit Textbook section on Phase Kickback](https://qiskit.org/textbook/ch-gates/phase-kickback.html).
* [Qiskit Textbook section on Berstein-Vazirani](https://qiskit.org/textbook/ch-algorithms/bernstein-vazirani.html).
* [An attempt at a popular science article on quantum non-locality](https://bullshit.ist/some-quantum-weirdness-with-the-simplest-maths-possible-446d33046cf7).


### Make a game using quantum programming

Throughout the history of computing, people have been making simple games to help understand the new technology. Now we can do the same thing with quantum computing. I wrote a whole article on this idea, which you can find [here](https://medium.com/@decodoku/games-computers-and-quantum-84bfdd2c0fe0).

Basically, reasons why we might make a quantum game are:
* To provide a simple and accessible example of a quantum program in action.
* To educate people about quantum computing.
* To start looking for ways in which quantum computing might actually be useful for games.

To make a game, you need a game engine of some sort. Fortunately we at IBM Quantum have made one specifically to help people making quantum games with Qiskit. You can find it [here](https://github.com/qiskit-community/Qisge/blob/main/README.md). Also see [this video](https://www.twitch.tv/videos/996850668) on how to use it.

**Remember: don't just use quantum for a random number generator!**

#### Examples

* [Hello Qiskit](https://qiskit.org/textbook/ch-ex/hello-qiskit.html): a game that teaches quantum computing.
* [Quantum Awesomeness](https://github.com/Qiskit/qiskit-community-tutorials/blob/master/games/quantum_awesomeness.ipynb): a game that gives insight into real devices (and [featured in the NZZ](https://www.nzz.ch/wissenschaft/games-with-james-ld.1367435)).
* [QPong](https://www.youtube.com/watch?v=a1NZC5rqQD8): A game that implements the core game mechanic with a (simulation of).
* [Q Avrai](https://github.com/quantumjim/Q_Avrai/blob/master/papers/CoG/main.pdf): using quantum computing for map generation.


### Run benchmarks on prototype devices

You can access real quantum hardware at the [IBM Quantum Experience](quantum-computing.ibm.com/) and [Quantum Inspire](https://www.quantum-inspire.com/). But how well do they actually work? Many people have run various different types of quantum circuit and analyzed the results to give some insight into this.

You can come up with your own method for benchmarking, or reproduce something that has already been done on a different device. The easiest way is to implement repetition codes using [Qiskit's `topological_codes` module](https://github.com/quantumjim/TopologicalCodesTutorial/blob/main/README.md). But since this package (hopefully) makes it easy, you'll need to try out more than just a single code on a single device

#### Examples

* [Quantum Awesomeness](https://github.com/Qiskit/qiskit-community-tutorials/blob/master/games/quantum_awesomeness.ipynb): a game that gives insight into real devices (and [featured in the NZZ](https://www.nzz.ch/wissenschaft/games-with-james-ld.1367435)).
* [Decoherence of entangled states](https://arxiv.org/abs/1712.07080): A paper looking at decoherence in GHZ states.
* [Repetition Codes](https://arxiv.org/abs/2004.11037): using Qiskit's `topological_codes` module to test a device.
