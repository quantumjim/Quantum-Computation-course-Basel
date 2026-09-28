# 3 — Representing Single Qubit States and Gates

*Dr James Wootton, IBM Quantum*

> **Transcription note:** transcript-based rewrite, using James's actual spoken narration (lightly cleaned up — filler words, mid-take corrections, and recording asides removed) matched against the whiteboard's equation order.

---

## From experimentalist to theorist

Hello, I'm Dr James Wootton of IBM Quantum, and this is the third lecture in this course on quantum computing. In the first two lectures we have been like experimentalists — at least, a toy model of experimentalists — where we've been getting our hands on qubits, poking them in various ways to see what happens, to get an understanding of what kind of states they have, how they're manipulated through gates, and how they can be used in computation.

Now it's time to start being a theorist, and write down a mathematical representation of the kind of states and operations we've seen, so that we can better understand it and build up toward things like algorithms.

---

## Reviewing the circuits we already know

Let's first review a couple of simple circuits we've seen so far, and the behaviour we've seen, so we can start thinking about how to represent them with mathematics.

The simplest thing we'll have seen so far is the circuit which does nothing — it just takes us from the default initial state to a measurement gate representing a $Z$ measurement, and the result we get is, with certainty, a zero.

If we have something a little more complicated — where we go into an $X$ gate — this takes the qubit that's destined to give us a zero for a $Z$ measurement, and acts essentially as a NOT gate, giving us with certainty a one.

We also see examples where we have some probability of getting a zero, and some probability of getting a one. For example, if we do a Hadamard gate: doing the Hadamard gives us exactly $50/50$ probability of getting a zero or a one — at least in theory; if you run that on a real device, noise will have an opinion as to whether you really get $50/50$.

---

## Naming the states: $|0\rangle$ and $|1\rangle$

We need some way to represent these mathematically — a way to write down the state that's certain to give us a zero if we do a $Z$ measurement. So what are we going to call it? Let's call it "zero." How are we going to remind ourselves that this is a *qubit state* zero, and not the number zero, or a bit-string zero? When we do vectors we might write a little arrow on top — so what's our equivalent, to remind us this is a quantum state? It's to write a line on one side and an angle bracket on the other:

$$|0\rangle$$

Similarly we define the state destined to give us a $1$ for a $Z$ measurement with certainty:

$$|1\rangle$$

What mathematical object are we going to use to represent these? These are the only two possibilities, because this is a quantum bit — it has to be defined as something with only two possible states, otherwise it's not a quantum version of a bit.

What we've found is that the best way is to represent these as vectors in a two-dimensional space, where each of these two states is one of two orthogonal vectors. The fact that these are two completely disjoint possibilities is represented by the fact that they're orthogonal. The fact that there are only two possibilities allowed for a qubit is represented by the fact that they sit in a two-dimensional vector space.

We can use any basis vectors we like, as long as they're orthogonal — but since at this point we're defining things, let's use the simplest ones. One vector points along one particular direction — the $|0\rangle$ direction — and the other points along another. These aren't directions in physical space (that comes later, with the Bloch sphere) — these are just abstract vectors.

More generally, we can write a qubit state as a general vector, written as an amplitude times the $|0\rangle$ state plus an amplitude times the $|1\rangle$ state — a linear superposition of the two:

$$|\psi\rangle = a_0|0\rangle + a_1|1\rangle$$

---

## The inner product

Let's talk about the notion of a scalar product, or dot product. With vectors it's often useful to have a product of two vectors that yields a scalar — in quantum computing we call this the **inner product**.

Say we've got a state $|\psi\rangle$ as defined above, with amplitudes $a_0$ and $a_1$ represented as a column vector. We're going to define a **dual** of this — a row vector, with the same amplitudes $a_0$ and $a_1$, except that they're also complex conjugates. That's a bit of a spoiler for later, when we realize we'll need complex numbers — but when we do, this dual has to use the complex conjugate. For real numbers this makes no difference, but for complex numbers it means we reverse the sign of the imaginary part.

