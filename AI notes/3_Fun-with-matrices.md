# 5 — Fun with Matrices

*Dr James Wootton, Moth Quantum*

> **Transcription note:** this is a transcript-based rewrite, using James's actual spoken narration (lightly cleaned up — filler words, mid-take corrections, and recording asides removed) matched against the whiteboard's equation order.

---

## Introduction

Hello and welcome to this lecture, which I like to call "Fun with Matrices." It's basically a disjoint-seeming set of facts about the kind of matrices that are important to us in quantum computing, which we're going to use to help us analyze quantum gates and how they can be combined into quantum algorithms.

---

## The Hermitian conjugate

So let's begin with the Hermitian conjugate. Here we have an example of a two-by-two matrix — an arbitrary two-by-two matrix:

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

On this we're going to define the notion of a Hermitian conjugate. A Hermitian conjugate is defined in terms of two other properties.

One is the **transpose**. The transpose of a matrix is where you basically flip the matrix along this axis: everything below goes above, everything above goes below, and everything on the diagonal stays where it is. So for a two-by-two matrix, the diagonal elements stay where they are, but the off-diagonal elements get swapped:

$$M^T = \begin{pmatrix} a & c \\ b & d \end{pmatrix}$$

We also define the **complex conjugate**, which is simply the complex conjugate of all the elements:

$$M^* = \begin{pmatrix} a^* & b^* \\ c^* & d^* \end{pmatrix}$$

Now, if we do both of these things — take the complex conjugate and then the transpose, or equivalently take the transpose and then the complex conjugate — we get the **Hermitian conjugate**:

$$M^\dagger = (M^*)^T = (M^T)^* = \begin{pmatrix} a^* & c^* \\ b^* & d^* \end{pmatrix}$$

You'll be hearing more about that.

---

## The Paulis

Now let's move on to introduce the Paulis. The Paulis are the simplest, but also arguably the most important gates — ones that come up all of the time. They are $X$, $Y$, and $Z$. And in some contexts an honorary Pauli is the identity, $I$.

Each of them has the property that if you square it, you get the identity — and this even holds for the honorary Pauli:

$$X^2 = Y^2 = Z^2 = I^2 = I$$

And for any pair of them, we have anticommutation:

$$XY = -YX, \qquad XZ = -ZX, \qquad ZY = -YZ$$

Also, if you multiply two of them together, you get the third one. What we find is that:

$$ZX = iY, \qquad \text{while} \qquad XZ = -iY$$

I leave it as an exercise to the viewer to work out all the rest of them. But up to a global phase, multiply two of them together and you get the third one. So these are the Paulis.

