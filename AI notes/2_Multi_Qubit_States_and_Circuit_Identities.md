# 4 — Multi Qubit States and Circuit Identities

*Dr James Wootton, Moth Quantum*

> **Transcription note:** transcript-based rewrite, using James's actual spoken narration (lightly cleaned up — filler words, mid-take corrections, and recording asides removed) matched against the whiteboard's equation order.

---

## Introducing the tensor product

Hello and welcome to another lecture in this course on quantum computing, based on the Qiskit textbook. In this lecture we're going to be moving from one-qubit states and gates, as we saw in the last lecture, to two-qubit states and gates. In doing so, we introduce a tool that lets us generalize to any number of qubits: the **tensor product**.

The tensor product is used quite widely in linear algebra, so you may already know it — if not, let's look at a few examples. Take two $2\times2$ matrices, $A$ and $B$:

$$A = \begin{pmatrix}a_{00}&a_{01}\\a_{10}&a_{11}\end{pmatrix}, \qquad B = \begin{pmatrix}b_{00}&b_{01}\\b_{10}&b_{11}\end{pmatrix}$$

The tensor product $A\otimes B$ gives us a $4\times4$ matrix. I kind of think of it as inserting the matrix on the right into the matrix on the left — we make a bigger, padded-out version of $A$, where the top-left element $a_{00}$ gets copied four times, and each copy multiplied by a different element of $B$: $a_{00}b_{00}$, $a_{00}b_{01}$, $a_{00}b_{10}$, $a_{00}b_{11}$. So here we've multiplied this element of $A$ by the whole $B$ matrix. We continue the same principle for $a_{01}$, $a_{10}$, $a_{11}$ (I won't fill in every entry — same principle, and I don't want to be saying "$a$, $b$, zero and one in various combinations" for the next 15 minutes):

$$A\otimes B = \begin{pmatrix}a_{00}b_{00}&a_{00}b_{01}&a_{01}b_{00}&a_{01}b_{01}\\a_{00}b_{10}&a_{00}b_{11}&a_{01}b_{10}&a_{01}b_{11}\\a_{10}b_{00}&a_{10}b_{01}&a_{11}b_{00}&a_{11}b_{01}\\a_{10}b_{10}&a_{10}b_{11}&a_{11}b_{10}&a_{11}b_{11}\end{pmatrix}$$

That's how you do a tensor product of two $2\times2$ matrices, and hopefully that also gives you a flavor of how it works more generally.

Now let's do it for vectors. Take vector $|a\rangle$ with amplitudes $a_0,a_1$, represented as the column vector $(a_0,a_1)$, and vector $|b\rangle = (b_0,b_1)$. The tensor product of these vectors works the same way — take the first element of $|a\rangle$, multiply it by the whole of $|b\rangle$; take the second element of $|a\rangle$, multiply it by the whole of $|b\rangle$ again:

$$|a\rangle\otimes|b\rangle = \begin{pmatrix}a_0\begin{pmatrix}b_0\\b_1\end{pmatrix}\\a_1\begin{pmatrix}b_0\\b_1\end{pmatrix}\end{pmatrix} = \begin{pmatrix}a_0b_0\\a_0b_1\\a_1b_0\\a_1b_1\end{pmatrix}$$

This is going to be pretty important for what we're going to say today.

---

## Recap: the single-qubit case

Let's briefly review what happened in the single-qubit case. We found we can take a single measurement — the $Z$ measurement is our favorite — and there are two possible outcomes, $0$ and $1$. We define a state $|0\rangle$ that's definitely going to give us the outcome zero, and a state $|1\rangle$ that's definitely going to give us the outcome one. Any other state can be expressed as a linear superposition of these two, expressed as vectors:

$$c_0|0\rangle + c_1|1\rangle = |\psi\rangle$$

---

## The two-qubit case