We need some notation to flag that this is a quantum state, but not the same kind as the ket form — this different, dual form we call a **bra**. We flag it up by writing the notation in reverse:

$$\langle\psi|$$

Now, when we have a bra and a ket, we can multiply them together using standard matrix multiplication to get a scalar. Let's multiply the bra form of $|\psi\rangle$ with the ket form:

$$\langle\psi|\psi\rangle$$

This compact notation is really just shorthand for the matrix multiplication of a row vector by a column vector. And in fact, this is the origin of the entire notation — writing things in terms of these brackets came before writing the vectors themselves as "bras" and "kets." It's the word *bracket* that was split up to get *bra* and *ket*. So there you go — hopefully that makes a bit more sense now, and I can stop referring to it as "this weird notation."

---

## Computing $\langle\psi|\psi\rangle$

If we do this matrix multiplication — a row vector times a column vector — we're multiplying rows by columns to get the entries of the result. Because we're multiplying a single row by a single column, we get a single scalar as the result, and that scalar is equal to the square of the magnitude of $a_0$ plus the square of the magnitude of $a_1$:

$$\langle\psi|\psi\rangle = |a_0|^2 + |a_1|^2$$

Here I'm using the fact that for any complex number, the complex conjugate times the original number is the square of the magnitude.

Now let's do something that's not multiplying the bra of a state by the ket of the same state. Let's do the inner product of $|0\rangle$ with $|\psi\rangle$. This is multiplying the basis vector $(1, 0)$ by our vector $(a_0, a_1)$ — well, technically $(1,0)$ is the complex conjugate of the basis vector, but that's just $(1,0)$, so who cares. Doing this multiplication:

$$\langle0|\psi\rangle = 1\cdot a_0 + 0\cdot a_1 = a_0$$

I'm not going through each individual step of the matrix multiplication here since it's just matrix multiplication, and there are vast resources online if that doesn't make sense to you already.

So we find that the inner product of $|0\rangle$ and $|\psi\rangle$ gives us $a_0$ — exactly the amplitude in front of the $|0\rangle$ state in the superposition. You get "how much zero-ness" there is in the superposition by doing this inner product.

---

## Inner products of the basis states, and normalization

Let's do a couple of inner products on states we already know well. $\langle0|0\rangle$: doing the matrix multiplication of $(1,0)$ with $(1,0)$, that's $1\times1 + 0\times0 = 1$. Similarly $\langle1|1\rangle$: $0\times0 + 1\times1 = 1$. And the off-diagonals — $\langle0|1\rangle$ and $\langle1|0\rangle$ — both come out as $1\times0 + 0\times1 = 0$.

$$\langle0|0\rangle = 1, \qquad \langle1|1\rangle = 1, \qquad \langle0|1\rangle = \langle1|0\rangle = 0$$

So for a state with itself we get one, and between two orthogonal states we get zero — which is exactly what we should find. This gives us a **normalization condition** for our general state: if we take $|\psi\rangle$ and do the inner product of itself with itself, we get $a_0^* a_0 + a_1^* a_1$, and we want this to be one, for the state to be nicely normalized in the same way that $|0\rangle$ and $|1\rangle$ are:

$$|a_0|^2 + |a_1|^2 = 1$$

---

## Working out the $|+\rangle$ state

Now let's work out what state we get from doing a Hadamard. If we apply a Hadamard to $|0\rangle$, we know that doing a $Z$ measurement afterward, we're equally likely to get zero or one — but if we were to do an $X$ measurement, we'd definitely get zero. So what does this state look like?

The fact that it's equally likely to give a zero or a one means the state shouldn't be biased toward either. The most even-handed thing is just $|0\rangle + |1\rangle$, since this is no more zero than it is one. But to make sure it's nicely normalized, we add a constant $C$ — let's call this state $|+\rangle$:

$$|+\rangle = C\big(|0\rangle+|1\rangle\big)$$

