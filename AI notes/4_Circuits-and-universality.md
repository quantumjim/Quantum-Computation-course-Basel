# 6 — Circuits and Universality

*Dr James Wootton, Moth Quantum*

> **Transcription note:** this is a transcript-based rewrite, using James's actual spoken narration (lightly cleaned up — filler words, mid-take corrections, and recording asides removed) matched against the whiteboard's equation order.

---

## What is computing?

Hello, I'm again Dr James Wootton. This is again a lecture on quantum computing. But what is computing?

A very simple model for what a computer does is: it takes an input, let's call it $x$, and then it computes a function, let's call it $f(x)$, to give us an output which we can call $y$:

$$x \qquad f(x) = y$$

In a digital computer, all inputs and outputs can be expressed as binary strings. So this is a function which takes in binary strings and outputs binary strings. In general those binary strings can be different lengths: an input bit string with some $n_i$ bits, an output bit string with some $n_o$ bits. And in the middle we can think of the computer as basically just being a black box which takes the input in and spits the output out:

$$n_i \text{ bit} \longrightarrow \boxed{\phantom{xxxx}} \longrightarrow n_o \text{ bit}$$

It's not literally a black box, but you get the idea.

If we can implement a general mapping from inputs to outputs for a general function in this way, then whatever it is we're using to do that, we can call **universal**. So if we can use, for example, NAND gates to perform any general mapping of this kind, we can say NAND gates are universal for computation — they can do any of these general computations, any function, any number of bits for inputs and outputs. You can find some configuration of NAND gates which does that.

---

## Why a lookup table is a terrible program

It's easiest to prove this if we think of implementing the computation through a lookup table — basically writing down the program as: if the input is some particular input, then output the corresponding output.

$$\text{NAND} \qquad \text{if } x==x' : \ \text{return } y$$

This is a terrible way to write a program, because (A) you need as many lines in your code as there are possible inputs — you have to go through all $2^{n_i}$ possible inputs, which goes up exponentially with the number of input bits — and (B) you need to know all of the answers already. Nevertheless, it's quite easy to show that if you have building-block logic gates, you can do the process of checking all the values to see if these conditions are met, and if they are, writing down the correct output. So we can show that Boolean logic gates are universal, because they can reproduce any of these functions.

$$2^{n_i}$$

Before we move on, let's look at a couple of possible functions just to be more concrete. We could have an input which is something like three times five: the binary representation of the numbers to be multiplied.

$$3 \times 5 \longrightarrow 15$$

If your function is just multiplication, that's all you need. If you have a more general computation that could do any kind of maths, you might also want a binary representation telling your computer *that* you want it to do multiplication. And of course the output here would be $15$.

But you also might have something where your input is an image — say, a picture of a cat — and your output is a simple binary yes/no of whether the image contains a cat:

$$\boxed{\text{🐱}} \longrightarrow 1$$

We'd hope a picture with a cat in it gives us a $1$, and one without gives a $0$. These are just a few examples of the many possible kinds of computation. And in this latter case, it's obvious that you do *not* want to do it by a lookup table — you don't want to go through every possible image that could ever exist and decide by hand whether there's a cat in it, then write a lookup table that checks against that list. You want to actually *process* the information. And once you do that, you get into the weeds of what is actually computable — we're not going into that right now. We're just thinking about the notion of universality: computation as a function, and when do we have the ability to implement those functions.

---

## Reversible computation

Now let's start talking more specifically about quantum computing. In quantum computing we do computations by unitary gates, and unitary gates are reversible. So we're going to need a slightly different definition of computation to suit this reversibility condition.

Specifically, we want to define computation as something that takes an $n$-bit input and gives an $n$-bit output, where the $n$ is the same in both cases:

$$n \text{ bit} \longrightarrow \boxed{\phantom{xxxx}} \longrightarrow n \text{ bit}$$

This looks like a more restrictive version of computation than before, but it isn't necessarily so. We also want each unique input to give a unique output, and vice versa — again seemingly more restrictive, but again not necessarily so, because we can just choose $n$ to be large enough to forgive all the sins.

Specifically, take $n$ to be our previous $n_i + n_o$:

$$n = n_i + n_o$$