*(This confirms the whiteboard's second relation should read $XZ = -iY$, not $XZ = +iY$ as it appears written — a slip of the pen while talking, per the narration above.)*

---

## Any matrix as outer products — and in terms of Paulis

Now let's return to our general single-qubit matrix — although the properties we're going to look at also hold for any arbitrary matrix. So $a, b, c, d$: this can be written as $a$ times the matrix which has only a single element of one, and the rest of them are zero — and the one is exactly where we want this $a$ in our matrix — plus $b$ times the matrix which has a one only where we want the $b$, and so on for $c$ and $d$.

The interesting thing is that all of these can be written out as an outer product. And they could also be written in terms of Paulis.

So let's look at $\begin{pmatrix}1&0\\0&0\end{pmatrix}$. This can be written as the outer product of the column vector and the row vector — the outer product of $|0\rangle$ with itself. And the next one, for $b$, $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, can be written as the outer product of $|0\rangle$ with $\langle1|$, and so on:

$$M = a\,|0\rangle\langle0| + b\,|0\rangle\langle1| + c\,|1\rangle\langle0| + d\,|1\rangle\langle1|$$

This just proves something we've already really been using: that you can always write a matrix out in terms of outer products. Before, we've been using properties of the matrices we were looking at to know how to write down those outer products — but this is a way of doing it which holds in all times and in all places, for any matrix, regardless of what its properties are. Because we're just singling out each of the elements and writing down an outer product that corresponds to that particular element.

And this holds for multi-qubit matrices too — you can write down the outer product of $|00\rangle$ with itself, for example, which is a four-by-four matrix with a one in the top corner and zeros everywhere else.

---

## Writing those outer products in terms of Paulis

We can also write down those exact outer products in terms of Paulis, which is going to show us that everything can be written in terms of Paulis as well.

The outer product of $|0\rangle$ with itself, $\begin{pmatrix}1&0\\0&0\end{pmatrix}$, can be written as $(1,1) + (1,-1)$ along the diagonal — so that the element we don't want cancels. The first matrix in that sum is the identity, and the second is $Z$:

$$|0\rangle\langle0| = I + Z$$

Similarly, we can write down the outer product of $|1\rangle$ with itself as:

$$|1\rangle\langle1| = I - Z$$

*(Note: as spoken, these two don't quite add up dimensionally without a normalizing $\tfrac12$ — the standard identity is $|0\rangle\langle0|=\tfrac12(I+Z)$. It's dropped both on the board and in the narration here, so it may be intentional shorthand for this lecture; worth a quick gut-check before it goes to the slides.)*

But how about something like the outer product of $|1\rangle$ with $\langle0|$? Well, this can be written as $X$ times the outer product of $|0\rangle$ with $\langle0|$, because of course that $X$ times $|0\rangle$ gives us the $|1\rangle$ we desire. And that means it's $X$ times $(I+Z)$: $X$ times identity is just $X$, and $X$ times $Z$ is $-iY$. So:

$$|1\rangle\langle0| = X(I+Z) = X - iY$$

This gives us two more of these outer products written in terms of Paulis, and now we've even got a special guest star from $Y$. The outer product of $|0\rangle$ with $\langle1|$ comes out the same way, but with $+iY$:

$$|0\rangle\langle1| = X + iY$$

Using these relations, we can write any general matrix down as:

$$M = \alpha I + \beta X + \gamma Y + \delta Z$$

(I'm not using $a, b, c, d$ as before, because these aren't going to be the same numbers — these aren't the matrices that single out single elements. But there is a relationship between those numbers, which I'll leave for you to investigate yourself.) Hopefully it should be clear now that we can also write down matrices as sums of Pauli matrices.

---

## The same trick, tensored up

Similarly, if you have a term like $|00\rangle\langle00|$, this is the tensor product of $|0\rangle\langle0|$ with itself — and each of those can be written as $I + Z$. Expand this out, and:

$$|00\rangle\langle00| = (I+Z)\otimes(I+Z) = I\otimes I + I\otimes Z + Z\otimes I + Z\otimes Z$$

You can do this for all other possible two-qubit outer products, and also multi-qubit outer products. So it's also true that multi-qubit matrices can be written as sums of Paulis — but the notion of a Pauli gets extended to include tensor products of Paulis like these, plus, as the honorary Pauli, the identity.

So that's how we can write down matrices in terms of outer products, but also in terms of Paulis.

---

## Unitary matrices

Now let's talk about two specific classes of matrix which are defined in relation to the Hermitian conjugate.

One class of matrices is a class for which multiplying the matrix by its Hermitian conjugate gives us the identity — and it doesn't matter which way around you do it. If a matrix satisfies this property, we call it **unitary**:

$$UU^\dagger = \mathbb{1} = U^\dagger U$$

There are a few fun facts about unitaries. Suppose you've got a state $|\psi\rangle$ that's normalized, so $\langle\psi|\psi\rangle = 1$. Now someone comes along and applies $U$ to $|\psi\rangle$, giving you some new state $|\varphi\rangle$. Is $|\varphi\rangle$ still normalized?

The inner product of $|\varphi\rangle$ with itself — and we already noted before that the effect $U$ has on the ket form of the state, $U^\dagger$ has the same effect on the bra form — is the inner product $\langle\psi|U^\dagger U|\psi\rangle$. But because $U^\dagger U = \mathbb{1}$, putting an identity in the middle of that just means we come out with the inner product of $|\psi\rangle$ with itself, which is one:

$$\langle\varphi|\varphi\rangle = \langle\psi|U^\dagger U|\psi\rangle = \langle\psi|\psi\rangle = 1$$

So if you apply a unitary to a normalized state, you get a normalized state back. But actually the property is more general than this.

If we have a couple of states, $|\psi_0\rangle$ and $|\psi_1\rangle$, and we know their inner product — and act on both of these with $U$, turning $|\psi_0\rangle$ into $|\varphi_0\rangle$ and $|\psi_1\rangle$ into $|\varphi_1\rangle$ — then the inner product of $|\varphi_0\rangle$ and $|\varphi_1\rangle$ will be exactly the same as that of $|\psi_0\rangle$ and $|\psi_1\rangle$, with exactly the same proof as before:

$$\langle\varphi_0|\varphi_1\rangle = \langle\psi_0|\psi_1\rangle$$

What this means is that if $|\psi_0\rangle$ and $|\psi_1\rangle$ are, for example, orthogonal — if they represent a basis we can use to describe our system — then the new states $|\varphi_0\rangle$ and $|\varphi_1\rangle$ will also represent a basis. So we can think of unitaries as being transformations between different orthogonal bases: whatever basis we care about, we can apply the unitary to it and find out what basis it turns that into.

---

## Worked example: the $X$ gate as a basis transformation

Let's look at a few examples of this. One is $X$. We can apply this to our favorite basis, the $|0\rangle/|1\rangle$ basis. What we find is it turns $|0\rangle$ into $|1\rangle$, and $|1\rangle$ into $|0\rangle$:

$$X: |0\rangle \to |1\rangle, \qquad |1\rangle \to |0\rangle$$

We have started off with a basis, and we have ended up with a basis — all we've actually done is changed the ordering of the states, but it's still a valid effect.

We could also try $X$ on another basis: the $X$-basis states $|+\rangle$ and $|-\rangle$. Then we find $X$ turns $|+\rangle$ into $|+\rangle$, and gives $|-\rangle$ a phase of $-1$:

$$X: |+\rangle \to |+\rangle, \qquad |-\rangle \to -|-\rangle$$

That's another valid basis — these basis states only differ by global phases, but it's still a valid effect.

And of course we've been using exactly these basis transformations as a way of writing down the effects of $X$: we've been writing $X = |0\rangle\langle1| + |1\rangle\langle0|$, because this pair of outer products describes exactly this effect. And similarly, we can write $X$ in its own eigenbasis:

$$X = |+\rangle\langle+| - |-\rangle\langle-|$$

---

## The general recipe for a unitary

With any unitary, if it's turning some states $|\psi_0\rangle$ and $|\psi_1\rangle$ — which form a basis, so they're orthogonal — into some states $|\varphi_0\rangle$ and $|\varphi_1\rangle$, then this is a way of writing down that unitary:

$$U = |\varphi_0\rangle\langle\psi_0| + |\varphi_1\rangle\langle\psi_1|$$

When we have multi-qubit states, we just have more states in our basis — it's become bigger, but it's all equally valid.

---

## Eigenbasis and spectral form

Now one particular basis of interest for any unitary is the **eigenbasis** — the basis for which the unitary has no effect but to give global phases. And unitaries always have an eigenbasis.

So for any unitary $U$, we can find a set of states, which I'm going to call $|h_j\rangle$ (the reason for using $h$ will become clear later), such that $U$ acting on these $|h_j\rangle$s gives us just a global phase. It's very limited in what it can do — it can only multiply by a global phase, just like $X$ applied to $|-\rangle$ gives a phase of $-1$. And global phases can always be written as $e^{i}$ times some real number — our eigenvalue, parametrized by that real number:

$$U|h_j\rangle = e^{ih_j}|h_j\rangle$$

This also shows us how $U^\dagger U$ comes out as the identity: for $U^\dagger$, the effect is to give us the complex conjugate of the phase, and everything else is the same eigenbasis:

$$U^\dagger|h_j\rangle = e^{-ih_j}|h_j\rangle$$

And we can write this all in what we call **spectral form**. When we're using the eigenbasis, the mapping of the original basis to the new basis is all nice and diagonal, because we've got the same state on both sides, differing only by the eigenvalue — summed over all of our basis states:

$$U = \sum_j e^{ih_j}\,|h_j\rangle\langle h_j|$$

That's going to come in handy.

---

## Hermitian matrices

Now let's move on to the other special kind of matrix defined in relation to the Hermitian conjugate: **Hermitian matrices**, which are matrices equal to their own Hermitian conjugate:

$$H = H^\dagger$$

Hermitian matrices can also be written in spectral form — they also have eigenstates — but in this case, applying a Hermitian matrix to some state does not necessarily give us a valid state. One example: $\begin{pmatrix}1&0\\0&0\end{pmatrix}$ is Hermitian (transpose it, conjugate it, you get the same thing back), but if you apply this matrix to the $|1\rangle$ state, you get the two-dimensional zero vector — not a normalized state at all.

So we don't necessarily get normalized states out of these. For the eigenstates — call them $|h_j\rangle$ again, which makes more sense here since $h$ is for "Hermitian" — applying $H$ gives us some number times $|h_j\rangle$. But in spectral form, one thing we'll note is that these numbers have to be **real**:

$$H|h_j\rangle = h_j|h_j\rangle, \qquad h_j = h_j^*$$

Why do they have to be real? The Hermitian conjugate is a basis-independent quantity. The transpose depends on what basis you perform it in, and so does the complex conjugate — but the combination of these two things isn't basis-dependent. It doesn't matter which basis you write your matrix down in; the Hermitian conjugate you get out is exactly the same.

So if we do the transpose in the eigenbasis — and for outer products, a transpose just means swapping the two states in each term — using the spectral form, the two states are already the same, so the transpose has no effect. What's left is to do the complex conjugate, and in the eigenbasis that means taking the complex conjugate of the eigenvalues. For the Hermitian matrix to equal its own Hermitian conjugate, the complex conjugates of the eigenvalues have to equal the eigenvalues themselves — which means these values have to be real. So:

$$H = \sum_j h_j\,|h_j\rangle\langle h_j|$$

---

## $U = e^{iH}$

So we've got two kinds of matrices: unitary matrices, which in spectral form can be written as $e^i$ times a real number for each eigenstate, and Hermitian matrices, which can be written as a real number times the eigenstate projector — and this is why I've used $|h_j\rangle$ for the eigenstates of both, because we can see a correspondence between these two things. Both are parametrized by a set of real numbers — in one case used directly as eigenvalues, in the other used to define complex numbers of magnitude one — but in both cases they exist.

This means that for any unitary we can define a corresponding Hermitian, and for any Hermitian we can define a corresponding unitary. The way we write this down is to say we can get a unitary which is $e$ to the $i$ times a Hermitian:

$$\boxed{U = e^{iH}}$$

— where the exponential here is defined the way we always define the exponential of a matrix, via its Taylor series. If you apply that to something in spectral form, when you square the outer products you get the original outer product back, and when you multiply terms from different eigenstates you get zero because they're orthogonal. What it means is you just get the exponentials of the eigenvalues — exactly what we want: you take the complex exponential of $H$, and you get the matrix with exactly the same eigenstates, whose eigenvalues are exponentials of the original eigenvalues.

---

## Cliffords

Now let's talk about Cliffords. There are different families of gates useful for different things in quantum computation. We've already talked about the Paulis — $X, Y, Z$, and the identity as an honorary Pauli.

Another set of gates are the **Cliffords**, which map Paulis to Paulis by conjugation. If we conjugate a Pauli by a Clifford — applying the gate on one side and its Hermitian conjugate on the other — what we get is a Pauli, up to some phase.

The unitary that does this for $X$, up to sign, is the **Hadamard**:

$$HXH = Z, \qquad HZH = X, \qquad HYH = -Y$$

That's not the only example of a Clifford gate. Another is $S$:

$$SXS^\dagger = Y, \qquad SYS^\dagger = -X, \qquad SZS^\dagger = Z$$

$S$ and $Z$ commute, so conjugating $Z$ by $S$ just gives you plain old $Z$ back. So with Cliffords we can transform Paulis into each other.

A Pauli on its own is pretty boring and cheap, so you might wonder why we'd want to do this — but we'll see some good uses of this later. I should note that the notion of a Pauli also exists for multi-qubit systems: a tensor product of Paulis. So here's a two-qubit example. We can have the equivalent of what we saw before, which just turns $X\otimes I$ into $Z\otimes I$. But we can have something more interesting: a different unitary that takes $X\otimes I$ and turns it into $X\otimes X$:

$$U(X\otimes I)U^\dagger = X\otimes X$$

And in fact, you already know the gate that does that — it's the **controlled-NOT**.

Most of the gates we've looked at so far are Cliffords, in fact. One more example of Cliffords: the Paulis themselves are Cliffords too. If you do $XZX^\dagger$, say — and Paulis are Hermitian, so this is the same as $XZX$ — commuting the $X$'s through gives us $-Z X^2$, and $X^2$ is the identity, so that gives us $-Z$:

$$XZX^\dagger = XZX = -ZX^2 = -Z$$

So Paulis transform Paulis to Paulis too, just in a rather boring way — giving phases due to the anticommutation.

So we have Paulis, and then we have Cliffords, which include the Paulis but also include other gates. And then we have the next set of gates: **non-Cliffords** — everything else.

---

## Non-Cliffords: rotation gates

An example of a non-Clifford gate is a rotation around the $x$-axis by some angle. If it's $\pi$, you get $X$, which is a Clifford. If it's $\pi/2$, you also get a Clifford. Everything else is non-Clifford.

Recall that any unitary can be represented as the matrix exponential of a Hermitian, $e^{iH}$. What's the Hermitian matrix corresponding to rotation around the $x$-axis by some angle? It's $X$ times $\theta/2$:

$$R_x(\theta) = e^{iX\theta/2}$$

And similarly:

$$R_y(\theta) = e^{iY\theta/2}, \qquad R_z(\theta) = e^{iZ\theta/2}$$

---

## Using a Clifford to trade one rotation for another

If we have the ability to do one of these rotations, but want another, and we also have Clifford gates, this is one place Cliffords become useful. Say we want to do $R_z(\theta)$. This equals $e^{iZ\theta/2}$ — but we can also implement it with a Hadamard conjugating $e^{iX\theta/2}$:

$$R_z(\theta) = e^{iZ\theta/2} = H\,e^{iX\theta/2}\,H$$

The reason: the only difference between $e^{iZ\theta/2}$ and $e^{iX\theta/2}$ is their eigenstates — the unitary and its Hermitian generator share an eigenbasis, so the eigenstates of $e^{iZ\theta/2}$ are the $|0\rangle,|1\rangle$ eigenstates of $Z$, and the eigenstates of $e^{iX\theta/2}$ are the eigenstates of $X$. All we need to do is transform the state from the eigenstates of $X$ to the eigenstates of $Z$, and that basis transformation is exactly what a Hadamard does.

So we can take the ability to do a rotation around the $x$-axis, plus the ability to do a Hadamard, and turn that into the ability to do a rotation around the $z$-axis. We can also bring the Clifford conjugation up into the exponent (writing the Hadamard's Hermitian conjugate explicitly, even though $H = H^\dagger$ here for clarity):

$$R_z(\theta) = H\,e^{iX\theta/2}\,H^\dagger = e^{i(HXH^\dagger)\theta/2}$$

That's fine to do because all it's doing is a basis transformation — changing the eigenbasis — and we're using the fact that the unitary has the same eigenbasis as the Hermitian we're describing it in terms of. So we can apply the conjugation to the Hermitian just as well as to the unitary. That's a trick we'll use again shortly.

---

## Spreading a rotation across a multi-qubit register

With Cliffords, we can turn a rotation around $X$, $Y$, or $Z$ on a single qubit into one of the others. But using multi-qubit Cliffords, this gets even more interesting.

Say we have $e^{i\theta/2\, X}$ applied to a single qubit. To apply it across many qubits, we tensor it up — say, over four qubits, with our chosen qubit in one slot and identities elsewhere:

$$e^{i\theta/2\; X\otimes\mathbb{1}\otimes\mathbb{1}\otimes\mathbb{1}}$$

(Same trick as before — moving everything up into the exponent, since the unitary and the Hermitian share an eigenbasis.)

What happens if we conjugate this with a controlled-NOT — labeling the qubits $0,1,2,3$, controlled on qubit $3$ and targeted on qubit $2$?

$$C_x^{3,2}\; e^{i\theta/2\; X\otimes\mathbb{1}\otimes\mathbb{1}\otimes\mathbb{1}}\; C_x^{3,2}$$

We can write this out again, this time moving the CNOTs up into the exponent:

$$e^{i\theta/2\; C_x^{3,2}\big(X\otimes\mathbb{1}\otimes\mathbb{1}\otimes\mathbb{1}\big)C_x^{3,2}}$$

And CNOTs have exactly the effect we discussed earlier — conjugating $X\otimes I$ by a CNOT gives $X\otimes X$. So this becomes:

$$e^{i\theta/2\; X\otimes X\otimes\mathbb{1}\otimes\mathbb{1}}$$

This is *not* the same as doing this rotation independently on both qubits — in that case you'd get lots of different terms. Instead, this is an **entangling operation** — it entangles the first two qubits involved.

We can similarly conjugate by even more CNOTs and get:

$$e^{i\theta/2\; X\otimes X\otimes X\otimes X}$$

by the magic of controlled-NOTs. Then we can apply some other Clifford operation and use it, by conjugation, to change one of those Paulis — say a Hadamard on qubit $2$, either side of the operation. That Hadamard conjugates that $X$, turning it into a $Z$:

$$H_2\; e^{i\theta/2\; X\otimes X\otimes X\otimes X}\; H_2^\dagger = e^{i\theta/2\; X\otimes Z\otimes X\otimes X}$$

---

## The punchline

So by just using the humble rotation around the $x$-axis, combined with all of the Clifford gates — notably the controlled-NOT, and the single-qubit Cliffords which can transform $X$ into $Z$, $Z$ into $X$, $X$ into $Y$, $Y$ into $X$ — we can write down any arbitrary unitary of the form:

$$e^{i\theta/2\; P_{n-1}\otimes P_{n-2}\otimes\cdots\otimes P_1\otimes P_0}$$

where each $P_j$ is drawn from the set of Paulis, including the honorary Pauli, the identity.

Any gate of this form — big, multi-qubit, messy gates — we can get from the gates we started with. And this is a pretty powerful gate set. We don't usually think about designing algorithms specifically in terms of gates of this form, but we can prove that using gates of this form, we can do *anything*.

So if we can do anything with gates of this form, and we can make gates of that form by combining simple, single-qubit non-Cliffords with Cliffords, then just with these gates we know so far — rotation around the $x$-axis, the Hadamard, $S$, and the controlled-NOT — we can do quite a lot.

But we'll leave it till next week to use this to prove that we can do anything: we'll define what it means for a quantum computer to do *anything* a quantum computer can do — the notion of **universality** — and show that using this gate set, we can achieve it. Then we'll link that to a specific application showing that quantum computers can also do things that are intractable for classical computers. Once we have that, we can start looking at specific applications.
