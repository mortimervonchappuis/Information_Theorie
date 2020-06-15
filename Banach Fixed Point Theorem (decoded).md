# Banach Fixed Point Theorem

Let $(X, d)$ be a complete metric space. Then $T: X \to X$ is a contraction mapping if :

$$
\forall x, y \in X \, \exist q \in [0,1[: d(T(x), T(y)) \leq d(x, y)
$$



For $T$ there exists a fixed point $x^*$ such that $T(x^*) = x^*$.

### Proof

Let $x_0\in X$ and define a sequence $\{x_n\}$ by setting $x_{n+1} = T(x_n)$. We note, that the following inequality is satisfied:

$$
\forall n \in \mathbb{N}: d(x_{n+1}, x_n) \leq q^nd(x_1, x_0)
$$

This follows by induction on $n$ using the fact that $T$ is a contraction mapping. Then we show that $\{x_n\}$ is a Cauchysequence. Let $n, m \in \mathbb{N} \wedge n < m$:

$$
\begin{aligned}
d(x_n, x_m) & \leq \sum_{i=n}^{m-1} d(x_i, x_{i+1}) \\
& \leq d(x_0, x_1)\sum_{k=n}^{m-1}q^k \\
& = q^n d(x_0, x_1) \sum_{k=0}^{m-n-1}q^k \\
& \leq q^n d(x_0, x_1) \sum_{k=0}^\infty q^k \\
& = q^n d(x_0, x_1) \frac{1}{1-q}
\end{aligned}
$$

Let $\epsilon > 0$ by arbitrary. Since $q \in [0, 1[$ we can find $N$ so that:

$$
q^N < \frac{\epsilon(1-p)}{d(x_0, x_1)}
$$

Therefore we can write the previous inequality as:

$$
d(x_n, x_m) \leq q^n d(x_0, x_1) \frac{1}{1-q} < \frac{\epsilon(1-p)}{d(x_0, x_1)} d(x_0, x_1) \frac{1}{1-q}=\epsilon
$$

This proofs that the sequence $\{x_n\}$ is Cauchy. By completeness of $(X,d)$ the sequence has a limit $x^* \in X$. Furthermore $x^*$ must be a fixed point of $T$:

$$
x^* = \lim_{n \to \infty} x_n = \lim_{n \to \infty} T(x_{n-1}) = T(\lim_{n \to \infty} x_{n-1}) = T(x^*)
$$