Then our computation takes in not just $x$, but $x$ together with a bunch of zeros — a blank variable where we're going to write our output — and the output is a copy of $x$ with the output written on the blank variables:

$$x, 00\ldots \longrightarrow x, f(x)$$

So every unique input does have a unique output, enforced in a very simple way, just by keeping a copy of the input alongside the output.

If we take reversible gates and implement a function like this — say, a computation that takes $x$ and turns it into $f(x)$ — you could compile that down to NAND gates, then implement those with Toffolis (the reversible form of the NAND gate). Implementing the function this way, keeping a copy of the output, you'll find it's also reversible, in that each unique output has a unique input. That happens automatically because you're building it out of reversible gates — that condition is enforced naturally.

---

## Writing this in quantum form

Let's now write this in a more quantum form. What we want from our computation is the ability to take an input expressed as a bit string, but written in qubits. If it's an $n_i$-bit string, we use $n_i$ qubits — so that's a tensor product of $n_i$ qubits hiding inside the simple-looking $|x\rangle$. We tensor that with a bunch of zeros, specifically $n_o$ of them:

$$|x\rangle \otimes |0\rangle^{\otimes n_o}$$

We want our computation to take such a state and rotate it into a state which still has the input expressed as a bit string, but also has the output expressed as a bit string. And since it's a reversible process, this can be implemented by a unitary:

$$|x\rangle \otimes |0\rangle^{\otimes n_o} \longrightarrow |x\rangle \otimes |f(x)\rangle$$

So we want to find unitaries that provide this sort of rotation. If universality for classical computers means the ability to implement any function $y = f(x)$ for a given function, universality for quantum computers means the ability to implement any unitary $U_f$ — an $n$-qubit unitary that reproduces this function, taking a bit string expressed in qubits and writing down the corresponding output:

$$U_f : |x\rangle \otimes |0\rangle^{\otimes n_o} \longrightarrow |x\rangle \otimes |f(x)\rangle$$

For any possible function, for any possible number of qubits, if we can create these corresponding unitaries, we can reproduce computation in exactly the same way a classical computer does — and we are universal.

However, restricting ourselves to unitaries that specifically reproduce this binary-function form is an unnecessary complication — it doesn't actually make anything simpler or make more sense. We can be much more general and much simpler in our definition of universality for quantum computers:

$$y = f(x) \qquad\qquad U_f$$

**Universality means we can reproduce any arbitrary unitary acting on $n$ qubits.**

$$U_f \; (n \text{ qubits})$$

For any number of qubits, if we can find some way to implement any arbitrary unitary, we have what we'd call a universal quantum computer. It's just a consequence of that that we could use these unitaries to implement classical computations, and therefore, in theory, run everything from Excel to Mario Kart. But because we're defining it in terms of unitaries, we can also do more general things.

In this lecture we want to prove that a gate set we've already seen is sufficient for universality — sufficient for reproducing any unitary, and therefore any quantum computation, any quantum algorithm, or indeed any classical algorithm. So let's get on with doing that.

---

## The gate set: $R_x(\theta)$ and the Cliffords

I'll remind you of the gate set we looked at last week: rotations around the $x$-axis (we could use rotations around any axis, but we were looking specifically at $R_x(\theta)$ for some angle $\theta$), plus the Clifford gates — the Hadamard, $S$, and $S^\dagger$ (even without $S^\dagger$ explicitly, you can make it out of $S$'s, since it's $S^3$), and the controlled-NOT:

$$R_x(\theta),\quad H,\ S,\ S^\dagger = S^3,\ CX$$

There are different ways to express generators for the Clifford group, but this is a good one.

The first step towards "everything" is to note that $R_x$ can be expressed as $e^{i(\theta/2)X}$. Using the single-qubit Cliffords, we can transform this into $e^{i(\theta/2)Y}$, $e^{-i(\theta/2)X}$, and so on. And by using the two-qubit Clifford — the controlled-NOT — we can turn this into a two-qubit gate such as $e^{i(\theta/2)X\otimes X}$, and from there into $X\otimes Z$, $Y\otimes X$, and so on:

$$e^{i\frac{\theta}{2}X} \qquad e^{i\frac{\theta}{2}X\otimes X}$$