Taking the inner product of $|+\rangle$ with itself: $\langle+|+\rangle = 2C^2$ (or more generally $2C^*C$ — let's just keep it real, sounds a bit nineties). We want this to equal one, so $2C^2=1$, which implies $C = 1/\sqrt2$:

$$|+\rangle = \frac{1}{\sqrt2}\big(|0\rangle+|1\rangle\big)$$

Why does that give equal probabilities of zero or one? Well, what else would it give? It's basically an argument from symmetry — no reason for it to be more biased toward zero or one, since it's an equal superposition of the two. But in general we can't rely on symmetry arguments to work out probabilities.

---

## The Born rule

Let's look at the clues we already have for what corresponds to probability. We've got an equation where the magnitude of a complex number squared, plus another magnitude squared, equals one — and separately, we have two things that should equal a probability of a half: the outcomes for zero and for one, both with amplitude $1/\sqrt2$.

If we look at what $a_0$ and $a_1$ are for the $|+\rangle$ state, we find that the squares of these amplitudes are equal to a half — they're actually equal to the probability. This could be a coincidence, but one thing that lends weight to it not being a coincidence is that in general, these two numbers have to add up to one, just like the probability of getting zero and the probability of getting one have to add up to one, because these are two disjoint possibilities that completely cover all possibilities.

So it makes sense to say: the probability of getting a zero should be the square of the amplitude for the $|0\rangle$ state, and the probability of getting a one should be the square of the amplitude of the $|1\rangle$ state. You can either be convinced by the arguments so far, or just accept the rule either way — this is called the **Born rule**.

---

## Working out the $|-\rangle$ state

With this in mind, we can think about what would happen if we did $X$ then Hadamard. From Hello Qiskit or other experimentation, you can find that if you do a $Z$ measurement at the end, you get zero or one with equal probability — so the corresponding state should be some kind of equal superposition of $|0\rangle$ and $|1\rangle$, just like $|+\rangle$. However, if you were to do an $X$ measurement, you'd be certain to get a **one** — the complete opposite of what you get from $|+\rangle$, where you're certain to get a zero.

So we need a state that's, like $|+\rangle$, an equal superposition of $|0\rangle$ and $|1\rangle$, but orthogonal to $|+\rangle$. The way to do this is simply to put a minus in the middle instead of a plus:

$$|-\rangle = \frac{1}{\sqrt2}\big(|0\rangle - |1\rangle\big)$$

Here the amplitude $a_0 = 1/\sqrt2$, giving probability $P_0 = 1/2$. And for $a_1 = -1/\sqrt2$, this squares again to a half for probabilities — because we're squaring, the minus disappears, and we get the properties we need. You can verify for yourself that the inner product of this state with $|+\rangle$ is zero — they're orthogonal.

So here we have a state we call $|-\rangle$, orthogonal to $|+\rangle$, just like $|0\rangle$ and $|1\rangle$ are orthogonal to each other. But if you measure either $|+\rangle$ or $|-\rangle$ in the $Z$ basis, you get random outcomes — and if you measure $|0\rangle$ or $|1\rangle$ in the $X$ basis, you'd also get random results. There's actually no way that $|0\rangle$ and $|1\rangle$ are more special than $|+\rangle$ and $|-\rangle$ — we could have started with $|+\rangle$ or $|-\rangle$ and taken the $X$-basis measurement as our favorite instead. There's no mathematical reason one is more important than the other; we just have a bias toward $|0\rangle$, $|1\rangle$, and the $Z$ basis when thinking about quantum computing. They're not in any way more fundamental states — they're just as valid as any other superposition. Everything is a superposition of everything else.

---

## The $Y$ basis, and why we need complex numbers

Because we're using complex numbers, we can define another pair of orthogonal states, mutually unbiased from the other two bases — the ones with $i$ in them:

$$\frac{1}{\sqrt2}\big(|0\rangle + i|1\rangle\big)$$

Again normalized, with $1/\sqrt2$ — because of the possibility of having complex numbers, this is perfectly valid. If we take $a_1 = i/\sqrt2$, its complex conjugate $a_1^* = -i/\sqrt2$, and multiplying those together to get the probability of one, we find it's a half.

This is the state that gives a definite result when measured in the $Y$ basis, and you can also define one orthogonal to it. This is just to make sure you know complex numbers are indeed required here — required to incorporate the $Y$ basis, which we already know exists because we covered it very lightly in the Hello Qiskit workbook. So, we'll be needing complex numbers in general as we go forward.

---

## Global phase

Now let's think about the general form of a quantum state. But before we can nail that down, we need to think about **global phase**.

Consider the state $|0\rangle$ and the state $-|0\rangle$. How do these differ? $|0\rangle$ has amplitude $a_0=1$, so probability of getting zero is one. $-|0\rangle$ has amplitude $a_0=-1$, so the probability of getting zero is *also* one. If you measured in the $Z$ basis, you'd find no difference between the two states.

What about the $X$ basis — are they distinguishable there? In the $X$ basis, we can write the $|0\rangle$ state as the superposition of $|+\rangle$ and $|-\rangle$ (I'll leave you to verify this yourself) — with amplitude $a_+ = 1/\sqrt2$ for $|+\rangle$ and $a_- = 1/\sqrt2$ for $|-\rangle$. The probability of getting the $|+\rangle$ outcome, $P_+$, is the square of $a_+$, which is a half for the $|0\rangle$ state.

What happens for $-|0\rangle$? All those probabilities are the same, because the amplitudes are just multiplied by minus one — but that disappears when we take the square. So it turns out that in the $X$ basis too, these two states are completely indistinguishable. In fact, in *any* measurement we could ever possibly make, these two states are completely indistinguishable. There's no way to tell whether you have a $|0\rangle$ state or a $-|0\rangle$ state — or, more generally, whether you multiplied by any complex phase of magnitude one at all. It gives a perfectly normalized state that's completely indistinguishable, because when we take the magnitude, this phase disappears and doesn't show up in any probability.

These probabilities for measurement results are the only thing that's actually physical when we're doing anything with qubits — and if there's no way in theory that any measurement could distinguish between two things, are they not the same? So it's true in this case too: when you multiply any state by a **global phase** — this could be a factor of minus one, or any factor of $e^{i\theta}$ for any real $\theta$ — the state is physically indistinguishable. So even though mathematically it might look different, physically it's indistinguishable. Therefore, when writing down the most general form of a quantum state, we don't need to include the ability for a general global phase, because global phases are irrelevant.

---

## Building the general single-qubit state

So let's write down our general state. We have $|\psi\rangle = a_0|0\rangle + a_1|1\rangle$, where $a_0$ has a real part and an imaginary part, which can be written as two real numbers, the imaginary part multiplied by $i$. We can think of either amplitude in terms of a real and imaginary part — but there's also a way to write complex numbers in **polar form**, again in terms of two real numbers, but differently: a phase and a magnitude.

If the phase is zero, $e^{i\cdot0}=1$, so it's just a positive number; if the phase is $\pi$, we get $-1$, a negative number; anything else gives a more general complex number. Writing this out:

$$|\psi\rangle = e^{i\alpha_0}a_0|0\rangle + e^{i\alpha_1}a_1|1\rangle$$

(here I'm using "nought" instead of "zero" when speaking, just because I'm inconsistent about what I call a particular number — I've tried for years to be more consistent and have yet to succeed, so please bear with me.)

As a little trick, we can take $e^{i\alpha_0}$ as a **global phase** and remove it, since we don't care about it any more — it's physically equivalent without it. So this is what we'll call our state $|\psi\rangle$. And now, since it's only the *difference* between $\alpha_0$ and $\alpha_1$ — the relative phase — that's physically relevant, instead of having both, let's have a single parameter $\phi$. This gives us a simpler form, since we've removed one of the numbers and made it have a consistent global phase.

One other thing to note: since $|a_0|^2 + |a_1|^2 = 1$, these amplitudes aren't really two independent parameters — they have a constraint over them, and we can replace them with a single parameter using a relationship like $\cos^2\theta + \sin^2\theta = 1$, whatever the value of $\theta$. So we can replace the magnitudes $|a_0|$ and $|a_1|$ with $\cos\theta$ and $\sin\theta$ for some $\theta$. There's another aspect here — for particular values of $\theta$, you can get one of them negative and the other positive, and that's a phase difference; so, although the phase is doing the work of that, we can get any balance we want using cos and sin with a single parameter $\theta$.

I've drawn the $\theta$ slightly floating here because it's actually better for us to use $\theta/2$ rather than just $\theta$ — we'll see why in a moment. So our general form of a single-qubit superposition state is parametrized by two numbers, $\theta$ and $\phi$.

---

## The Bloch sphere

I have another example of something parametrized by two real numbers, which we might like to call $\theta$ and $\phi$: a point on the surface of a sphere, using polar coordinates — an angle down from the $z$-axis, and an angle around from the $x$-axis. The reason we use $\theta/2$ in our state is so that we get a one-to-one correspondence between states and points on the surface of this sphere.

Let's look at some particular states. The $|0\rangle$ state has $\theta=0$, and $\phi$ doesn't matter, since $\phi$ is only relevant to the $|1\rangle$ amplitude, and $|1\rangle$ has no amplitude anyway — this is the state at the top of the sphere (with the polar bears). The $|1\rangle$ state has $\theta=\pi$, so $\cos(\pi/2)$ and $\sin(\pi/2)$ — and since $|1\rangle$ is the only state present, $e^{i\phi}$ becomes a global phase and we don't care about it either — this is the state among the penguins, at the bottom.

The other states we've looked at, $|+\rangle$ and $|-\rangle$, are on the equator: $\theta=\pi/2$. For $\phi=0$ you're pointing along the $x$-axis — that's your $|+\rangle$ state — and for $\phi=\pi$, $e^{i\pi}=-1$, giving you a minus in the superposition instead of a plus, so that's your $|-\rangle$ state. The $Y$-basis states point along the $y$-axis. This is why we call these things $X$, $Y$, and $Z$ measurements — because the two states with a definite result for $Z$ measurement are associated with the $z$-axis of the sphere, and similarly for $X$ and $Y$. That gives us a nice visual understanding, and it's also nice that orthogonal states here are antipodes on this sphere.

This is a two-dimensional — well, I say "real," meaning "true," not "real" in the sense of real numbers — description of what's going on in a qubit. It's the correspondence between a two-dimensional complex vector space and a three-dimensional real vector space, which lets us imagine this weird two-dimensional complex vector space as a nice, sensible three-dimensional real thing that we, as beings living in a three-dimensional real-valued world, can understand better. It's not the same vector space — that's why orthogonal states in the two-dimensional complex vector space correspond to antipodes in this three-dimensional version. But nevertheless it's a nice correspondence between different forms of things. In fact, we can define a measurement between any pair of antipodes on this sphere — any state anywhere, plus its antipode — and that measurement distinguishes between the two, giving outcome zero for one, and outcome one for the other.

---

## Gates as rotations of the Bloch sphere

This visualization is also good for thinking about what operations we can perform on single-qubit states. When we apply a gate, we're moving from one state to another — both points on the surface of the sphere (surface, because of our normalization condition — though we'll see examples later, with multiple qubits, where they don't live on the surface).

The gates we have move things around like a **rotation**. We can have a rotation around the $x$-axis by some angle — for example, a rotation around the $x$-axis by an angle of $\pi$ is a 180-degree rotation, which would take a $|0\rangle$ state and turn it into a $|1\rangle$ state, and take $|1\rangle$ and rotate it round to $|0\rangle$. That's something we've seen before — that's the **$X$ gate**. This is why the $X$ gate is called the $X$ gate: it's a $\pi$ rotation around the $X$-axis. But we can have any angle of rotation, not just $\pi$.

We can also rotate around the $Z$-axis — this is what's explicitly referenced in the textbook chapter this lecture is based on. This would take something like the $|+\rangle$ state and turn it into $|-\rangle$, and vice versa — that's the $Z$ we've seen before. There are also special names for other rotations around the $Z$-axis: $\pi/2$ we call $S$, $-\pi/2$ we call $S^\dagger$ (reasons we'll see in later lectures), $\pi/4$ we call $T$, and there's also $T^\dagger$ for $-\pi/4$.

---

## Gates as matrices

Because these are operations applied to vectors, we can also think of them as matrices.

**Identity.** The identity gate is the one we've discussed already — the trivial gate that does nothing. Its matrix representation is the identity matrix:

$$I = \begin{pmatrix}1&0\\0&1\end{pmatrix}$$

Applying it to a general vector $|\psi\rangle$ with amplitudes $a_0,a_1$ — taking the $1$ from the first row times $a_0$ from the column, plus the $0$ times $a_1$, gives $a_0$ back; likewise the second row gives $a_1$ back. So it does nothing — that's the identity matrix.

**$X$.** The $X$ gate's matrix looks like this:

$$X = \begin{pmatrix}0&1\\1&0\end{pmatrix}$$

Also multiplying things by ones and zeros — an easy answer, just with the ones and zeros the other way round, so you get the result the other way round: explicitly $(a_1, a_0)$. It has the effect of flipping a bit: $X|0\rangle = |1\rangle$, $X|1\rangle=|0\rangle$.

What happens when we apply $X$ to $|+\rangle$? It's still got the $1/\sqrt2$ out front, and $|+\rangle = |0\rangle+|1\rangle$, so the $|0\rangle$ turns into $|1\rangle$ and the $|1\rangle$ turns into $|0\rangle$ — but $|0\rangle+|1\rangle$ is the same as $|1\rangle+|0\rangle$, so you get the same state out as you started with:

$$X|+\rangle = |+\rangle$$

That's what we'd expect from Hello Qiskit. However, if you apply $X$ to $|-\rangle$, you get $|1\rangle - |0\rangle$, which isn't quite the same as $|-\rangle$ — but if you take a global phase of minus one, you get back to $|-\rangle$:

$$X|-\rangle = -|-\rangle$$

Since this is just a global phase, it also effectively does nothing. So we can say $X$ does nothing to the $|-\rangle$ state on its own — but it does have an effect we need to account for when superpositions happen: it causes a phase difference between $|+\rangle$ and $|-\rangle$ within superpositions.

**$Z$.** To see this, let's look at another gate:

$$Z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

Rather like the identity, except with this phase difference between $|0\rangle$ and $|1\rangle$: $Z|0\rangle = |0\rangle$, $Z|1\rangle = -|1\rangle$. So $Z$'s action on $|0\rangle,|1\rangle$ is the same as $X$'s action on $|+\rangle,|-\rangle$. When we apply $Z$ to a general superposition, it keeps the $|0\rangle$ part as $|0\rangle$, but multiplies the $|1\rangle$ part by minus one — and because this phase difference isn't global, you can't pull the minus out and ignore it; it's actually relevant.

Let's see this on $|+\rangle$ and $|-\rangle$. $|+\rangle$ is the superposition of $|0\rangle$ and $|1\rangle$ with amplitude $1/\sqrt2$ each — but because of $Z$'s effect, instead of adding $|0\rangle$ and $|1\rangle$, we get a minus in there, giving us $|-\rangle$:

$$Z|+\rangle = |-\rangle, \qquad Z|-\rangle = |+\rangle$$

So $Z$ flips $|+\rangle$ to $|-\rangle$ and vice versa — the same effect on the $X$-basis states that $X$ has on the $Z$-basis states.

**Hadamard.** Another important gate — this cannot be expressed purely as a rotation around the $X$, $Y$, or $Z$ axis of the Bloch sphere; it can be built out of a few of these combined, but another way to think of it is as a rotation around the axis that lies equally between the $X$ and $Z$ axes, by $\pi$. That's why it takes you from $|0\rangle$ round to $|+\rangle$ and vice versa, and also why it transforms between $|1\rangle$ and $|-\rangle$.

$$H = \frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac{1}{\sqrt2}(X+Z)$$

If you do the matrix multiplication (I'll leave this as an exercise), $H|0\rangle$ gives $|+\rangle$, and $H|1\rangle$ gives $|-\rangle$ — transforming the $Z$-basis states into the $X$-basis states.

---

## Gates as outer products

Another important thing to note: these gates can also be written in terms of **outer products**. Let's take a ket and multiply it by a bra using matrix multiplication — a bra times a ket gives a scalar; a ket times a bra gives a matrix.

$$|0\rangle\langle0| = \begin{pmatrix}1\\0\end{pmatrix}\begin{pmatrix}1&0\end{pmatrix} = \begin{pmatrix}1&0\\0&0\end{pmatrix}$$

Similarly $|1\rangle\langle1| = \begin{pmatrix}0&0\\0&1\end{pmatrix}$, and adding these together gives us back the identity matrix:

$$I = |0\rangle\langle0| + |1\rangle\langle1|$$

Now let's try this for $X$. Taking the off-diagonal terms $|0\rangle\langle1|$ and $|1\rangle\langle0|$: $|0\rangle\langle1|$ gives a $1$ only in the first row, second column; $|1\rangle\langle0|$ gives a $1$ only in the second row, first column. Adding these:

$$X = |0\rangle\langle1| + |1\rangle\langle0|$$

You might notice this isn't a coincidence with what $X$ actually does — it turns $|0\rangle$ into $|1\rangle$ and vice versa, and here we've got exactly that pairing. If you apply this to $|0\rangle$, you can reinterpret each term as an inner product: $|0\rangle\langle1|$ times $|0\rangle$ becomes $|0\rangle$ multiplied by the inner product $\langle1|0\rangle = 0$, giving zero; and $|1\rangle\langle0|$ times $|0\rangle$ becomes $|1\rangle$ multiplied by $\langle0|0\rangle=1$, giving $|1\rangle$. So one term was "looking for a $|1\rangle$" and does nothing when it doesn't find one, and the other was "looking for a $|0\rangle$," and once it slots in, outputs $|1\rangle$.

We could equally have written $X$ in terms of its own eigenbasis — the gate that turns $|+\rangle$ into $|+\rangle$, and $|-\rangle$ into $-|-\rangle$:

$$X = |+\rangle\langle+| - |-\rangle\langle-|$$

And similarly, $Z$ can be written $Z=|0\rangle\langle0|-|1\rangle\langle1|$, or, in terms of $|+\rangle$ and $|-\rangle$, as the gate that switches $|+\rangle$ to $|-\rangle$ and $|-\rangle$ to $|+\rangle$. These are some tricks we'll look into more in later lectures, but you can already start playing around with these outer products now.

---

## General $Z$-rotations, and the $S$ gate as $\sqrt Z$

Now let's look at more general $Z$-rotations in matrix form. Taking $R_Z(\phi)$, there are two ways to write this down — we'll use the form with $e^{i\phi}$ in this lecture, though it could equivalently be written with $e^{-i\phi/2}$ and $e^{i\phi/2}$ (differing from the other form by a global phase; sometimes one form makes more sense than the other):

$$R_Z(\phi) = \begin{pmatrix}1&0\\0&e^{i\phi}\end{pmatrix}$$

If you put $\pi$ in here, you get $e^{i\pi}=-1$, recovering the known result:

$$R_Z(\pi) = Z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

And $R_Z(\pi/2)$ — what we're calling the $S$ gate, also called the **square root of $Z$**:

$$R_Z(\pi/2) = S = \sqrt Z = \begin{pmatrix}1&0\\0&i\end{pmatrix}$$

We call it the square root of $Z$ because if you do two of these — $S$ followed by another $S$ — that's the same as a $Z$:

$$SS = S^2 = Z$$

That relation will be useful later. And one more useful relation: $HZH = X$ — conjugating $Z$ by a Hadamard gives you $X$.

$$HZH = X$$

---

## Closing

So there you have some gates as matrices. Quantum computing is basically all about playing around with these matrices, playing around with the behaviour we get as we combine them — looking at things like what happens if you do a Hadamard, then a $Z$, then a Hadamard, and finding that this gives you the same as an $X$. Most of the time we'll be doing more complex things than that, but playing around with these sorts of relations is pretty much all that quantum computing is about — you just have to get to bigger and fancier implementations of it. That's what we'll be doing in the future lectures. But that's all for today. Thank you for listening, and I'll see you next time.