What about the two-qubit case? If we measure both of our qubits in the $Z$ basis, we have four possible outcomes: $00, 01, 10, 11$. Similarly, we can define four vectors that correspond to those four cases — $|00\rangle$, representing the state where we definitely get outcome zero for both qubits; $|01\rangle$, meaning definitely zero for one qubit and definitely one for the other; and so on for $|10\rangle$ and $|11\rangle$.

$$|00\rangle, \qquad |01\rangle, \qquad |10\rangle, \qquad |11\rangle$$

With these four basis states we can write any state as a superposition of them, with complex amplitudes in general, and the amplitudes have to satisfy a normalization condition — and global phase is again irrelevant. The probability of getting outcome $00$ again satisfies the Born rule: it's the square of the amplitude of $|00\rangle$. If we take a sum over all $j,k$ (each either zero or one) of $|c_{jk}|^2$, this has to equal one, since these individually are probabilities:

$$c_{00}|00\rangle + c_{01}|01\rangle + c_{10}|10\rangle + c_{11}|11\rangle, \qquad \sum_{j,k\in\{0,1\}}|c_{jk}|^2 = 1$$

That's how you represent a two-qubit state. Put a three-bit string in the kets and this represents a three-qubit state; five, five qubits; a 72-bit string inside the kets, and it represents the state of 72 qubits. This is basically how you do it. But you might be wondering: what does $|00\rangle$ actually look like as a vector?

---

## Basis vectors as tensor products

We can represent these vectors as tensor products of vectors we already know:

$$|00\rangle = |0\rangle\otimes|0\rangle = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}$$

For $|01\rangle$: the tensor product of $|0\rangle=(1,0)$ with $|1\rangle=(0,1)$. The first two elements of this four-dimensional vector are a copy of $(0,1)$, and the next two elements are all multiplied by the zero in $|0\rangle$'s second entry, so they're zero too:

$$|01\rangle = \begin{pmatrix}1\\0\end{pmatrix}\otimes\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\1\\0\\0\end{pmatrix}$$

Each of these corresponds to a different possible bit string — that one's $00$, that one's $01$, the next is $10$, and the last is $11$.

Also, if we have two single-qubit state vectors $|a\rangle$ (amplitudes $a_0,a_1$) and $|b\rangle$ (amplitudes $b_0,b_1$), their tensor product describes a two-qubit state in which one qubit is in state $|a\rangle$ and the other is in state $|b\rangle$:

$$|a\rangle=a_0|0\rangle+a_1|1\rangle, \qquad |b\rangle=b_0|0\rangle+b_1|1\rangle, \qquad |a\rangle\otimes|b\rangle$$

So you can still do all your familiar single-qubit stuff on two-qubit states, but you have to use a tensor product to make it more general.

---

## Applying single-qubit gates within a multi-qubit register

If we were just talking about single-qubit states and wanted to apply an $X$ to the qubit in state $|a\rangle$, we'd just apply the $X$ matrix to that vector. But for two-qubit states, you can't just apply that $2\times2$ matrix to the four-dimensional vector describing both qubits — you need a $4\times4$ matrix that does an $X$ to the qubit you want, and nothing to the other. We already know how to do nothing — the identity matrix — and with these we do a tensor product again: $X\otimes I$.

$$X = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad I = \begin{pmatrix}1&0\\0&1\end{pmatrix}$$

$$X\otimes I = \begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}$$

This matrix applies an $X$ only to the qubit we want, and does nothing to the other — the top-left and bottom-right blocks are zero, and the off-diagonal blocks are identities. (This is what you signed up for, isn't it — listening to a guy talk in binary.) This matrix acts non-trivially on only a single qubit, but is phrased as a two-qubit matrix, so you can apply it to two-qubit states.

Similarly, if you had three qubits and wanted to do an $X$ on just the middle one, that's $I\otimes X\otimes I$. (One other note: people often write the identity matrix with a blackboard-bold $\mathbb{1}$ — if I ever use that by accident instead of $I$, now you know what it means, since it's easy to slip between the two very common conventions.)