We can get to the point of expressing this as $e^{i(\theta/2)P}$, where $P$ is some general $n$-qubit Pauli — a tensor product of Paulis on qubits $n-1$ down to qubit $0$, each Pauli being $X$, $Y$, $Z$, or the identity:

$$e^{i\frac{\theta}{2}P}, \qquad P = P_{n-1}\otimes\cdots\otimes P_0, \qquad P_j \in \{X,Y,Z,I\}$$

So we have the ability to create a wide set of multi-qubit Paulis this way — but not every unitary can be expressed in this form. We need the ability to represent unitaries expressed in *other* forms too. The simplest such case is where we take $e^{i}$ times $(\theta/2)P$ plus $(\theta'/2)P'$, for some other Pauli $P'$ that isn't of the same tensor-string form:

$$e^{i\left(\frac{\theta}{2}P + \frac{\theta'}{2}P'\right)}$$

How can we use gates of the first kind to create gates of this second kind?

---

## Why the naive approach fails

As a naive approach, it doesn't work — but we can adapt it into something that does. The naive approach is to remember from school that $e^xe^y = e^{x+y}$. One way to prove this is via the Taylor series of each term:

$$e^xe^y = e^{x+y}$$
$$\big(1+x+O(x^2)\big)\big(1+y+O(y^2)\big) = 1 + x + y + xy + yx + \cdots$$

And you compare that to the Taylor series of $e^{x+y}$ directly. Why have I written this as $xy$ *plus* $yx$, when I could more easily have written $2xy$?

$$+\,2xy$$

Because they commute — and that's exactly the property we need to be careful of. If we continued this proof, we'd explicitly be using the fact that $x$ and $y$ commute:

$$xy = yx$$

When we're given this relation in school, we're given it for numbers, and the fact that multiplication commutes for ordinary numbers is so ingrained in us we hardly think about it. But when we have matrices, we have to be more careful — matrices do not always commute. So this relation only holds when $A$ and $B$ commute:

$$e^Ae^B = e^{A+B} \qquad \text{only if} \qquad AB = BA$$

And this is not true of Paulis in general — sometimes they commute, sometimes they anticommute. $X$ and $Y$ anticommute, for example, and therefore $e^Xe^Y \neq e^{X+Y}$. That's why the naive approach doesn't work.

---

## Why the Trotter–Suzuki approach *does* work

Now let's see why it does work. Explicitly, what we want is for

$$U = e^{i\left(\frac{\theta}{2}P + \frac{\theta'}{2}P'\right)}$$

to equal

$$U = e^{i\frac{\theta}{2}P}\,e^{i\frac{\theta'}{2}P'}$$

since we have the ability to do each of the two gates on the right separately, and just doing them both would give us this unitary. However, it doesn't work exactly, because they don't commute in general.

But what we *can* do is take the $N$th root of both sides, for some sufficiently large $N$:

$$U^{1/N} \approx e^{i\frac{\theta}{2N}P}\,e^{i\frac{\theta'}{2N}P'}$$

That's equivalent to just making the angle much smaller — $\theta/2N$ instead of $\theta/2$:

$$\frac{\theta}{2N}$$

In that case, these become approximately equal. Although on its own this isn't a very strong statement — if you take some unitary to the power of $1/N$ for very large $N$, as $N\to\infty$ it basically becomes $U^0$, and $U^0$ is the identity:

$$U^0 = I$$

So in that limit, we're really just saying something approximately equal to the identity is approximately equal to something approximately equal to the identity, times something approximately equal to the identity — not very impressive.

What's a *stronger* statement is that if we take the $N$th **power** of both sides, the approximate relation still holds:

$$U \approx \left(e^{i\frac{\theta}{2N}P}\,e^{i\frac{\theta'}{2N}P'}\right)^{N}$$

because taking the $N$th power of $U^{1/N}$ just gets you back to $U$. More explicitly, if we want this written as equal up to some error term $\delta$, the value of $N$ needed to get an arbitrarily small $\delta$ increases only *polynomially* in $1/\delta$:

$$U = \left(e^{i\frac{\theta}{2N}P}\,e^{i\frac{\theta'}{2N}P'}\right)^{N} + \delta, \qquad N = \mathrm{poly}\!\left(\frac{1}{\delta}\right)$$

So it's not just approximate — you can get as close as you like just by choosing the right number of repetitions, and that number doesn't scale horribly; it doesn't ask for too many repetitions. This is a way of taking gates of the first form and combining them into gates of the second form, and it's known as the **Trotter–Suzuki method**. We basically take very tiny slices of those gates, put them in order, and repeat many, many times. The more repetitions, and the tinier the slices, the better the approximation.

That's sufficient to explain how to do it for two Paulis — but more generally we'll have more than two terms.

---

## Any unitary is reachable: $U = e^{iH}$, $H$ decomposed into Paulis

Let's go towards the final goal: showing how to reproduce *any* unitary. Any unitary can be expressed as $e^{iH}$ for some Hermitian matrix $H$. And a Hermitian matrix, like any matrix, can be decomposed into a linear combination of Paulis with corresponding coefficients:

$$U = e^{iH}, \qquad H = \sum_j J_j P_j$$

One thing to note: if you take the Hermitian conjugate of a linear combination of matrices, you get the linear combination of the Hermitian conjugates of each — so we take the Hermitian conjugate of these Paulis, and of the coefficients, which for numbers just means the complex conjugate:

$$H^\dagger = \sum_j J_j^*\, P_j^\dagger$$

Since $H$ is Hermitian (equal to its own Hermitian conjugate), and the Paulis are Hermitian too, this relation only holds if the couplings are also "Hermitian" — which for numbers just means they have to be **real**:

$$J_j = J_j^*, \qquad H = H^\dagger, \qquad P_j = P_j^\dagger$$

So a general unitary can be written as $e^{iH}$ for some $H$ expressed as a linear combination of $n$-qubit Paulis with real coefficients. This means we can decompose each term as one of these $e^{i(\theta/2)P_j}$ gates, just using $\theta/2$ as the corresponding coupling $J_j$ for that particular $j$:

$$e^{i\frac{\theta}{2}P_j}, \qquad \frac{\theta}{2} = J_j$$

So by setting these angles to the right values, we can come up with a gate corresponding to each term using the Trotter–Suzuki method — which we just looked at for two terms, but it works for any number of terms. Stitching together all of these terms, we can come up with any arbitrary unitary.

So there's our result: using single-qubit rotations like $R_x(\theta)$ for an arbitrary angle, together with the Cliffords, we can make these big multi-qubit $e^{i(\theta/2)P}$ gates — and using the fact that a unitary can be written as $e^{i(\text{Hermitian})}$, and that a Hermitian matrix can be written as a linear combination of Paulis, then with the Trotter–Suzuki method and these gates we've created, we can recreate any unitary.

This is not necessarily the *best* way to build any given unitary in practice — you shouldn't, as your first tactic in writing a quantum algorithm, come up with the target unitary and then try to reproduce it via Trotter–Suzuki. That's a bit like the bad method of programming I mentioned earlier — writing an exponential number of conditional clauses. It's not necessarily the best way, but it *does* prove that the gate set is universal. So we can proceed with gates like $R_x(\theta)$ and the Cliffords, knowing that anything a quantum computer can do, can be done using those gates. If we build our algorithms out of those gates, we're not missing out on any fancy quantum features, because any quantum computation is a unitary, and any unitary can be made out of those gates — they are a universal gate set.

---

## Other universal gate sets

There are also other universal gate sets. For example, the Cliffords plus *anything* non-Clifford. $R_x(\theta)$ is one example of something non-Clifford — but it's really an infinite number of gates, since it can take any angle. We could instead take, say, the $T$ gate, which is rotation around the $z$-axis by an angle of $\pi/4$:

$$\text{Clifford} + T = R_z(\pi/4)$$

If we have the $T$ gate as well as all the Cliffords, we can also prove this is universal. It's a bit of a horrible and awkward proof, so we won't do it here — but you can.

One I find even more surprising: another universal gate set is the **Toffoli**, which (as you may remember, since it can do AND and NAND) is essentially universal for classical computation on its own already, given bits initialised to $1$s to unlock its NAND power. The only thing you need to add to make it universal for quantum computation is the **Hadamard**:

$$\text{Toffoli} + H$$

Using these two together, you can do any arbitrary single-qubit rotation — which is kind of mind-blowing. It's not necessarily how you'd want to actually *build* a quantum computer, but the very fact this can be proven is an interesting fact.

The "Clifford plus anything non-Clifford" result is actually used quite a lot in fault-tolerant quantum computing plans, because — for reasons we'll look at more later in the course — it's quite easy to build versions of Clifford gates that are hardly affected by noise, that we can easily identify and correct imperfections in. For non-Clifford gates, especially a continuous rotation like $R_x(\theta)$ by some angle, this is much harder — a rotation by $\theta$ is a valid gate, but so is a rotation by $\theta$ plus some infinitesimal amount. How do you distinguish the correct gate from a slight over-rotation, when the two are continuously related to each other? It's a very difficult thing to distinguish. But because we can just use a single non-Clifford gate, all we need to do is hone the ability to do that *one* thing perfectly — and if we're slightly over-rotated from that gate, we know that's incorrect and needs correcting. We then use that one, perfectly-honed gate to bring in all the non-Cliffordness the computation needs.

That's enough about universality. We've proven that our quantum computer can do everything. What remains is to prove it can do specific things, and that it can do them better than a classical computer.

---

## A motivating example: simulating spin-1/2 systems

One motivating example of a quantum computer doing something better than a classical computer actually uses exactly the same example we've used to prove universality.

In physics there are various physical systems we might be interested in. One is spin-1/2 particles, like electrons — these have a property called spin, described by a two-dimensional quantum system with states of spin up and spin down in each of the normal real-world directions. Another is photons — described in terms of position by a continuous quantum variable, but they also have polarisation, described by a discrete quantum variable: vertical or horizontal, or (an equally valid basis) $45°$-rotated polarisations, or (another valid basis) circularly polarised states. So that's another two-dimensional quantum system. And of course our favourite two-dimensional quantum system is an abstract one that isn't physical at all: the qubit, with basis states $|0\rangle$ and $|1\rangle$ (the $Z$ basis), the $X$ basis $|+\rangle,|-\rangle$, and the $Y$ basis:

$$\text{Spin-}\tfrac12: \ |{+}\rangle,|{-}\rangle \qquad \text{Photon}: \ |{\circlearrowleft}\rangle,|{\circlearrowright}\rangle \qquad \text{Qubit}: \ |0\rangle,|1\rangle$$

What a coincidence they're all written here — this is just to impress upon you that the mathematics, the theory, behind qubits is exactly the same as the theory behind spin-1/2 particles. That's one reason some approaches to building quantum computers use spin-1/2 particles as qubits. It's also the same as the theory behind photon polarisation, which is why some approaches use that instead.

So, if you want to do the physics of a bunch of spin-1/2 particles sitting on, say, some square lattice, interacting with each other according to their spin values, that's something we can seek to represent on a classical computer, or on a quantum computer. Which is going to be best?

The length of the state vector for $n$ spin-1/2 particles — the number of numbers you have to write down — is $2^n$: it scales exponentially with the number of particles, just to write down the state.

$$2^n$$

But how many *qubits* do you need to write down the state of $n$ spin-1/2 particles? Just $n$:

$$n$$

That's an exponential advantage, simply because you're encoding the information in a system that's more naturally expressed that way, instead of trying to write it down in terms of classical variables.

And if you want to simulate the time evolution on a classical computer, you still have to keep track of that horrible number of numbers. But in quantum computing, time evolution corresponds to a unitary, and that unitary can be expressed as $e^{iH}$, where $H$ here is indeed Hermitian, but it's also called $H$ because it's the **Hamiltonian** — the operator describing the interactions between these spin-1/2 particles, naturally written as a set of interaction terms expressed in terms of Paulis and corresponding couplings:

$$U = e^{iH}, \qquad H = \sum_j J_j P_j$$

So the description of our problem is exactly one of these Hamiltonians. What we want is that time evolution, and we know we have a polynomial number of gates that can simulate it to arbitrary accuracy. So simulating the time evolution of a quantum system is a computational problem that would take exponential resources in general for a classical computer — assuming no special symmetries let you simplify things — but for a quantum computer, because it naturally speaks the language of spin-1/2 particles, it can do it in a much more efficient way.

So we've shown that quantum computing is universal, how to get universality, and found a motivating example for a problem where a quantum computer could do better than a classical one. Now we can study more generally what quantum computing is, how it approaches problems, and what advantages it can have over classical computing — both for problems relevant to physics and chemistry, where the quantum-ness of the computer is doing the quantum-ness in the problem, and also more broadly for problems that have nothing to do with physics.

---

## Oracles: Boolean and phase

As we go into some of these examples — especially the early, simple examples of quantum advantage we'll go through — we'll learn the concept of an **oracle**. An oracle is just a fancy way of saying "a time when we need a quantum computer to do classical computation within, as part of, its quantum computation." The classic forms are **phase oracles** and **Boolean oracles**.

The Boolean oracle is exactly what we saw earlier — call it $U_f^b$. It takes an input encoded in a bunch of qubits, and a bunch of blank qubits (to the power $n_o$), and turns this into the input unchanged, but with the output written on the other register:

$$U_f^b \; |x\rangle\otimes|0\rangle^{\otimes n_o} = |x\rangle\otimes|f(x)\rangle$$

We've got two quantum registers — $n_i$ qubits and $n_o$ qubits — and the oracle effectively doesn't do anything to the input register, but does act on the output register. The reason we need to represent this quantum-mechanically is that there are times in computations where we want to act not just on some single $x$, but on a *superposition* of $x$'s, in order to get interference effects — so we start with a superposition and want a superposition of different outputs out:

$$U_f^b \sum_x c_x\, |x\rangle\otimes|0\rangle^{\otimes n_o} = \sum_x c_x\, |x\rangle\otimes|f(x)\rangle$$

That's a Boolean oracle.

The other kind is a **phase oracle**. It acts on a register of qubits encoding the input, and gives back the same register in the same state, but with a phase. Applied to a single basis state, this is just a global phase and has no effect — but applied to a superposition, it becomes a *relative* phase, and becomes relevant. The phase is $(-1)^{f(x)}$ — here we assume $f$ gives a binary result out (like our cat picture):

$$U_f^p\,|x\rangle = (-1)^{f(x)}\,|x\rangle, \qquad f(x)\in\{0,1\}$$

If $f(x)=0$ the phase is $(-1)^0=+1$; if $f(x)=1$ the phase is $(-1)^1=-1$.

---

## Phase kickback: building a phase oracle from a Boolean one

Even though these two kinds of oracle look quite different, they're actually closely related, and we can use Boolean oracles to implement phase oracles. The trick is to take a Boolean oracle for a given function and apply it to the input state tensored with the $|-\rangle$ state:

$$U_f^b \; |x\rangle\otimes|-\rangle$$

Why does this work? The action of the Boolean oracle takes $|x\rangle\otimes|0\rangle$ to $|x\rangle\otimes|0\rangle$ if $f(x)=0$, and to $|x\rangle\otimes|1\rangle$ if $f(x)=1$:

$$|x\rangle\otimes|0\rangle \longrightarrow |x\rangle\otimes|0\rangle, \ f(x)=0 \qquad\qquad |x\rangle\otimes|1\rangle, \ f(x)=1$$

It's like a generalised form of the controlled-NOT — but instead of just looking at a control qubit and checking if it's $0$ or $1$, it looks at the control *register* and asks: is this an $x$ that gives $f(x)=0$, or an $x$ that gives $f(x)=1$? In the case $f(x)=1$, it applies an $X$ to flip the target qubit from $0$ to $1$.

Now, we know that applying $X$ to the $|-\rangle$ state gives $|-\rangle$ back with a phase of $-1$:

$$X|{-}\rangle = -|{-}\rangle$$

So, doing this "controlled-NOT"-like operation, the control either does nothing to the $|-\rangle$ (no phase induced) or applies an $X$ to it (picking up a phase of $-1$). What we find is:

$$U_f^b\;|x\rangle\otimes|{-}\rangle = (-1)^{f(x)}\,|x\rangle\otimes|{-}\rangle$$

— depending on whether the phase has been induced or not — and the $|-\rangle$ remains completely unaffected. Which means if the $|x\rangle$ part was in a superposition, it stays in exactly that superposition, unentangled from $|-\rangle$. So we can effectively ignore the $|-\rangle$ register entirely, and we find that this **phase kickback** method means the Boolean oracle has the effect of a phase oracle. So wherever we need phase oracles, if we can implement a Boolean oracle, we get ourselves a phase oracle too.

---

## Implementing a Boolean oracle without garbage

So — how do we implement a Boolean oracle? I implied earlier that the ability to do a classical computation which takes a given $x$ and gives back $f(x)$ is sufficient to also do a quantum version, because you can take the program implementing that, compile it down to NAND gates, replace the NANDs with Toffolis, and get something that takes $x$ and a bunch of zeros and gives you $|x\rangle\otimes|f(x)\rangle$:

$$x \longrightarrow f(x) \qquad\qquad |x\rangle\otimes|0\ldots\rangle \longrightarrow |x\rangle\otimes|f(x)\rangle$$

However, this isn't quite true, because one thing we often forget is that in the course of a classical computation, we typically use intermediate variables that get thrown away over the course of the program. If we account for these, they show up as what we could call **garbage** — the undeleted remnants of a computation:

$$|x\rangle\otimes|0\ldots\rangle\otimes|0\ldots\rangle \longrightarrow |x\rangle\otimes|f(x)\rangle\otimes|g(x)\rangle$$

In classical computation it's perfectly fine to do a *deleting* operation — something that, expressed in quantum terms, would keep a $0$ as $0$ but turn a $1$ into a $0$:

$$|0\rangle\langle0| + |0\rangle\langle1|$$

Such an operation isn't Hermitian — it can't be realised by a *unitary* gate. If we wanted to do this in a computation, we'd have to use something like measurement — measure a qubit, and if it's $1$, flip it down to $0$. Or, in a case where the $0$ and $1$ states have different physical energies, let the qubit interact with a thermal bath and cool down to the $0$ state. But that too is physically similar to a measurement — it's almost as if the thermal bath is measuring the qubit and then deciding whether to take the energy out. This will not sit well with any interference effects: lots of quantum algorithms rely on delicate interference, and using non-unitary gates will mess that up.

So we need some way to get rid of this garbage, without wrecking the interference effects the algorithm needs.

---

## Uncomputation

Let's assume we have a unitary $U$ that does this computation, with garbage:

$$U : |x\rangle\otimes|0\ldots\rangle\otimes|0\ldots\rangle \longrightarrow |x\rangle\otimes|f(x)\rangle\otimes|g(x)\rangle$$

When we have a unitary, we typically also have the ability to do its Hermitian conjugate — because whatever sequence of gates makes up $U$ (say $U = AB$, so $U^\dagger = B^\dagger A^\dagger$), as long as we can do the Hermitian conjugate of each individual gate, we can just reverse the order and conjugate each one to get $U^\dagger$:

$$U = AB \qquad U^\dagger = B^\dagger A^\dagger$$

So usually if we can do a gate, we can also do its Hermitian conjugate. This means we can take something with garbage and delete the garbage *unitarily*, because applying $U^\dagger$ to $|x\rangle\otimes|f(x)\rangle\otimes|g(x)\rangle$ gets us back to $x$ and a bunch of zeros, both for the register that held the output and the register that held the garbage:

$$U^\dagger\;|x\rangle\otimes|f(x)\rangle\otimes|g(x)\rangle = |x\rangle\otimes|0\ldots\rangle\otimes|0\ldots\rangle$$

So we've got rid of the garbage — but at the cost of also getting rid of the output, which is a problem, because we need the output.

---

## Copying the output first (and why the no-cloning theorem doesn't block this)

So the idea is: before we "uncompute" to get rid of the garbage, why don't we just copy-paste our output first? For this we need to be careful, because of the **no-cloning theorem**.

Does there exist a unitary that can be applied to a state — say a single-qubit state $|\psi\rangle$ — plus another qubit in a well-known state like $|0\rangle$, that creates two copies of $|\psi\rangle$?

$$U\;|\psi\rangle\otimes|0\rangle = |\psi\rangle\otimes|\psi\rangle$$

The answer depends on what $|\psi\rangle$ is. If we completely and utterly know what the state is, this is fine — we know a unitary that creates that one specific state, and we apply it to the other qubit and we have two of them. However, if we have *no* idea what the state $|\psi\rangle$ is, and we want *one single* unitary that can be given any arbitrary state and copy it, that is *not* possible — no such unitary exists. This is the no-cloning theorem.

So that's two extremes: if you know exactly what the state is, designing a copier for that one specific state is possible; if you want one unitary that copies *any* arbitrary unknown state, that's not possible.

An in-between case: designing a unitary that copies a *partially* unknown state — say, we know it's going to be either $|0\rangle$ or $|1\rangle$, and we want a single unitary that can copy whichever one it is, without needing to design a specific unitary for each:

$$|\psi\rangle\otimes|0\rangle = |\psi\rangle\otimes|\psi\rangle, \qquad |\psi\rangle \in \{|0\rangle,|1\rangle\}$$

When we know the state is drawn from a set of *orthogonal* states, we *can* do this — there is a way to copy an unknown state from a set of orthogonal states. The unitary we need for this is one we already know well: the **controlled-NOT**. It takes $|00\rangle \to |00\rangle$ and $|10\rangle \to |11\rangle$:

$$C_x: \ |00\rangle \to |00\rangle, \qquad |10\rangle \to |11\rangle$$

Whatever is on the control gets copied onto the target, assuming the target starts in state $|0\rangle$. So we can copy *bits*, and that's perfectly valid.

---

## Putting it together: compute, copy, uncompute

So we can do a process where we initially have a register of qubits with our input $x$, then a register of zeros (for the output), then another register of zeros (for the garbage), then another register of zeros (where we'll park a clean copy of the output). We apply our computation $U$, which gives back $x$ again, overwrites the second register of zeros with the output $f(x)$, overwrites the third with the garbage $g(x)$, and leaves the last register untouched, since $U$ doesn't act on it:

$$|x\rangle\otimes|0\ldots\rangle\otimes|0\ldots\rangle\otimes|0\ldots\rangle \ \xrightarrow{\ U\ }\ |x\rangle\otimes|f(x)\rangle\otimes|g(x)\rangle\otimes|0\ldots\rangle$$

Then we apply a bunch of controlled-NOTs, one for each qubit in the output register, targeted onto the corresponding qubit of that final, blank register — copying $f(x)$ bit by bit until we have $x$, $f(x)$, $g(x)$, and a second copy of $f(x)$:

$$\xrightarrow{\ \otimes^{n_o}C_x\ }\ |x\rangle\otimes|f(x)\rangle\otimes|g(x)\rangle\otimes|f(x)\rangle$$

Once we've safely got our copy of the output in the bag, we apply the **uncomputation** — $U^\dagger$ — to undo the original computation, going back to just $x$ and two blocks of zeros, getting rid of the unwanted garbage, and leaving our safe copy of the output exactly where it was:

$$\xrightarrow{\ U^\dagger\ }\ |x\rangle\otimes|0\ldots\rangle\otimes|0\ldots\rangle\otimes|f(x)\rangle$$

The entire effect of this — if you just recheck the registers — is exactly the Boolean oracle we wanted, $U_f^b$, sitting on the input register and the final output register:

$$U_f^b : |x\rangle\otimes|0\ldots\rangle \longrightarrow |x\rangle\otimes|f(x)\rangle$$

So: with the ability to do any classical computation, and compile it down to, say, NAND gates, we can use this **compute–copy–uncompute** trick to build the corresponding Boolean oracle, and hence the corresponding phase oracle. So when we come across quantum algorithms that need oracles in the next few sessions, you'll know exactly how those are built — if you want the details of actually implementing them, we usually leave that as an exercise to the reader, or to whoever's actually implementing it once we have fault-tolerant quantum computers.

You've also seen in this lecture that we can build universal gate sets from just a few simple gates — rotations around the $x$-axis for a single qubit, plus the Clifford gates — and with those, we can do any computation. So it now just remains to look at specific forms of computation, which is what we'll be doing in the next few sessions.

That's all for this time. Thank you for listening.
