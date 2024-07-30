# [18065](https://github.com/mitmath/18065)

# MIT Course 18.065/18.0651, Spring 2023

This is a repository for the course [18.065: Matrix Methods in Data Analysis, Signal Processing, and Machine Learning](http://student.mit.edu/catalog/m18a.html#18.065) at MIT in Spring 2023.   See also [18.065 from spring 2018](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/) (MIT OpenCourseWare) for a previous version of this class.

**Instructor**: [Prof. Steven G. Johnson](http://math.mit.edu/~stevenj).

**Lectures**: MWF1 in 2-190. Handwritten [notes are posted](https://www.dropbox.com/s/zny0l2njkhe5a8c/18.065%20Spring%202023.pdf?dl=0), along with [video recordings (MIT only)](https://canvas.mit.edu/courses/18680/external_tools/595).

**Office hours (virtual):** Thursdays at 4pm [via Zoom](https://mit.zoom.us/j/95322064681?pwd=ZzB3eHllMXpuWnNqc0NaeXZvUXF2dz09).

**Textbook**: [*Linear Algebra and Learning from Data*](https://math.mit.edu/~gs/learningfromdata/) by Gilbert Strang (2019).  (Additional readings will be posted in lecture summaries below.)

**Resources**: [Piazza discussion forum](https://piazza.com/mit/spring2023/18065), [pset partners](https://psetpartners.mit.edu/).

**Grading**: 50% homework, 50% final project.

**Homework**: Biweekly, due Fridays (2/17, 3/3, 3/17, 4/7, 4/21, 5/5) [on Canvas](https://canvas.mit.edu/courses/18680).  You may consult with other students or any other resources you want, but must write up your solutions *on your own*.  Psets are accepted until solutions are posted (sometime Friday); extensions require permission of instructor.

**Exams**: None.

**Final project**: Due **May 15** [on Canvas](https://canvas.mit.edu/courses/18680).  You can work in **groups of 1–3** ([sign up on Canvas](https://community.canvaslms.com/t5/Student-Guide/How-do-I-join-a-group-as-a-student/ta-p/468)).
* **1-page** proposal **due Monday April 3** [on Canvas](https://canvas.mit.edu/courses/18680) (right after spring break), but you are encouraged to discuss it with Prof. Johnson earlier to get feedback.
* Pick a problem involving "learning from data" (in the style of the course, but not *exactly* the same as what's covered in lecture), and take it further: to numerical examples, to applications, to testing one or more solution algorithms.  Must include computations (using any language).
* Final report **due May 15**, as an 8–15 page academic paper in the [style template](https://template-selector.ieee.org/secure/templateSelector/format?publicationTypeId=1&titleId=154&articleId=1) of [IEEE Transactions on Pattern Analysis and Machine Intelligence](https://www.computer.org/csdl/journal/tp).
* Like a good academic paper, you should **thoroughly reference** the published literature (citing both original articles and authoritative reviews/books where appropriate \[rarely web pages\]), tracing the historical development of the ideas and giving the reader pointers on where to go for more information and related work and later refinements, with references cited throughout the text (enough to make it clear what references go with what results). (Note: you may re-use diagrams from other sources, but all such usage must be _explicitly credited_; not doing so is [plagiarism](http://writing.mit.edu/wcc/avoidingplagiarism).) See some [previous topic areas](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/pages/final-project/).

What followes is a *brief* summary of what was covered in each lecture, along with links and suggestions for further reading.  It is
*not* a good substitute for attending lecture, but may provide a
useful study guide.

## Lecture 1 (Feb 6)

* Syllabus (above) and introduction.
* ![18.065 overview diagram](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/d6b9603509fe7de36c57a0ed8ebd92d2_chart_300.jpg)
* Column space, basis, rank, rank-1 matrices, A=CR, and AB=∑(col)(row)
* See handwritten notes and lecture video linked above.

**Further reading**: Textbook 1.1–1.3. [OCW lecture 1](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-1-the-column-space-of-a-contains-all-vectors-ax/)


## Lecture 2 (Feb 8)

* Matrix multiplication by blocks and columns-times-rows.  Complexity: standard algorithm for (m×p)⋅(p×n) is [Θ(mnp): roughly proportional](https://en.wikipedia.org/wiki/Big_O_notation) to mnp for large m,n,p, regardless of how we rearrange it into blocks. (There also [exist theoretically better](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication), but highly impractical, algorithms.)
* Briefly reviewed the "famous four" matrix factorizations: [LU](https://en.wikipedia.org/wiki/LU_decomposition), [diagonalization XΛX⁻¹ or QΛQᵀ](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix), [QR](https://en.wikipedia.org/wiki/QR_decomposition), and the [SVD UΣVᵀ](https://en.wikipedia.org/wiki/Singular_value_decomposition).  QR and QΛQᵀ in the columns-times-rows picture, especially QΛQᵀ (diagonalization for real A=Aᵀ) as a sum of symmetric rank-1 projections.
* The [four fundamental subspaces](https://web.mit.edu/18.06/www/Essays/newpaper_ver3.pdf) for an m×n matrix A of rank r, mapping "inputs" x∈ℝⁿ to "outputs" Ax∈ℝᵐ: the "input" subspaces C(Aᵀ) (row space, dimension r) and its [orthogonal complement](https://en.wikipedia.org/wiki/Orthogonal_complement) N(A) (nullspace, dimension n–r); and the "output" subspaces C(A) (column space, dimension r) and its orthogonal complement N(Aᵀ) (left nullspace, dimension m–r).
* [pset 1](psets/pset1.ipynb), due Friday Feb 17

**Further reading**: Textbook 1.3–1.6. [OCW lecture 2](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-2-multiplying-and-factoring-matrices/).  If you haven't seen [matrix multiplication by blocks](https://www.math.ucdavis.edu/~linear/old/notes9.pdf) before, [here is a nice video](https://www.youtube.com/watch?v=KCUgWj5nhYc).

## *Optional* Julia Tutorial: Wed Feb 8 @ 5pm via Zoom

* Virtually via Zoom.  See [the recording](https://mit.zoom.us/rec/share/n2B1-t0NoGd5pr9gNBLgDYme159TstNttH5PLMcYPsEFEThCohKIJPsLrZXRhaZZ.LMM65H-ATiUFXkPf?startTime=1675893372000) (MIT only).

A basic overview of the Julia programming environment for numerical computations that we will use in 18.06 for simple computational exploration.   This (Zoom-based) tutorial will cover what Julia is and the basics of interaction, scalar/vector/matrix arithmetic, and plotting — we'll be using it as just a "fancy calculator" and no "real programming" will be required.

* [Tutorial materials](https://github.com/mitmath/julia-mit) (and links to other resources)

If possible, try to install Julia on your laptop beforehand using the instructions at the above link.  Failing that, you can run Julia in the cloud (see instructions above).

## Lecture 3 (Feb 10)

* Orthogonal bases and unitary matrices "Q".

Choosing the right "coordinate system" (= "right basis" for linear transformations) is a key aspect of data science, in order to reveal and simplify information.  The "nicest" bases are often orthonormal.  (The opposite is a *nearly* linearly dependent "ill-conditioned" basis, which can greatly distort data.)

Orthonormal bases ⟺ QᵀQ=I, hence basis coefficients c=Qᵀx from dot products.  QQᵀ is orthogonal projection onto C(Q).  A square Q with orthonormal columns is known as a ["orthogonal matrix"](https://en.wikipedia.org/wiki/Orthogonal_matrix) or (more generally) as a ["unitary matrix"](https://en.wikipedia.org/wiki/Unitary_matrix): it has Qᵀ=Q⁻¹ (*both* its rows and columns are orthonormal).  Qx preserves length ‖x‖=‖Qx‖ and dot products (angles) x⋅y=(Qx)⋅(Qy).  Less obviously: *any* square matrix that preserves length must be unitary.

Some important examples of unitary matrices:
* [2×2 rotation matrices](https://en.wikipedia.org/wiki/Rotation_matrix)
* the identity matrix I
* any [permutation matrix](https://en.wikipedia.org/wiki/Permutation_matrix) P which re-orders a vector, and is simply a re-ordering of the rows/cols of I
* [Hadamard matrices](https://en.wikipedia.org/wiki/Hadamard_matrix): unitary matrices Hₙ/√n where Hₙ has entries of ±1 only.  For n=2ᵏ they are easy to construct recursively, and are known as [Walsh–Hadamard transforms](https://en.wikipedia.org/wiki/Hadamard_transform).  (See also the Julia [Hadamard package](https://github.com/JuliaMath/Hadamard.jl).)
* discrete [Haar wavelets](https://en.wikipedia.org/wiki/Haar_wavelet), which are unitary after a diagonal scaling and consist of entries ±1 and 0.  They are a form of ["time-frequency analysis"](https://en.wikipedia.org/wiki/Time%E2%80%93frequency_analysis) because they reveal information about *both* how oscillatory a vector is ("frequency domain") and *where* the oscillations occur ("time domain").
* orthonormal eigenvectors can be found for any real-symmetric ("Hermitian") matrix A=Aᵀ: A=QΛQᵀ
* the [SVD](https://en.wikipedia.org/wiki/Singular_value_decomposition) A=UΣVᵀ of *any* matrix A gives (arguably) the "best" orthonormal basis U for C(A) and the "best" orthonormal basis V for C(Aᵀ), which reveal a lot about A.
* orthonormal eigenvectors can *also* be found for any *unitary* matrix!  (The proof is similar to that for Hermitian matrices, but the eigenvalues |λ|=1 in this case.) Often, unitary matrices are used to describe *symmetries* of problems, and their eigenvectors can be thought of as a kind of "generalized Fourier transform".  (All of the familar Fourier transforms, including Fourier series, sine/cosine transforms, and discrete variants thereof, can be derived in this way. For example, the symmetry of a circle gives the Fourier series, and the symmetry of a sphere gives a "spherical-harmonic transform".)  For example, eigenvectors of a [cyclic shift permutation](https://en.wikipedia.org/wiki/Circular_shift) give the [discrete Fourier transform](https://en.wikipedia.org/wiki/Discrete_Fourier_transform), which is famously computed using [FFT algorithms](https://en.wikipedia.org/wiki/Fast_Fourier_transform).

**Further reading**: Textbook section 1.5 (orthogonality), 1.6 (eigenproblems), and 4.1 (Fourier); [OCW lecture 3](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-3-orthonormal-columns-in-q-give-q2019q-i/). The fact that preserving lengths implies unitarity is not obvious, but is proved in various textbooks; a concise summary is [found here](https://math.stackexchange.com/questions/3313702/does-preservation-of-induced-norm-imply-unitarity).  The relationship between symmetries and Fourier-like transforms can be most generally studied through the framework of "group representation theory"; see e.g. textbooks on "group theory in physics" like [Inui et al. (1996)](https://www.amazon.com/Applications-Physics-Springer-Solid-State-Sciences/dp/3540604456).  Of course, there are whole books *just* on the discrete Fourier transform (DFT), *just* on wavelet transforms, etcetera, and you can find lots of material online at many levels of sophistication.

## Lecture 4 (Feb 13)

* Eigenproblems, diagonalization, complex inner products, and the spectral theorem.

Reviewed eigenvectors/eigenvalues Ax=λx, which make a square matrix act like a scalar λ.   For an m×m matrix A, you get m eigenvalues λₖ from the roots (possibly repeated) of the [characteristic polynomial](https://en.wikipedia.org/wiki/Characteristic_polynomial) det(A-λΙ), and you almost always get m independent eigenvalues xₖ (except in the very rare case of a [defective matrix](https://en.wikipedia.org/wiki/Defective_matrix)).

Went through the example of the 4×4 cyclic-shift permutation P from last lecture, and showed that P⁴x=x ⥰ λ⁴=1 ⥰ λ=±1,±i.  We can then easily obtain the corresponding eigenvectors, and put them into the "discrete Fourier transform" matrix F.

I then claimed that the eigenvectors (properly scaled) are orthonormal, so that F is unitary, but there is a catch: we need to **generalize our definition of "dot"/inner product** for complex vectors and matrices.   For complex vectors, the dot product x⋅y is `conj`(xᵀ)y (`conj`=[complex conjugate](https://en.wikipedia.org/wiki/Complex_conjugate)), *not* xᵀy.   And the length of a vector is then  ‖x‖² = x⋅x = ∑ᵢ|xᵢ|², which is always ≥ 0 (and = 0 only for x=0).   The ["adjoint"](https://en.wikipedia.org/wiki/Conjugate_transpose) `conj`(xᵀ) is sometimes denoted "xᴴ" (or x<sup>*</sup> in math, or x<sup>†</sup> in physics).   A unitary matrix is now more generally one for which QᴴQ=I, and we see that our Fourier matrix F is indeed unitary.  And unitary matrices still preserve lengths (and inner products) with the complex inner product.

If we do a **change of basis** x=Bc, then Ax=λx is transformed to Cc=λc, where C=B⁻¹AB.  C and A are called [similar matrices](https://en.wikipedia.org/wiki/Matrix_similarity), and we see that they are just the same linear operator in different bases; similar matrices always have identical eigenvalues, and eigenvectors transformed by a factor of B.

The most important change of basis for eigenproblems is changing to the *basis of eigenvectors* X, and showed that this gives the [diagonalizaton](https://en.wikipedia.org/wiki/Diagonalizable_matrix) X⁻¹AX=Λ ⟺ **A = XΛX⁻¹**.  However, this basis may be problematic in a variety of ways if the eigenvectors are nearly dependent (X is nearly singular or "ill-conditioned", corresponding to A being *nearly defective*).

The *nice* case of diagonalization is when you have **orthonormal eigenvectors** X=Q, and it turns out that this arises **whenever A commutes with its conjugate-transpose Aᴴ** (these are called [normal matrices](https://en.wikipedia.org/wiki/Conjugate_transpose)), and give **A=QΛQᴴ**.  Two important cases are:
* [Hermitian matrices](https://en.wikipedia.org/wiki/Hermitian_matrix) A=Aᴴ, and especially the special case of **real-symmetric matrices** (real A=Aᵀ) — not only are their eigenvectors orthogonal, but their eigenvalues λ are **real**.  In fact, if A is real-symmetric, then its *eigenvectors* are real too, and we can work with a purely real diagonalization A=QΛQᵀ.
* Unitary matrices Aᴴ=A⁻¹.  In this case, we can easily show that |λ|=1, and then prove orthogonality of eigenvectors from the fact that unitary matrices preserve inner products.

**Further reading** [OCW lecture 4](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-4-eigenvalues-and-eigenvectors/) and textbook section I.6.
* Complex numbers and vectors: See [18.06 lecture 26](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/lecture-26-complex-matrices-fast-fourier-transform/) on complex matrices.  This [brief review of complex numbers](https://web.stanford.edu/~boyd/ee102/complex-primer.pdf) (from Stephen Boyd at Stanford) is at about the level we need.  There are many more basic reviews, e.g. from [Khan academy](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:complex), that you can find online.
* Similar matrices are discussed in [18.06 lecture 28](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/lecture-28-similar-matrices-and-jordan-form/), and diagonalization is in [18.06 lecture 22](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/lecture-22-diagonalization-and-powers-of-a/).
* Hermitian (real-symmetric) matrices: [18.06 lecture 25](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/lecture-25-symmetric-matrices-and-positive-definiteness/).

## Lecture 5 (Feb 15)

* (Symmetric/Hermitian) positive definite ("SPD") matrices A=Aᵀ: λ > 0 ⟺ xᵀAx > 0 (for x ≠ 0) ⟺ A = BᵀB (B full column rank) ⟺ pivots > 0 (in Gaussian elimination / LU or [Cholesky](https://en.wikipedia.org/wiki/Cholesky_decomposition) factorization) ⟺ ...  (but it does *not* mean all entries of A are necessarily positive or vice versa!)
* BᵀB matrices arise in SVDs, least-squares, statistics (covariance matrices), and many other problems.
* Positive-definiteness of the [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix) Hᵢⱼ=∂²f/∂xᵢ∂xⱼ is the key test for determining whether x∈ℝⁿ is a [local minimum](https://en.wikipedia.org/wiki/Maximum_and_minimum) of f(x), since f(x+δ)=f(x)+∇fᵀδ + ½δᵀHδ + (higher-order).   For example, H=2A for the [convex](https://en.wikipedia.org/wiki/Convex_function) [quadratic](https://en.wikipedia.org/wiki/Quadratic_form) "bowl" function f(x)=xᵀAx+bᵀx
* Analogous definitions of "positive semidefinite" (> 0 replaced by ≥ 0) and negative definite/semidefinite (< 0 / ≤ 0).

**Further reading** [OCW lecture 5](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-5-positive-definite-and-semidefinite-matrices/) and textbook section I.7.   In Julia, the [`isposdef`](https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/#LinearAlgebra.isposdef) function checks whether a matrix is positive definite, and does so using a Cholesky factorization (which is just Gaussian elimination speeded up 2× for SPD matrices, and fails if it encounters a negative pivot).   See also [these lecture slides from Stanford](http://www.seas.ucla.edu/~vandenbe/133A/lectures/chol.pdf) for more properties, examples, and applications of SPD matrices.  See the [matrix calculus course at MIT](https://github.com/mitmath/matrixcalc) for a more general presentation of derivatives, gradients, and second derivatives (Hessians) of functions with vector inputs/outputs.

## Lecture 6 (Feb 17)

* "Reduced"/"compact" SVD A=UᵣΣᵣVᵣᵀ=∑σₖuₖvₖᵀ, "full" SVD A=UΣVᵀ, and "thin" SVD (what computers actually return, with zero singular values replaced by tiny roundoff errors).
* Uᵣ and Vᵣ as the "right" bases for C(A) and C(Aᵀ). Avₖ=σₖvₖ
* SVD and eigenvalues: U and V as eigenvectors of AAᵀ and AᵀA, respectively, and σₖ² as the positive eigenvalues.
* Deriving the SVD from eigenvalues: the key step is showing that AAᵀ and AᵀA share the same positive eigenvalues, and λₖ=σₖ², with eigenvectors related by a factor of A. From there you can work backwards to the SVD.
* [pset 1 solutions](psets/pset1sol.ipynb)
* [pset 2](psets/pset2.ipynb): Due March 3 at 1pm

**Further reading**: [OCW lecture 6](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-6-singular-value-decomposition-svd/) and textbook section I.8.  The [Wikipedia SVD article](https://en.wikipedia.org/wiki/Singular_value_decomposition).

## Lecture 7 (Feb 21)

* [SVD demo with image "compression"](https://nbviewer.org/github/mitmath/1806/blob/fall22/notes/SVD-intro.ipynb)
* [Low-rank approximation](https://en.wikipedia.org/wiki/Low-rank_approximation) and the Eckart–Young theorem.
* Vector [norms](https://en.wikipedia.org/wiki/Norm_(mathematics)) (ℓ², ℓ¹, and ℓ∞) and [Matrix norms](https://en.wikipedia.org/wiki/Matrix_norm).  Unitarily invariant norms, and unitary invariance of singular values.
* [Matrix completion], the ["Netflix problem"](https://en.wikipedia.org/wiki/Netflix_Prize), and the nuclear norm.

**Further reading**: Textbook sections I.9, I.11, III.5. [OCW lecture 7](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-7-eckart-young-the-closest-rank-k-matrix-to-a/) and [lecture 8](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-8-norms-of-vectors-and-matrices/).

## Lecture 8 (Feb 22)
* Mean, variance, and covariance.
* Diagonalizing the covariance matrix: [Principal components analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis).
* [PCA demo](https://nbviewer.org/github/mitmath/1806/blob/fall22/notes/Statistics-and-PCA.ipynb)

**Further reading**: Textbook sections I.9, V.1, V.4.  [OCW lecture 7](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-7-eckart-young-the-closest-rank-k-matrix-to-a/) and [OCW lecture 20](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-20-definitions-and-inequalities/).

## Lecture 9 (Feb 24)

* [pseudo-inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse) A⁺=VΣ⁺Uᵀ
* Least-squares: solve Ax≈b by minimizing ‖b-Ax‖ ⟺ solving AᵀAx̂=Aᵀb
* 4 methods for least squares: (1) Normal equations AᵀAx̂=Aᵀb (the fastest method, but least robust to roundoff errors etc); (2) orthogonalization A=QR ⟹ Rx̂=Qᵀb (much more robust, this is essentially what `A \ b` does in Julia for non-square `A`); (3) pseudo-inverse x̂=A⁺b ([`pinv(A)*b`](https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/#LinearAlgebra.pinv) in Julia; this lets you "regularize" the problem by dropping tiny singular values); (4) ["ridge" or "Tikhonov" regularization](https://en.wikipedia.org/wiki/Ridge_regression) (AᵀA + δ²I)⁻¹Aᵀb ⟶ x̂ as δ→0 (δ≠0 is useful to "regularize" ill-conditioned fitting problems where A has nearly dependent columns, making the solutions more robust to errors).
* [Least-squares demo](https://nbviewer.org/github/mitmath/1806/blob/fall22/notes/Least-Square%20Fitting.ipynb)

**Further reading:** Textbook section II.2 and [OCW lecture 9](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-9-four-ways-to-solve-least-squares-problems/).  Many advanced linear-algebra texts talk about the practical aspects of roundoff errors in QR and least-squares, e.g. *Numerical Linear Algebra* by Trefethen and Bau (the 18.335 textbook). A nice historical review can be found in the article [Gram-Schmidt orthogonalization: 100 years and more](https://doi.org/10.1002/nla.1839).  Rarely (on a computer) explicitly form AᵀA or solve the normal equations: it turns out that this greatly exacerbates the sensitivity to numerical errors (in 18.335, you would learn that it squares the [condition number](https://en.wikipedia.org/wiki/Condition_number)). Instead, we typically use the A=QR factorization and solve Rx̂=Qᵀb.  Better yet, just do `A \ b` (in Julia or Matlab) or the equivalent in other languages (e.g. [`numpy.linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html)), which will use a good algorithm.   (Even professionals can [get confused about this](https://discourse.julialang.org/t/efficient-way-of-doing-linear-regression/31232/33?u=stevengj).)

## Lecture 10 (Feb 27)

* Training vs test data: [VMLS slides p. 294](https://web.stanford.edu/~boyd/vmls/vmls-slides.pdf#page=294)
* Conditioning: κ(A) = (max σ)/(min σ) is the [condition number](https://en.wikipedia.org/wiki/Condition_number) of a matrix A, and gives us a bound on the "amplification" ‖Δx‖/‖x‖ ≤ κ(a) ‖Δb‖/‖b‖ of the relative error from inputs (b) to outputs (x) when solving Ax=b (including least-squares).   "Ill-conditioned problems" (κ≫1) magnify noise and other errors, and typically require some **regularization** (e.g. dropping smallest σ's) that **trades off robustness for accuracy** ‖b-Ax‖.
* Ridge/Tikhonov/ℓ² regularization: minimize ‖b-Ax‖₂² + δ²‖x‖₂² for some *penalty* δ≠0 to push the solution towards smaller x.  (More generally, δ²‖Dx‖₂² for some matrix D.)  This gives (AᵀA+δ²I)x̂=Aᵀb, which is similar to A⁺b but replaces 1/σ with σ/(σ²+δ²).  Effectively, this drops small σ's, but doesn't require an SVD and generalizes to other types of penalties.  (Example: [VMLS slides pg. 346](https://web.stanford.edu/~boyd/vmls/vmls-slides.pdf#page=346).)
* Under-determined problems: for "wide" matrices, Ax=b has many solutions (we can add any N(A) vector to a solution).  A common way to pick a solution is to pick the **minimum-norm** solution: minimize ‖x‖₂ subject to Ax=b.  (It turns out that this gives x̂=A⁺b!)

**Further reading**: Training/test data: [VMLS section 13.2](https://web.stanford.edu/~boyd/vmls/vmls.pdf#page=270). Condition numbers: Strang exercises II.3, [OCW video lecture 10](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-10-survey-of-difficulties-with-ax-b/), and [these 18.06 notes](https://github.com/mitmath/1806/blob/master/notes/Conditioning.ipynb); a more in-depth treatment can be found in e.g. *Numerical Linear Algebra* by Trefethen and Bau (the 18.335 textbook).  Tikhonov regularization: Strang section II.2, OCW video lecture 10, [VMLS section 15.3](https://web.stanford.edu/~boyd/vmls/vmls.pdf#page=326).  Underdetermined minimum-norm solutions: Strang section II.2, [OCW video lecture 11](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-11-minimizing-2016x2016-subject-to-ax-b/), [UIUC *Nonlinear Programming* lecture notes](https://faculty.math.illinois.edu/~mlavrov/docs/484-spring-2019/ch4lec4.pdf).

## Lecture 11 (Mar 1)

* Minimum-norm solutions x̂=A⁺b=Aᵀ(AAᵀ)⁻¹: smallest ‖x‖₂ for underdetermined problems Ax=b for "wide" A.
* Other common norms: ℓ¹ and ℓ<sup>∞</sup>, and sparsity with ‖x‖₁ norm ([LASSO regularization](https://en.wikipedia.org/wiki/Lasso_(statistics))).
* Avoid AᵀA: it squares the condition number κ(AᵀA)=κ(A)²
* Gram–Schmidt orthogonalization and QR factorization.

**Further reading**: Strang II.2, II.4.

## Lecture 12 (Mar 3)

* **QR factorization**: "thin" vs. "full" QR; practical considerations: pivoted QR, instability of classical Gram–Schmidt vs. modified G–S or "G–S twice" or Householder/Givens QR; the fact that many QR algorithms don't give you Q explicitly, only a fast way to multiply Qx or Qᵀy.
* Usage of QR for least-squares problem: AᵀAx̂=Aᵀb ⥰ Rx̂=Qᵀb.   (But this does not mean Ax̂=b!  QQᵀ is orthogonal projection onto C(A), ≠ I in general!)   This avoids squaring the condition number since κ(R)=κ(A).
* **Large-scale linear algebra**:  When solving m×m Ax=b for large m, we have a few options:
  - Dense linear algebra: Gaussian elimination, QR, eigenvalues, SVD, etcetera, assuming that A is just m×m numbers with no special structure.  Cost is Θ(m³), memory is Θ(m²).  Usually you run out of memory before running out of time! (m ∼ 10⁴ is close to filling up memory, but runs in only few minutes.)
  - Sparse-direct methods: For [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) (mostly 0), only store and compute with nonzero entries.  If a clever ordering is chosen for rows/cols, Gaussian elimination can often produce mostly sparse L and U factors!  (This is what `A \ b` does in Julia if `A` is a [sparse-matrix type](https://github.com/JuliaSparse/SparseArrays.jl).)   But for very big problems even these methods can eventually run out of memory.
  - Iterative methods: start with a "guess" for x (usually x=0 or x=random), and iteratively make it closer to a solution **using only A-times-vector operations** (and linear combinations and dot products).  Requires a fast A-times-vector, e.g. if A is sparse, low rank, a convolution, or some combination thereof.   Modern methods include [GMRES](https://en.wikipedia.org/wiki/Generalized_minimal_residual_method), [BiCGSTAB(ℓ)](https://en.wikipedia.org/wiki/Biconjugate_gradient_stabilized_method), [conjugate gradient (CG)](https://en.wikipedia.org/wiki/Conjugate_gradient_method), and others.
  - Randomized linear algebra: by multiplying A on the left/right by small random wide/thin matrices, carefully chosen, we can construct an approximate "sketch" of A that can be used to estimate the SVD, solutions to least-squares, etcetera, and can also accelerate iterative solvers.
  - Tricks for special cases: there are various specialized techniques for convolution/circulant matrices (via FFTs), [banded matrices](https://en.wikipedia.org/wiki/Band_matrix) (linear-time methods), and low-rank updates ([Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula))
* [pset 2 solutions](psets/pset2sol.ipynb)
* [pset 3](psets/pset3.ipynb) (due 3/17)

**Further reading:** For Gram–Schmidt and QR, see further reading for lecture 9.  Texbook section II.1, [OCW video lecture 10](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-10-survey-of-difficulties-with-ax-b/). Sparse-direct solvers are described in detail by the book *Direct Methods for Sparse Linear Systems* by Davis.  Iterative methods: More advanced treatments include the book *Numerical Linear Algebra* by Trefethen and Bao, and surveys of algorithms can be found in the *Templates* books for [Ax=b](http://www.netlib.org/linalg/html_templates/Templates.html) and [Ax=λx](http://web.cs.ucdavis.edu/~bai/ET/contents.html).  [Some crude rules of thumb](https://github.com/mitmath/18335/blob/spring20/notes/solver-options.pdf) for solving linear systems (from 18.335 spring 2020).

## Lecture 13 (Mar 6)

* Continued summary of large-scale linear algebra from lecture 12, mentioning randomized algorithms (which we will cover in more detail later), such as "sketched" least-squares and randomized SVD, and also specialized algorithms for particular cases.
* Krylov methods: defined [Krylov subspaces](https://en.wikipedia.org/wiki/Krylov_subspace) reachable by iterative algorithms, defined a Krylov algorithm (loosely) an iterative algorithm that finds the "best" solution in the whole Krylov space (possibly approximately) on the n-th step.  Gave [power iteration](https://en.wikipedia.org/wiki/Power_iteration) for largest |λ| as an example of something *not* a Krylov method.  Explained why the basis (b Ab A²b ⋯) is a poor (ill-conditioned) choice, and instead explained the [Arnoldi iteration](https://en.wikipedia.org/wiki/Arnoldi_iteration) to find an orthonormal basis Qₙ by (essentially) Gram–Schmidt, leading to the [GMRES algorithm](https://en.wikipedia.org/wiki/Generalized_minimal_residual_method) for Ax=b.

**Further reading:** Arnoldi iterations and GMRES are covered in the Strang textbook section II.1, and briefly in [OCW lecture 12](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-12-computing-eigenvalues-and-singular-values/); much more detail is found other sources (Trefethen, etc.) noted in the further reading for Lecture 12.  A review of randomized linear algebra can be found in the Strang textbook sec. II.4, and also in [Halko, Martinsson, and Tropp (2011)](https://epubs.siam.org/doi/10.1137/090771806).  A recent paper on a variety of new randomized algorithms, e.g. for "sketched" least-square problems or to accelerate iterative algorithms like GMRES, is [Nakatsukasa and Tropp (2022)](https://arxiv.org/pdf/2111.00113.pdf).  A nice review of the randomized SVD can be found in a blog post by [Gregory Gundersen (2019)](https://gregorygundersen.com/blog/2019/01/17/randomized-svd/).


## Lecture 14 (Mar 8)

* Krylov wrap-up:
  - GMRES caveats: storage is Θ(mn) after n steps, and cost of orthogonalization is Θ(mn²), so in practice one is often limited to n ≲ 100.  Workarounds include: "[restarted GMRES](https://personal.math.vt.edu/embree/39961.pdf)", randomized "[sketched GMRES](https://arxiv.org/pdf/2111.00113.pdf)", and approximate Krylov methods such as biCGSTAB(ℓ), QMR, or DQGMRES.   If A is Hermitian positive-definite, however, then there is ideal Krylov method called [conjugate gradient (CG)](https://en.wikipedia.org/wiki/Conjugate_gradient_method) that "magically" searches the whole Krylov space using only the two most recent search directions on each iteration; CG is [closely related](https://www.sciencedirect.com/science/article/abs/pii/S0893608003001709) to the "momentum" terms used in stochastic gradient descent / machine learning (covered later in 18.065).
  - GMRES convergence theory is complicated (see e.g. lecture 35 in [Trefethen & Bau](https://people.maths.ox.ac.uk/trefethen/text.html)), but basically it converges faster if the eigenvalues are mostly "clustered" (making A more like I).  You can therefore accelerate convergence by finding a [preconditioner](https://en.wikipedia.org/wiki/Preconditioner) matrix M such that MA has more-clustered eigenvalues (M is a "crude inverse" of A), and then solve MAx=Mb instead of Ax=b.  This can accelerate convergence by orders of magnitude, but finding a good preconditioner is a tricky problem-dependent task.
  - Krylov methods also exist for eigenproblems (e.g. Arnoldi and Jacobi-Davidson methods, or Lanczos and LOPCG for Hermitian problems), the SVD (requiring both Ax and Aᵀy operations), least-squares problems, and so on.
* Randomized linear algebra:
  - Randomized SVD, as covered in these notes by [Gregory Gundersen (2019)](https://gregorygundersen.com/blog/2019/01/17/randomized-svd/)
  - Randomized matrix multiplication AB ≈ random sampling (col j of A)(row j of B)/pⱼ with probability pⱼ. Choosing pⱼ proportional to ‖col j of A‖⋅‖row j of B‖ minimizes the variance of this estimate!  See Strang textbook section II.4 and [OCW lecture 13](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-13-randomized-matrix-multiplication/).

**Further reading:** See links above, and further reading from lecture 13.

## Lecture 15 (Mar 10)

* [Weighted least squares (WLS)](https://en.wikipedia.org/wiki/Weighted_least_squares) and [generalized least squares (GLS)](https://en.wikipedia.org/wiki/Generalized_least_squares): when fitting a model with noisy measurements, we want to *weight* the least-squares minimization inversely with the errors (variances) in the measurements (WLS), or more generally with the inverse of the measurement correlation matrix (GLS); see textbook section V.5.
 - Reviewed correlation matrix V and its positive semidefiniteness/definiteness (textbook section V.4).
 - Framed in terms of minimizing a [weighted ℓ² norm](https://math.stackexchange.com/questions/394237/understanding-weighted-inner-product-and-weighted-norms) ‖b-Ax‖<sub>V⁻¹</sub> and gave the WLS formula x̂=(AᵀV⁻¹A)⁻¹AᵀV⁻¹b = Lb.
 - This is an [unbiased estimator](https://en.wikipedia.org/wiki/Bias_of_an_estimator) if the measurement errors are unbiased.
 - Correlation matrix ("error bars") in the estimate x̂ is then given by W=LVLᵀ=(AᵀV⁻¹A)⁻¹ (textbook V.5).
* [Gauss–Markov theorem](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem): WLS/GLS is the unbiased linear estimator that *minimizes the variance* of the estimated parameters x.
  - in particular, showed that *any* other unbiased linear estimator gives a covariance W′ = W + (positive semidefinite), which results in ‖W′‖≥‖W‖ in the ℓ² (induced) or Frobenius norms
  - this means that OLS squares is the best choice when the errors are unbiased, independent, and have equal variances (["homoskedastic"](Homoscedasticity_and_heteroscedasticity))

**Further reading:** In addition to the links above, these subjects are covered in countless statistics textbooks and courses.  For example, see [these course notes from CMU](https://www.stat.cmu.edu/~cshalizi/mreg/15/lectures/24/lecture-24--25.pdf)


## Lecture 16 (Mar 13)

* [Optimization overview](https://docs.google.com/presentation/d/1K8BFfd-_6IWML2zpj_V88GvBjuJiK8EPHqYabDMU3CU/edit?usp=sharing) slides

Broad overview of optimization problems (see slides). The most general formulation is actually quite difficult to solve, so most algorithms (especially the most efficient algorithms) solve various special cases, and it is important to know what the key factors are that distinguish a particular problem. There is also something of an art to the problem formulation itself, e.g. a nondifferentiable minimax problem can be reformulated as a nicer differentiable problem with differentiable constraints.

**Further reading:** There are many textbooks on [nonlinear optimization](http://www.athenasc.com/nonlinbook.html) algorithms of various sorts, including specialized books on [convex optimization](http://web.stanford.edu/~boyd/cvxbook/), [derivative-free optimization](http://bookstore.siam.org/mp08/), etcetera.  A useful review of topology-optimization methods can be found in [Sigmund and Maute (2013)](https://link.springer.com/article/10.1007/s00158-013-0978-6).

## Lecture 17 (Mar 15)

* Matrix calculus — see also [our IAP 2023 course 18.S096](https://github.com/mitmath/matrixcalc).

Reviewed and broadened differential calculus (18.01 and 18.02) from the perspective of 18.06, where we view a derivative f′(x) as a [linear operator](https://en.wikipedia.org/wiki/Linear_map) acting on a small change in the input (dx) to give you the change in the output (df) to *first order* in dx ("linearized").   This viewpoint makes it easy to generalize derivatives, to scalar-valued functions of vectors where f′(x) is the transposed gradient (∇f)ᵀ, to vector-valued functions of vectors where f′(x) is the [Jacobian matrix](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant), and even to matrix-valued functions of matrices like f(x)=A² ⥰ df = A×dA+dA×A or f(x)=A⁻¹ ⥰ df=–A⁻¹×dA×A⁻¹; in both these cases f′(x) is a linear operator f′(x)[dA] that takes dA in and gives df out, but *cannot* be written simply as (matrix)×dA.

Derivatives viewed as linear approximations have many important applications in science, machine learning, statistics, and engineering. For example, ∇f is essential for large-scale optimization of scalar-valued functions f(x), and we will see that *how* you compute the gradient is also critical for practical reasons.  As another example, there is the **multidimensional Newton** algorithm for finding roots f(x)=0 of systems of nonlinear equations: At each step, you just solve a *linear* system of equations with the Jacobian matrix of f(x), and it converges incredibly rapidly.

**Further reading**: This material was presented in much greater depth in our [18.S096: Matrix Calculus](https://github.com/mitmath/matrixcalc) course in IAP 2022 and IAP 2023.    The viewpoint of derivatives as linear operators (also called [Fréchet derivatives](https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative)) was covered in lectures 1 and 2 of 18.S096, Newton's method was covered in lecture 4, and automatic differentiation was covered in lectures 5 and 8 — see the posted lecture materials and the further-reading links therein.   This [notebook](https://nbviewer.org/github/mitmath/1806/blob/fall22/notes/Newton-Thomson-example.ipynb) has a Newton's method example demo where we solve a 2d version of the famous [Thomson problem](https://en.wikipedia.org/wiki/Thomson_problem) to find the equilibrium position of N repulsive "point charges" constrained to lie on a circle; more generally, a sphere or hypersphere.

## Lecture 18 (Mar 17)

* d(A⁻¹), adjoint problems, chain rules, and forward vs reverse mode (backpropagation) derivatives
* [pset 3 solutions](psets/pset3sol.ipynb)
* [pset 4](psets/pset4.ipynb), due 4/7

Showed that d(A⁻¹)=–A⁻¹ dA A⁻¹.  (For example, if you have a matrix A(t) that depends on a scalar t∈ℝ, this tells you that d(A⁻¹)/dt = –A⁻¹ dA/dt A⁻¹.)   Applied this to computing ∇ₚf for scalar functions f(A⁻¹b) where A(p) depends on some parameters p∈ℝⁿ, and showed that ∂f/∂pᵢ = -(∇ₓf)ᵀA⁻¹(∂A/∂pᵢ)x.  Moreover, showed that it is critically important to evaluate this expression from *left to right*, i.e. first computing vᵀ=-(∇ₓf)ᵀA⁻¹m, which corresponds to solving the "adjoint (transposed) equation" Aᵀv=–∇ₓf.  By doing so, you can compute both f and ∇ₚf at the cost of only "two solves" with matrices A and Aᵀ.  This is critically important in enabling engineering/physics optimization, where you often want to optimize a property of the solution A⁻¹b of a physical model A depending on many design variables p (e.g. the distribution of materials in space).

More generally, presented the chain rule for f(g(x)) (f'(x)=g'(h(x))h'(x), where this is a *composition* of two linear operations, performing h' then g' — g'h' ≠ h'g'!).   For functions from vectors to vectors, the chain rule is simply the *product of Jacobians*.   Moreover, as soon as you compose 3 or more functions, it can a make a huge difference whether you multiply the Jacobians from left-to-right ("reverse-mode", or "backpropagation", or "adjoint differentiation") or right-to-left ("forward-mode"). Showed, for example, that if you have *many inputs but a single output* (as is common in machine learning and other types of optimization problem), that it is vastly more efficient to multiply left-to-right than right-to-left, and such "backpropagation algorithms" are a key factor in the practicality of large-scale optimization (including machine learning and neural nets).

**Further reading:**   For the derivative of A(t)⁻¹, see Strang sec. III.1 and [OCW lecture 15](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-15-matrices-a-t-depending-on-t-derivative-da-dt/); for backpropagation, see Strang sec. VII.3 and [OCW lecture 27](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-27-backpropagation-find-partial-derivatives/).  See also [these slides](https://docs.google.com/presentation/d/1U1lB5bhscjbxEuH5FcFwMl5xbHl0qIEkMf5rm0MO8uE/edit?usp=sharing) from [our matrix calculus course](https://github.com/mitmath/matrixcalc) (lecture 4) on adjoint methods for f(A⁻¹b) and similar problems in engineering design. See the [notes on adjoint methods](https://github.com/mitmath/18335/blob/spring21/notes/adjoint/adjoint.pdf) and [slides](https://github.com/mitmath/18335/blob/spring21/notes/adjoint/adjoint-intro.pdf) from 18.335 in spring 2021 ([video](https://mit.zoom.us/rec/share/xLxMyhBSoIhSFxce5lHb1ubItby5BKFs6mgJJ7kMmjotETmaYm4YA22TA8w8n13i.6sTEFrkkloG7LFeR?startTime=1619463273000)) The terms "forward-mode" and "reverse-mode" differentiation are most prevalent in [automatic differentiation (AD)](https://en.wikipedia.org/wiki/Automatic_differentiation). You can find many, many articles online about [backpropagation](https://en.wikipedia.org/wiki/Backpropagation) in neural networks.  This [video on the principles of AD in Julia](https://www.youtube.com/watch?v=UqymrMG-Qi4) by [Dr. Mohamed Tarek](https://github.com/mohamed82008) also starts with a similar left-to-right (reverse) vs right-to-left (forward) viewpoint and goes into how it translates to Julia code, and how you define custom chain-rule steps for Julia AD.

## Lecture 19 (Mar 20)

* Line minimization and [steepest descent](https://en.wikipedia.org/wiki/Gradient_descent).
* Newton steps and the Hessian matrix H
* Condition number κ(H) of the Hessian and convergence of steepest descent
* Example application: iteratively solving Ax=b (for A=Aᵀ positive definite) by minimizing f(x)=xᵀAx - xᵀb.  (See also the end of this [example notebook](https://github.com/mitmath/1806/blob/fall22/notes/Dense-and-Sparse.ipynb).)

**Further reading**: Strang section VI.4; [OCW lecture 21](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-21-minimizing-a-function-step-by-step/) and [OCW lecture 22](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-22-gradient-descent-downhill-to-a-minimum/).

## Lecture 20 (Mar 22)

* Momentum terms, [nonlinear conjugate gradient](https://en.wikipedia.org/wiki/Nonlinear_conjugate_gradient_method), and accelerated gradient descent
* [m-strongly convex and M-smooth functions](https://angms.science/doc/CVX/CVX_alphabeta.pdf) (i.e. 2nd derivative bounded above and below by m and M, i.e. ∇f is M Lipschitz)

**Further reading**: Strang section VI.4 and [OCW lecture 23](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-23-accelerating-gradient-descent-use-momentum/).  Conjugate gradient as an ideal Krylov method is covered by many authors, e.g. in [Trefethen and Bau](https://people.maths.ox.ac.uk/trefethen/text.html) lecture 38 or by [Shewchuk (1994)](http://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf); nonlinear conjugate gradient is reviewed by [Hager and Zhang (2006)](http://people.cs.vt.edu/~asandu/Public/Qual2011/Optim/Hager_2006_CG-survey.pdf) and its connection to "momentum" terms is covered by e.g. [Bhaya and Kaszkurewicz (2004)](https://www.sciencedirect.com/science/article/pii/S0893608003001709).  For accelerated gradient descent, see these [lecture notes](http://www.damtp.cam.ac.uk/user/hf323/M19-OPT/lecture5.pdf) from H. Fawzi at Cambridge Univ, and [this blog post](http://awibisono.github.io/2016/06/20/accelerated-gradient-descent.html) by A. Wibosono at Yale.  A recent article by [Karimi and Vavasis (2021)](https://arxiv.org/abs/2111.11613) presents an algorithm that blends the strengths of nonlinear conjugate gradient and accelerated gradient descent.

## Lecture 21 (Mar 24)

* [Stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent): [Julia notebook](notes/Stochastic-Gradient-Descent.ipynb)

**Further reading:** Strang section VI.5 and [OCW lecture 25](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-25-stochastic-gradient-descent/).  There are many, many tutorials on this topic online. See also the links and references in the [Julia notebook](notes/Stochastic-Gradient-Descent.ipynb).

## Lecture 22 (Apr 3)

* [slides from Boyd, chapter 5](https://github.com/mitmath/18335/blob/spring21/notes/boyd-ch5-slides.pdf)

In order to handle optimization problems with constraints, it's useful
to first generalize the local optimality criterion ∇f₀=0 for unconstrained problems, and this leads us into **Lagrangians**, **duality**, and **KKT conditions**.

Started by reviewing the basic idea of Lagrange multipliers to find an extremum of one function f₀(x) and one equality constraint h₁(x)=0. We instead find an extremum of L(x,ν₁)=f₀(x)+ν₁h₁(x) over x and the _Lagrange multiplier_ ν₁. The ν₁ partial derivative of L ensures h₁(x)=0, in which case L=f0 and the remaining derivatives extremize f0 along the constraint surface. Noted that ∇L=0 then enforces ∇f₀=0 in the direction parallel to the constraint, whereas perpendicular to the constraint ν₁ represents a "force" that prevents x from leaving the h₁(x)=0 constraint surface.

Generalized to the Lagrangian L(x,λ,ν) of the general optimization problem (the "primal" problem) with both inequality and equality constraints, following chapter 5 of the Boyd and Vandenberghe book (see below) (section 5.1.1).

Described the KKT conditions for a (local) optimum/extremum (Boyd, section 5.5.3). These are true in problems with strong duality, as pointed out by Boyd, but they are actually true in much more general conditions. For example, they hold under the "LICQ" condition in which the gradients of all the active constraints are linearly independent.

**Further reading:** _[Convex Optimization](http://www.stanford.edu/~boyd/cvxbook/)_ by Boyd and Vandenberghe (free book online), chapter 5. There are many sources on [Lagrange multipliers](http://en.wikipedia.org/wiki/Lagrange_multipliers) (the special case of equality constraints) online that can be found by googling.

## Lecture 23 (Apr 5)

* Using duality to solve optimization problems: [Augmented Lagrangian methods](https://en.wikipedia.org/wiki/Augmented_Lagrangian_method) and ADMM

**Further reading:** See the textbook sections III.3–III.4.  These [slides](https://pages.cs.wisc.edu/~swright/nd2016/IMA_augmentedLagrangian.pdf) by Stephen J. Wright at Univ. Wisc. are similar (but more in depth) to the approach from lecture.  This [2011 seminar by Stephen Boyd](http://videolectures.net/nipsworkshops2011_boyd_multipliers/) on ADMM may also be useful, and you can find many other resources online.  Many of these sources cover only equality constraints, but augmented Lagrangians can also be used for inequality constraints, e.g. as described in [Birgin et al. (2007)](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.72.6121).


## Lecture 24 (Apr 7)

* Quick review of augmented Lagrangians and ADMM from last lecture. Indicator function example from section III.4.
* CCSA interior-point algorithm
* [pset 4 solutions](psets/pset4sol.ipynb)
* [pset 5](psets/pset5.ipynb): due 4/21

Went over very different example of a nonlinear optimization scheme, solving a fairly general inequality-constrained nonlinear-programming problem: the CCSA algorithm(s), as described by Svanberg (2002). This is a surprisingly simple algorithm (the [NLopt](http://ab-initio.mit.edu/nlopt) implementation is only 300 lines of C code), but is robust and provably convergent, and illustrates a number of important ideas in optimization: optimizing an approximation to update the parameters **x**, guarding the approximation with trust regions and penalty terms, and optimizing via the dual function (Lagrange multipliers). Like many optimization algorithms, the general ideas are very straightforward, but getting the details right can be delicate!

Outlined the inner/outer iteration structure of CCSA, and the interesting property that it produces a sequence of feasible iterates from a feasible starting point, which means that you can stop it early and still have a feasible solution (which is very useful for many applications where 99% of optimal is fine, but feasibility is essential).  It could be thought of as a type of "interior point" algorithm.

The inner optimization problem involving the approximate gᵢ functions turns out to be *much* easier to solve because it is *convex* and *separable* (gᵢ = a sum of 1d convex functions of each coordinate xⱼ).  Convexity allows us to use **strong duality** to turn the problem into an equivalent "dual" optimization problem, and separability makes this dual problem trivial to formulate and solve.

**Further reading:** Pages 1–10 of [Svanberg (2002) paper on CCSA algorithms](
http://dx.doi.org/10.1137/S1052623499362822) — I used the "linear and separable quadratic approximation" functions gᵢ in section 5.1; as far as I can tell the other example gᵢ functions have no general advantages.
 (I presented a simplified form of CCSA compared to the paper, in which the per-variable scaling/trust parameters σⱼ are omitted.  These can be quite useful in practice, especially if different variables have very different scalings in your problem.)

## Lecture 25 (April 10)

* Compressive sensing (CS) and ℓ¹ regularization (LASSO etc.).
* [Slides](https://www.dropbox.com/s/iplx3gsk42t0xlb/Various-CS-slides.pdf?dl=0) collected from various sources.

**Further reading:** Strang textbook, section III.5.  There are many tutorials and other information on CS/LASSO/etcetera online.  For example, these [Rice Univ. tutorial slides (Cevher, 2019)](https://www.epfl.ch/labs/lions/wp-content/uploads/2019/01/Volkan-CS-IPSN09-tutorial-part-1.pdf) or [Princeton Slides (Cheng, 2014)](https://3dvision.princeton.edu/courses/COS598/2014sp/slides/lecture20_Compressive_Sensing.pdf) are fairly accessible.  For compressed sensing in MRI, see e.g. the slides by [Lustig et al.](https://pages.cs.wisc.edu/~brecht/cs838docs/deshpande.project.pdf) and [Tamir (2019)](http://users.ece.utexas.edu/~jtamir/files/jtamir_compressed_sensing_ismrm19.pdf) and many other sources. A hybrid of ℓ¹ (CS/LASSO) and ℓ² (ridge/Tikhonov) regularization is to use *both*, a combination called [elastic-net regularization](https://en.wikipedia.org/wiki/Elastic_net_regularization); see e.g. slides from [Univ. Iowa (Breheny)](https://myweb.uiowa.edu/pbreheny/7600/s16/notes/3-28.pdf).

## Lecture 26 (April 12)

* Neural networks, ReLU, and classification
* demo: [playground.tensorflow.org](http://playground.tensorflow.org/)

**Further reading:** Strang section VII.1 and [OCW lecture 26](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-26-structure-of-neural-nets-for-deep-learning/).

## Lecture 27 (Apr 14)

* Backpropagation for neural networks.

**Further reading:** Strang section VII.3 and [OCW lecture 27](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-27-backpropagation-find-partial-derivatives/).  You can find many, many articles online about [backpropagation](https://en.wikipedia.org/wiki/Backpropagation) in neural networks.   For generalizing gradients to scalar-valued functions of matrices and other abstract vector spaces, what we need is an inner product; we covered this in more detail in [lecture 4 of *Matrix Calculus* (IAP 2023)](https://github.com/mitmath/matrixcalc#lecture-4-jan-25).   Backpropagation for neural networks is closely related to backpropagation/adjoint methods [for recurrence relations (course notes)](https://math.mit.edu/~stevenj/18.336/recurrence2.pdf), and [on computational graphs (blog post)](https://colah.github.io/posts/2015-08-Backprop/); see also [lecture 8 of *Matrix Calculus* (IAP 2023)](https://github.com/mitmath/matrixcalc#lecture-8-feb-3).

## Lecture 28 (Apr 19)

* Non-negative matrix factorization — guest lecture by [Prof. Ankur Moitra](https://people.csail.mit.edu/moitra/).

**Further reading:** See section 2.1 of Moitra's [*Algorithmic Aspects of Machine Learning*](http://people.csail.mit.edu/moitra/docs/bookexv2.pdf).  An interesting application to image analysis can be found in [this paper](http://www.cs.columbia.edu/~blei/fogm/2020F/readings/LeeSeung1999.pdf).

## Lecture 29 (Apr 21)

* [(Discrete) convolutions](https://en.wikipedia.org/wiki/Convolution#Discrete_convolution), translation-invariance, [circulant matrices](https://en.wikipedia.org/wiki/Circulant_matrix), and convolutional neural networks (CNNs)
* [pset 5 solutions](psets/pset5sol.ipynb)

**Further reading:** Strang textbook sections IV.2 (circulant matrices) and VII.2 (CNNs), and [OCW lecture 32](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-32-imagenet-is-a-cnn-the-convolution-rule/).  See also these [Stanford lecture slides](http://cs231n.stanford.edu/slides/2016/winter1516_lecture7.pdf) and [MIT lecture slides](https://mit6874.github.io/assets/sp2020/slides/L03_CNNs_MK2.pdf).

## Lecture 30 (Apr 24)
* Backpropagation and convolutions: differentiating with respect to convolution coefficients involves a convolution!  via identity uᵀ(a⊛v)=aᵀ(Rv⊛u).
* The [discrete Fourier transform (DFT)](https://en.wikipedia.org/wiki/Discrete_Fourier_transform) and its inverse: [roots of unity](https://en.wikipedia.org/wiki/Root_of_unity), unitarity, diagonalizing convolutions.

**Further reading**: Textbook section IV.1 and VII.2.

## Lecture 31 (Apr 24)
* Proof of the [convolution theorem](https://en.wikipedia.org/wiki/Convolution_theorem): a DFT diagonalizes circular convolutions
* Convolutions y=a⊛x via DFT: DFT a and x, multiply elementwise, then inverse-DFT to obtain y!
* [Fast Fourier transforms (FFTs)](https://en.wikipedia.org/wiki/Fast_Fourier_transform): DFTs (and many related problems) in O(N log N) operations.  Derived the [Cooley–Tukey FFT algorithm](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm) and mentioned a few other algorithms.  See [slides](https://github.com/mitmath/18335/blob/spring21/notes/FFT.pdf).

**Further reading**: Textbook sections IV.1–IV.2 and [OCW lecture 31](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-31-eigenvectors-of-circulant-matrices-fourier-matrix/) and [lecture 32](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-32-imagenet-is-a-cnn-the-convolution-rule/).  The [Wikipedia FFT article](https://en.wikipedia.org/wiki/Fast_Fourier_transform) (partially written by SGJ) was still not bad last I checked. [Gauss and the history of the fast Fourier transform](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.309.181) (1985) is a wonderful article on the historical development of the FFT.  [Duhamel & Vetterli (1990)](https://doi.org/10.1016%2F0165-1684%2890%2990158-U) is a classic review article.  SGJ co-developed a little FFT library called [FFTW](https://www.fftw.org/).

## Lecture 32 (Apr 25)

* [pset 6](psets/pset6.ipynb): due Friday May 5.

Fourier series vs. DFT: If we view the DFT as a [Riemann sum](https://en.wikipedia.org/wiki/Riemann_sum) approximation for a [Fourier series](https://en.wikipedia.org/wiki/Fourier_series) coefficient (which turns out to be *exponentially* accurate for smooth periodic f(t)!), then the errors are an instance of [aliasing](https://en.wikipedia.org/wiki/Aliasing) (see e.g. the ["wagon-wheel" effect](https://en.wikipedia.org/wiki/Wagon-wheel_effect)).  For band-limited signals where we sample at a rate > twice the bandwidth, there is no aliasing and no information loss, a result known as the [Nyquist—Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem); in the common case where the bandwidth is centered at ω=0, this corresponds to sampling at more than *twice* the highest frequency.

**Further reading**: For a periodic function, a Riemann sum is equivalent to a trapezoidal rule (since the 0th and Nth samples are identical), and the exponential convergence to the integral is reviewed by [Trefethen and Weideman (2014)](https://epubs.siam.org/doi/pdf/10.1137/130932132); SGJ gave a [simplified review for IAP (2011)](https://math.mit.edu/~stevenj/trap-iap-2011.pdf). The subject of aliasing, sampling, and signal processing leads to the field of [digital signal processing (DSP)](https://en.wikipedia.org/wiki/Digital_signal_processing), on which there are many books and courses.  A classic textbook is [*Discrete-Time Signal Processing*](https://research.iaun.ac.ir/pd/naghsh/pdfs/UploadFile_2230.pdf) by Oppenheim and Schafer, and there are whole courses at MIT (like 6.3000 and 6.7000) on these topics.

## Lecture 33 (May 1)

* The [DTFT](https://en.wikipedia.org/wiki/Discrete-time_Fourier_transform), [windowing](https://en.wikipedia.org/wiki/Window_function) (e.g. relating DTFT to DFT) and spectral leakage.
* [Filter design](https://en.wikipedia.org/wiki/Filter_design) and [FIR filters](https://en.wikipedia.org/wiki/Finite_impulse_response).

**Further reading**: See the DSP links from lecture 32.

## Lecture 34 (May 3)
* FIR filter design = polynomial fitting.  Windowing & least-squares, or minimax design by [Parks-McClellan](https://en.wikipedia.org/wiki/Parks%E2%80%93McClellan_filter_design_algorithm) and similar.
* Changing variables H(z) = ĥ(ω) for z=exp(iω): the [Z transform](https://en.wikipedia.org/wiki/Z-transform)
* [IIR filters](https://en.wikipedia.org/wiki/Infinite_impulse_response): definition, relation to [rational functions](https://en.wikipedia.org/wiki/Rational_function), first-order IIR filter example, stability.

**Further reading**: See the DSP links from lecture 32.

## Lecture 35 (May 5)

* IIR filter stability: poles zₚ must lie inside the unit circle |zₚ|
* IIR filter design: non-convex and complicated, lots of algorithms and approximations.
* [Kronecker products A⊗B](https://en.wikipedia.org/wiki/Kronecker_product) and ["vectorization" vec(A)](https://en.wikipedia.org/wiki/Vectorization_(mathematics)): expressing "multidimensional linear operations" ([multilinear algebra](https://en.wikipedia.org/wiki/Multilinear_algebra)) as ordinary matrix–vector products.
* [pset 6 solutions](psets/pset6sol.ipynb)

## Lecture 36 (May 6)

* Kronecker products, [Hadamard matrices](https://en.wikipedia.org/wiki/Hadamard_matrix), and the mixed-product property (A⊗B)(C⊗D)=AC⊗BD: Kronecker products of unitary matrices are unitary.
* Kronecker products and the [fast Walsh–Hadamard transform (FWHT)](https://en.wikipedia.org/wiki/Fast_Walsh%E2%80%93Hadamard_transform): fast algorithms (FWHT, FFT, …) as *sparse factorizations* of dense matrices via Kronecker products, and equivalently as mono-to-multi-dimensional mappings.
* [Sylvester equations](https://en.wikipedia.org/wiki/Sylvester_equation) and [Lyapunov equations](https://en.wikipedia.org/wiki/Lyapunov_equation): can be solved as ordinary matrix–vector equations via Kronecker products, but this naively requires Θ(n⁶) operations, whereas exploiting the structure gives Θ(n³).  Kronecker products are often a nice way to *think* about things but *not* to explicitly compute with.

## Lecture 37 (May 10)

* [Graphs](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) and their application to representing how entities are connected — lots of applications, from data mining of social networks or the web, to bioinformatics, to analyzing sparse-matrix algorithms
* Representing graphs via matrices: [incidence matrices E](https://en.wikipedia.org/wiki/Incidence_matrix), [adjacency matrices A](https://en.wikipedia.org/wiki/Adjacency_matrix), and [graph Laplacians L=EᵀE=D-A](https://en.wikipedia.org/wiki/Laplacian_matrix)
* [Graph partitioning](https://en.wikipedia.org/wiki/Graph_partition): spectral partitioning via the [Fiedler vector](https://en.wikipedia.org/wiki/Algebraic_connectivity), corresponding to the **second-smallest** eigenvalue of L

**Further reading:** Textbook sections VI.6–VI.7 and [OCW lecture 35](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/resources/lecture-35-finding-clusters-in-graphs-second-project-handwriting/).  Using incidence matrices to identify cycles and spanning trees in graphs is also covered in 18.06 and in Strang's *Introduction to Linear Algebra* book (5th ed. section 10.1 or 6th ed. section 3.5), as well as in [this interactive Julia notebook](https://github.com/mitmath/1806/blob/1a9ff5c359b79f28c534bf1e1daeadfdc7aee054/notes/Graphs-Networks.ipynb).  A popular software package for graph and mesh partitioning is [METIS](https://github.com/KarypisLab/METIS).  The Google [PageRank algorithm](https://en.wikipedia.org/wiki/PageRank) is another nice application of linear algebra to graphs, in this case to rank web pages by "importance".  Direct methods (e.g. Gaussian elimination) for sparse-matrix problems turn out to be all about analyzing sparsity patterns via graph theory; see e.g. the [book by Timothy Davis](https://epubs.siam.org/doi/book/10.1137/1.9780898718881).

## Lecture 38 (May 15)

* [Floating-point introduction](notes/Floating-Point-Intro.ipynb)

If you want to continue with "numerical computing" in any form — whether it be for data analysis, machine learning, scientific/engineering modeling, or other areas — at some point you will need to learn more about **computational errors**.  The mathematical field that studies **algorithms + approximations** is called [numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis), covered by courses such as [18.335](https://github.com/mitmath/18335) at MIT.

One of the most basic sources of computational error is that **computer arithmetic is generally inexact**, leading to [roundoff errors](https://en.wikipedia.org/wiki/Round-off_error).  The reason for this is simple: computers can only work with numbers having a **finite number of digits**, so they **cannot even store** arbitrary real numbers.  Only a _finite subset_ of the real numbers can be represented using a particular number of "bits", and the question becomes _which subset_ to store, how arithmetic on this subset is defined, and how to analyze the errors compared to theoretical exact arithmetic on real numbers.

In **floating-point** arithmetic, we store both an integer coefficient and an exponent in some base: essentially, scientific notation. This allows large dynamic range and fixed _relative_ accuracy: if fl(x) is the closest floating-point number to any real x, then |fl(x)-x| < ε|x| where ε is the _machine precision_. This makes error analysis much easier and makes algorithms mostly insensitive to overall scaling or units, but has the disadvantage that it requires specialized floating-point hardware to be fast. Nowadays, all general-purpose computers, and even many little computers like your cell phones, have floating-point units.

Went through some simple definitions and examples in Julia (see notebook above), illustrating the basic ideas and a few interesting tidbits.  In particular, we looked at **error accumulation** during long calculations (e.g. summation), as well as examples of [catastrophic cancellation](https://en.wikipedia.org/wiki/Loss_of_significance) and how it can sometimes be avoided by rearranging a calculation.

**Further reading:** [Trefethen & Bau's *Numerical Linear Algebra*](https://people.maths.ox.ac.uk/trefethen/text.html), lecture 13. [What Every Computer Scientist Should Know About Floating Point Arithmetic](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.22.6768) (David Goldberg, ACM 1991). William Kahan, [How Java's floating-point hurts everyone everywhere](http://www.cs.berkeley.edu/~wkahan/JAVAhurt.pdf) (2004): contains a nice discussion of floating-point myths and misconceptions.   A brief but useful summary can be found in [this Julia-focused floating-point overview](https://discourse.julialang.org/t/psa-floating-point-arithmetic/8678) by Prof. John Gibson. Because many programmers never learn how floating-point arithmetic actually works, there are [many common myths](https://github.com/mitmath/18335/blob/spring21/notes/fp-myths.pdf) about its behavior.   (An infamous example is `0.1 + 0.2` giving `0.30000000000000004`, which people are puzzled by so frequently it has led to a web site [https://0.30000000000000004.com/](https://0.30000000000000004.com/)!)