---

## The controlled-NOT matrix

Now we've phrased some of the single-qubit stuff from last time in this two-qubit context using the tensor product, we can look at some *truly* two-qubit operations — operations that cannot be expressed as the tensor product of two single-qubit gates. That's the **controlled-NOT**.

The controlled-NOT has non-zero entries only in two blocks on the diagonal — one block looks like the identity, the other looks like an $X$; everything else is zero:

$$C_x = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$$

(Often people can't be bothered to draw all the zeros in matrices like this — but it's good to do it the first time.) The identity block acts on the subspace spanned by $|00\rangle$ and $|01\rangle$ — the states where this qubit is $|0\rangle$; the $X$ block acts on the subspace spanned by $|10\rangle$ and $|11\rangle$ — where it's $|1\rangle$. So this matrix is telling us: when we have a $|0\rangle$, do nothing (identity); when we have a $|1\rangle$, do the same as an $X$, swapping the amplitudes for those two states.

This is how you read off, from this matrix, a controlled-NOT where the control is the qubit on the *right* of these bit strings, and the target is the qubit on the *left*. If you want the matrix the other way round, it looks different — you can find it in the textbook, or calculate it yourself.

---

## Applying CNOT: an entangled state appears

Let's apply the controlled-NOT to a particular state, to see an interesting two-qubit state that can't be represented as a tensor product of two single-qubit states. We'll start with a state that *can* be — a $|+\rangle$ on one qubit and $|0\rangle$ on the other:

$$|{+}\rangle\otimes|0\rangle = \frac{1}{\sqrt2}\big(|0\rangle+|1\rangle\big)\otimes|0\rangle = \frac{1}{\sqrt2}\big(|00\rangle+|10\rangle\big)$$

I'm sure you have years of experience with how addition and multiplication play together — it's exactly the same for addition of vectors and tensor products of vectors.

When we apply the controlled-NOT to this state, we get the same interpretation as before: if the control qubit is $|0\rangle$, nothing happens; if it's $|1\rangle$, the target qubit gets flipped. So for the first term the control is $|0\rangle$, nothing happens; for the second term the control is $|1\rangle$, so the target's zero flips to a one:

$$C_x\;|{+}\rangle\otimes|0\rangle = \frac{1}{\sqrt2}\big(|00\rangle+|11\rangle\big)$$

There is no tensor product of two single-qubit states that yields this result — this is a **truly two-qubit state**. Whenever we have a truly multi-qubit state that cannot be represented as a tensor product of single-qubit states, that's called an **entangled state**. Having an entangled state means we can't describe things as just lots of separate single-qubit things — it's become truly multi-party.

This is why entangled states are key to quantum computing: if you could describe everything as lots of single-qubit states, you could *simulate* everything as lots of single-qubit states, which is very easy to simulate — and you'd never find anything a normal computer couldn't do. You need truly multi-qubit effects to find the advantage of quantum computing over conventional computing. That's why you need entanglement.

---

## CNOT on $|{+}{-}\rangle$, and phase kickback

Now let's look at applying the controlled-NOT to the tensor product of a $|+\rangle$ and a $|-\rangle$. This gives $\tfrac12$ (the two factors of $1/\sqrt2$ multiplied together), and a superposition of all the basis states, but with a few minus-one phases in there from the $|-\rangle$ state — a phase of minus one comes in whenever there's a one on that particular bit value, because of the phase coming from that side:

$$|{+}\rangle\otimes|{-}\rangle = \frac{1}{2}\big(|00\rangle-|01\rangle+|10\rangle-|11\rangle\big)$$

Now let's look at cases where the controlled-NOT is controlled on the qubit written on the *left* and targeted on the qubit on the *right* — the opposite convention from the one in the textbook. The reason for taking the opposite convention is that controlled-NOTs do go both ways round, so it's important to see them both ways round — it's not that I'm choosing an "opposite" convention where only one should exist; both conventions exist simultaneously, they just differ by how you choose the control and target. (Also, I prefer it this way round!)

