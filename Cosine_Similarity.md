# 📐 Cosine Similarity

Cosine similarity measures **how similar the directions of two vectors are**.

It is widely used in **Machine Learning, NLP, embeddings, semantic search, and RAG systems**.

---

## 1. What is Cosine Similarity?

The formula is:

$$
\boxed{
\cos(a,b)=\frac{a^Tb}{\|a\|_2\|b\|_2}
}
$$

Where:

- $a^Tb$ → dot product
- $\|a\|_2$ → L2 norm (length) of vector $a$
- $\|b\|_2$ → L2 norm (length) of vector $b$

In simple terms:

> **Cosine similarity measures how similarly two vectors are oriented, regardless of their magnitude.**

---

## 2. Breaking Down the Formula

### Numerator — Dot Product

$$
a^Tb
$$

The dot product measures the **alignment** between two vectors.

For:

$$
a=[a_1,a_2,\dots,a_n]
$$

and

$$
b=[b_1,b_2,\dots,b_n]
$$

the dot product is:

$$
a^Tb=\sum_{i=1}^{n}a_i b_i
$$

---

### Denominator — Vector Lengths

The L2 norm of a vector is:

$$
\|a\|_2=\sqrt{\sum_{i=1}^{n}a_i^2}
$$

Therefore:

$$
\|a\|_2\|b\|_2
$$

represents:

$$
(\text{length of }a)(\text{length of }b)
$$

So cosine similarity is essentially:

$$
\boxed{
\text{Cosine Similarity}
=
\frac{\text{Dot Product}}
{\text{Length of }a\times\text{Length of }b}
}
$$

---

# 3. Why Do We Divide by the Lengths?

Consider:

$$
a=[1,0]
$$

and:

$$
b=[10,0]
$$

Both vectors point in **exactly the same direction**, but $b$ is much longer.

### Dot Product

$$
a^Tb=(1)(10)+(0)(0)=10
$$

If we only used the dot product, we would get a large value because of the magnitude of $b$.

But cosine similarity asks:

> **"Do these vectors point in the same direction?"**

It removes the effect of magnitude through normalization.

### Norms

$$
\|a\|_2=1
$$

$$
\|b\|_2=10
$$

Therefore:

$$
\cos(a,b)
=
\frac{10}{1\times10}
=1
$$

So:

$$
\boxed{\cos(a,b)=1}
$$

This means the vectors are **perfectly aligned**.

---

# 4. Cosine Similarity and Angle

The most important intuition is:

$$
\boxed{\cos(a,b)=\cos\theta}
$$

where $\theta$ is the angle between the two vectors.

### Same Direction

$$
\theta=0^\circ
$$

$$
\cos(0^\circ)=1
$$

➡️ **Maximum similarity**

---

### 90° Apart

$$
\theta=90^\circ
$$

$$
\cos(90^\circ)=0
$$

➡️ **No directional similarity**

---

### Opposite Direction

$$
\theta=180^\circ
$$

$$
\cos(180^\circ)=-1
$$

➡️ **Opposite directions**

Therefore, for non-zero vectors:

$$
\boxed{-1\leq\cos(a,b)\leq1}
$$

### Quick Intuition

```text
Same direction
      ↑
      │
      │
      ↑
     1.0

90° apart
      ↑
      │────→
       0.0

Opposite directions
      ↑
      ↓
     -1.0