Let's apply this controlled-NOT to $|{+}{-}\rangle$. Going through each basis state: for the first two ($|00\rangle,|01\rangle$) the control is $|0\rangle$, so nothing happens; for the other two ($|10\rangle,|11\rangle$) the control is $|1\rangle$, so the target flips — $|0\rangle\to|1\rangle$ and $|1\rangle\to|0\rangle$:

$$C_x\;|{+}{-}\rangle = \frac{1}{2}\big(|00\rangle-|01\rangle+|11\rangle-|10\rangle\big) = |{-}\rangle\otimes|{-}\rangle$$

That's exactly what you'd get from the tensor product of $|-\rangle$ with $|-\rangle$ — I'll leave you to verify that yourself, but it's a quite interesting relation: take $|+\rangle$ on one qubit and $|-\rangle$ on the other, apply a CX, and you end up with $|-\rangle$ on *both* qubits. The qubit we're thinking of as the target is unchanged in this process; the qubit we're thinking of as the control *does* get changed. There's something interesting happening here.

To see what, note that $|{-}\rangle\otimes|{-}\rangle$ can be expressed as a superposition of $|0\rangle$ on the control qubit tensored with $|{-}\rangle$, and $|1\rangle$ on the control qubit tensored with $|{-}\rangle$:

$$|{+}\rangle\otimes|{-}\rangle = \frac{1}{\sqrt2}\Big(|0\rangle\otimes|{-}\rangle + |1\rangle\otimes|{-}\rangle\Big)$$

Look at these two terms individually. $C_x\;|0\rangle\otimes|{-}\rangle$: following the same steps as before, this can be expressed as $|0\rangle\otimes|{-}\rangle$ — no surprise, since the control qubit is $|0\rangle$, so nothing should happen. But apply it to the other term, $|1\rangle\otimes|{-}\rangle$: the control is $|1\rangle$, so we apply an $X$ to the $|-\rangle$ state. And when you apply an $X$ to $|-\rangle$, it doesn't affect that state, but does give a global phase of minus one:

$$C_x\;|0\rangle\otimes|{-}\rangle = |0\rangle\otimes|{-}\rangle, \qquad C_x\;|1\rangle\otimes|{-}\rangle = -|1\rangle\otimes|{-}\rangle$$

$$X|{-}\rangle = -|{-}\rangle$$

But when we applied it to the superposition, that global phase of minus isn't global anymore — it changes *this* term's phase from a plus to a minus, and that's how the overall $|+\rangle$ on the control side becomes a $|-\rangle$. The global phase became a **relative** phase, and therefore becomes relevant. This effect is known as **phase kickback**, and it's a quite useful effect that shows up in many algorithms.

---

## CNOT's truth table for $|\pm\rangle$ inputs

If we look at a few more states, we find the CX has the effect of turning $|{+}{+}\rangle$ into $|{+}{+}\rangle$ (no change — only plus-one phases, so nothing to kick back), $|{+}{-}\rangle$ into $|{-}{-}\rangle$ (as we just found), $|{-}{+}\rangle$ into $|{-}{+}\rangle$ (no effect either, since the target's phase is just plus, multiplying by $+1$), and $|{-}{-}\rangle$ into $|{+}{-}\rangle$ (a phase to kick back that flips the initial phase):

$$C_x: \quad |{+}{+}\rangle\to|{+}{+}\rangle,\quad |{+}{-}\rangle\to|{-}{-}\rangle,\quad |{-}{+}\rangle\to|{-}{+}\rangle,\quad |{-}{-}\rangle\to|{+}{-}\rangle$$

With this truth table you can come up with a completely different interpretation of what the controlled-NOT does: instead of looking at the control qubit, seeing if it's $|0\rangle$ or $|1\rangle$, and deciding whether to do an $X$ on the target — it also effectively looks at the *target* qubit, to see whether it's in state $|+\rangle$ or $|-\rangle$, and in the case where it's $|-\rangle$, applies a $Z$ to the *control* qubit, since $Z$ is the operation that flips $|+\rangle$s to $|-\rangle$s and vice versa:

$$Z|{+}\rangle = |{-}\rangle$$

Don't get too stuck on the idea of the controlled-NOT being "the thing that looks at the control and decides whether to do an $X$ on the target" — there are multiple valid interpretations of what a controlled-NOT does. It's a truly quantum gate, and therefore has lots of lovely mysteries for us to ponder.

---

## CNOT in Dirac notation

To complete our meditation upon the controlled-NOT, let's look at it in Dirac notation form. First let's remind ourselves what it looks like as a matrix — the version with the control on the left, target on the right — as a block-diagonal form, where the first block is identity and the second is $X$:

$$C_x = \begin{pmatrix}1&0&&\\0&1&&\\&&0&1\\&&1&0\end{pmatrix}$$

The first block pertains to any state where the control is $|0\rangle$, the second to any state where the control is $|1\rangle$. This means — and there's a bit of a leap between these two steps, so don't worry if you don't instantly see it, hopefully once we're there you'll see how it got there — we can write this down as a projector onto $|0\rangle$ (only affecting states where the control qubit is $|0\rangle$), tensor-producted with the identity, plus a projector onto $|1\rangle$, tensor-producted with an $X$:

$$C_x = |0\rangle\langle0|\otimes\mathbb{1} + |1\rangle\langle1|\otimes X$$

Now let's use the expansions of these gates into their Dirac-notation outer-product form. The identity can be expressed as $|0\rangle\langle0|+|1\rangle\langle1|$, but equally as $|+\rangle\langle+|+|-\rangle\langle-|$. And $X$ can be represented as the gate that turns $|0\rangle$ into $|1\rangle$ and vice versa — but also as the gate that turns $|+\rangle$ into itself and gives $|-\rangle$ a phase of minus:

$$\mathbb{1} = |0\rangle\langle0|+|1\rangle\langle1| = |{+}\rangle\langle{+}|+|{-}\rangle\langle{-}|$$

$$X = |0\rangle\langle1|+|1\rangle\langle0| = |{+}\rangle\langle{+}|-|{-}\rangle\langle{-}|$$

Substituting these identity expansions into our $C_x$ expression — first for the identity term, using $\mathbb{1}=|{+}\rangle\langle{+}|+|{-}\rangle\langle{-}|$, and then for the $X$ term, using $X=|{+}\rangle\langle{+}|-|{-}\rangle\langle{-}|$:

$$C_x = |0\rangle\langle0|\otimes|{+}\rangle\langle{+}| + |0\rangle\langle0|\otimes|{-}\rangle\langle{-}| + |1\rangle\langle1|\otimes|{+}\rangle\langle{+}| - |1\rangle\langle1|\otimes|{-}\rangle\langle{-}|$$

Now we collect terms. Collecting the two terms sharing $|{+}\rangle\langle{+}|$ on the target qubit: on the control side we get $|0\rangle\langle0|+|1\rangle\langle1|$, which is just the identity. Collecting the two terms sharing $|{-}\rangle\langle{-}|$: on the control side we get $|0\rangle\langle0|-|1\rangle\langle1|$, which is $Z$:

$$C_x = \mathbb{1}\otimes|{+}\rangle\langle{+}| + Z\otimes|{-}\rangle\langle{-}|$$

This completes the picture: we can see the CX in the normal way — the first matrix form we wrote down — or in a way where it looks to see whether the *target* qubit is $|+\rangle$ (and if so, does nothing) or $|-\rangle$ (and if so, does a $Z$ to the control).

So there I've told you a lot about controlled-NOTs — we've really sort of meditated on them for a while, because they're really very key, and there's a lot of cool stuff to just thinking about controlled-NOTs. Forget Grover's algorithm, Shor's algorithm, all that nonsense — controlled-NOTs are more than enough coolness to keep you going for some time. But we're going to have to move on, unfortunately, to a few circuit identities: simple ways of combining gates to get useful effects that come up a lot in quantum computing.

---

## The Hermitian conjugate, and Hadamard conjugation of Paulis

We've already seen that if you have a ket, there's an equivalent representation of that state as a bra. Similarly, if you have a gate represented as a matrix $U$, there's an equivalent representation $U^\dagger$, known as its **Hermitian conjugate**. For now, the only thing we really need is: whatever effect $U$ has on a ket, $U^\dagger$ has the same effect on the corresponding bra.

$$|\psi\rangle \xrightarrow{U} \qquad \langle\psi| \xrightarrow{U^\dagger}$$

There's a notion of a **Hermitian** matrix — one equal to its own Hermitian conjugate:

$$U = U^\dagger$$

Most of the gates we've looked at so far are Hermitian: $X$, $Y$, $Z$, the Hadamard, the controlled-NOT — these are all Hermitian gates. The Hadamard, for example, turns $|0\rangle$ into $|+\rangle$ and $|+\rangle$ into $|0\rangle$ — and it has the same effect on bras:

$$H|0\rangle=|{+}\rangle, \qquad H|{+}\rangle=|0\rangle$$
$$\langle0|H=\langle{+}|, \qquad \langle{+}|H=\langle0|$$

(Also, $H$ applied to $|-\rangle$ gives $|1\rangle$, and $H$ applied to $|1\rangle$ gives $|-\rangle$ — I won't write those bra versions down, but they follow the same way.)

This means we can use $H$ to transform different Paulis into each other. $X$ has the form $X = |0\rangle\langle1|+|1\rangle\langle0|$. If we apply a Hadamard on both sides — $HXH$ — the $H$ applied to that $|0\rangle$ turns it into $|+\rangle$, the $H$ applied to that $\langle1|$ turns it into $\langle{-}|$, and so on for the other term, giving us $|{+}\rangle\langle{-}|$ from the first term and $|{-}\rangle\langle{+}|$ from the second. A gate that turns $|+\rangle$ into $-|-\rangle$... — wait, let's write it as it comes out: a gate that turns $|+\rangle$'s component to a $-$ and $|-\rangle$'s component to a $+$ is exactly what the $Z$ gate does:

$$HXH = Z$$

So taking an $X$ gate and putting a Hadamard before and after gives us the effect of a $Z$ gate — something that should be familiar from Hello Qiskit. And if you did an $H$ before and after a $Z$, you'd get an $X$ back:

$$HZH = X$$

---

## Turning a controlled-$X$ into a controlled-$Z$

This gives us a way of turning a controlled-NOT into a controlled-$Z$, and vice versa. Recall the controlled-NOT expressed with outer products for zero (first term) and one (second term) on the control, and identity/$X$ on the target respectively.

If we apply the gate $\mathbb{1}\otimes H$ before the controlled-NOT, and $\mathbb{1}\otimes H$ after it, the identities in the first term wouldn't do much — in fact nothing at all — but after, we'd get $H\,\mathbb{1}\,H$ for the first term, and $H\,X\,H$ for the other. What's $H\,\mathbb{1}\,H$? $H$ times identity is just $H$, so $H\,\mathbb{1}\,H$ is $H^2$ — and multiplying $H$ by itself gives you back the identity ($H^2=\mathbb{1}$):

$$C_x = |0\rangle\langle0|\otimes\mathbb{1} + |1\rangle\langle1|\otimes X$$

$$(\mathbb{1}\otimes H)\;C_x\;(\mathbb{1}\otimes H) = |0\rangle\langle0|\otimes(H\mathbb{1}H) + |1\rangle\langle1|\otimes(HXH)$$

$$= |0\rangle\langle0|\otimes\mathbb{1} + |1\rangle\langle1|\otimes Z, \qquad H^2=\mathbb{1}$$

So the first term stays identity, while the second term becomes $Z$ for exactly the reasons we just saw — instead of a controlled-$X$, we've now got a controlled-$Z$.

---

## $Z$-rotations conjugated by $X$

Another useful identity concerns rotations. Let's compare a $Z$-rotation on its own, $R_Z(\theta)$, to the same rotation sandwiched with an $X$ before and after.

As an example, take a particular point on the Bloch sphere — let's use the $|+\rangle$ state, since it has a convenient property. Apply $R_Z(\theta)$ to it, bringing us to some new point on the equator. Now consider doing an $X$ first, then that same rotation, then another $X$. Since we're starting at $|+\rangle$, and $X$ applied to $|+\rangle$ is just $|+\rangle$, the first $X$ takes us nowhere; then we do the $Z$-rotation, starting from the same place, so we end at the same place; and then the last $X$ — since $X$ is a $\pi$ rotation around the $x$-axis — takes us to the *other* side, rather than back to where the plain rotation ended up. Doing more examples, or just multiplying the matrices, shows that the result is again a rotation around the $Z$-axis by angle $\theta$, but now in the **other direction**:

$$X\;R_Z(\theta)\;X = R_Z(-\theta)$$

So sandwiching a $Z$-rotation between two $X$ gates flips its direction. (The exact same trick works for $Y$-rotations too: $X\;R_Y(\theta)\;X = R_Y(-\theta)$.)

---

## Building a controlled rotation

With that in mind, here's a circuit to think about: two rotations and two controlled-NOTs. Without any controlled-NOTs, on the bottom line you'd just have $R_Z(\theta)$ followed by $R_Z(-\theta)$ — these two combine to the identity, so nothing would happen: you'd rotate, then un-rotate, and get back exactly to where you were:

$$R_Z(-\theta)\,R_Z(\theta) = I$$

However, if we insert some $X$s around that negative rotation, it gets flipped, as we've just seen, into a *positive* rotation, due to the effect of these flipping the sign of the rotation — so what we'd have instead is a combined rotation of $2\theta$:

$$X\,R_Z(-\theta)\,X\,R_Z(\theta) = R_Z(2\theta)$$

So whether we get no rotation at all, or a rotation of $2\theta$, depends on whether or not we insert those $X$s — and that's exactly what a controlled-NOT does: whether or not we effectively have $X$s on this bottom line is *controlled* on what the top line is doing. So depending on whether the top qubit is $|0\rangle$ or $|1\rangle$, the bottom qubit either experiences no rotation at all, or a $Z$-rotation by angle $2\theta$ — and by choosing $\theta$, you can make this angle whatever you want:

$$\begin{array}{c}\text{top: }|0\rangle \text{ or } |1\rangle \\ \text{bottom: } R_Z(\theta)\ \oplus\ R_Z(-\theta)\ \oplus\end{array} \quad\longrightarrow\quad \text{controlled-}R_Z(2\theta)$$

So what we have here is a **controlled rotation around the $Z$ axis**. And this trick works exactly the same way for $Y$-rotations — since, similarly, $X\;R_Y(\theta)\;X = R_Y(-\theta)$, sandwiching a $Y$-rotation between $X$s the same way gives you the controlled-rotation form you'll see in the textbook version of this lecture.

---

## Closing

If you look in the textbook section, you'll find more examples of circuit identities, and if you go through the entirety of Hello Qiskit, you'll go through multiple circuit identities there as well — things like how to make a SWAP gate, or how to construct a Toffoli out of single- and two-qubit gates. I won't go through them all explicitly now, but you now have the tools to start trying to understand how these things work for yourself. And there is no better exercise in knowing how quantum computing works than to do just that.
