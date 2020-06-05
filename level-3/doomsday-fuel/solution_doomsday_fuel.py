"""
The first test case for this problem seems pretty straightforward. You can
follow along in your head or on paper and arrive at the answer fairly easily.

But then you hit the second test case. And you probably notice pretty quick
if you were to implement the same solution in your head you end up with what
seems like an infinite loop. So there's probably some math theory behind this
problem.

Depending what you initially search for you might end up here:
    https://en.wikipedia.org/wiki/Stochastic_matrix

And then you'll probably end up here:
    https://en.wikipedia.org/wiki/Markov_chain

Eventually, you might even end up here:
    https://en.wikipedia.org/wiki/Absorbing_Markov_chain

"In the mathematical theory of probability, an absorbing Markov chain is a
Markov chain in which every state can reach an absorbing state. An absorbing
state is a state that, once entered, cannot be left."

Yeah, that sounds about right. You can see the described "terminal" state
matches up with what is defined as an "absorbing" state.

There is a lot of information out there about Markov Chains but there are some
great YouTube videos by patrickJMT:
    https://www.youtube.com/watch?v=qhnFHnLkrfA

Once you understand the overall idea then you can implement your own matrix
operations to achieve the desired result.
"""
from fractions import Fraction, gcd


def solution(m):
    """Find the solution!

    Args:
        m: A list of lists (each containing integers) representing a matrix.

    Returns:
        A list of integers representing exact probabilities of each terminal
        state with the common denominator at the end of the list.
    """
    absorbing_state = []
    transient_state = []

    # Organize into absorbing and transient states and convert to fractions
    for i, row in enumerate(m):
        # Absorbing (aka Terminal)
        if sum(row) == 0:
            absorbing_state.append(i)
        # Transient
        else:
            transient_state.append(i)

    # If there's only one absorbing state then it's 1/1
    if len(absorbing_state) == 1:
        return [1, 1]

    """
    We need to reorder the matrix values like:
            s2 s3 s4 s5  s0 s1
        s2  1  0  0  0   0  0
        s3  0  1  0  0   0  0    absorbing
        s4  0  0  1  0   0  0
        s5  0  0  0  1   0  0

        s0  0  0  0  1   0  1    transient
        s1  0  3  2  0   4  0

    These pieces have the following labels:
            s2 s3 s4 s5  s0 s1
        s2
        s3     I         0
        s4
        s5

        s0     R         Q
        s1
    """
    matrix_q = []
    matrix_r = []
    for i, row in enumerate(m):
        row_q = []
        row_r = []
        row_sum = sum(row)

        if i in transient_state:
            for j, value in enumerate(row):
                if j in absorbing_state:
                    row_r.append(Fraction(value, row_sum))
                else:
                    row_q.append(Fraction(value, row_sum))

        if row_q:
            matrix_q.append(row_q)
        if row_r:
            matrix_r.append(row_r)

    # Create an identity matrix the same size as Q
    matrix_i = create_identity_matrix(len(matrix_q))

    """
    Then we need to find F:
            s2 s3 s4 s5  s0 s1
        s2
        s3     I         0
        s4
        s5

        s0     FR        0
        s1

    Where:
        F = (I-Q)^-1
    """
    # Find (I-Q) via subtraction
    matrix_iq = []
    for i, row in enumerate(matrix_q):
        row_iq = []
        for j, value in enumerate(row):
            row_iq.append(matrix_i[i][j] - matrix_q[i][j])
        matrix_iq.append(row_iq)

    # Find the inverse of the result from (I-Q) subtraction
    matrix_f = create_identity_matrix(len(matrix_iq))
    for i in range(len(matrix_iq)):
        value = Fraction(1, matrix_iq[i][i])
        matrix_iq = inverse_helper_col_multiply(matrix_iq, i, value)
        matrix_f = inverse_helper_col_multiply(matrix_f, i, value)
        for j in range(len(matrix_iq)):
            if i == j:
                continue
            value = -matrix_iq[j][i]
            matrix_iq = inverse_helper_col_row_multiply(matrix_iq, i, j, value)
            matrix_f = inverse_helper_col_row_multiply(matrix_f, i, j, value)

    # Multiply F and R
    matrix_fr = multiply_two_matrices(matrix_f, matrix_r)

    # Find the common denominator from the fractions
    fraction_result = matrix_fr[0]
    denominator = None
    for value in fraction_result:
        if denominator:
            n = denominator * value.denominator
            d = gcd(denominator, value.denominator)
            denominator = n / d
        else:
            denominator = value.denominator

    # Adjust and format the resulting values
    result = []
    for value in fraction_result:
        if value.numerator == 0:
            result.append(0)
        else:
            d = denominator / value.denominator
            result.append(d * value.numerator)

    # Add the denominator at the end
    result.append(denominator)

    return result


def create_identity_matrix(size):
    """Create a square matrix with diagonal 1's (aka identity matrix).

    Args:
        size: The number of rows and columns.

    Returns:
        An identity matrix (list of lists).
    """
    result = []
    for i in range(size):
        result.append([0] * size)
        result[i][i] = Fraction(1)
    return result


def multiply_two_matrices(matrix1, matrix2):
    """Perform matrix multiplication on two matrices.

    Args:
        matrix1: A matrix (list of lists).
        matrix2: A matrix (list of lists).

    Returns:
        A matrix (list of lists) with the resulting values.
    """
    result = []
    for i in range(len(matrix1)):
        result.append([0] * len(matrix2[0]))
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def inverse_helper_col_multiply(matrix, i, value):
    """Helper to multiply matrix with identity matrix having replaced value.

    Args:
        matrix: A matrix (list of lists).
        i: A row and column index.
        value: A value to place at the given row/column.

    Returns:
        A matrix (list of lists).
    """
    matrix_i = create_identity_matrix(len(matrix))
    matrix_i[i][i] = value
    return multiply_two_matrices(matrix_i, matrix)


def inverse_helper_col_row_multiply(matrix, i, j, value):
    """Helper to multiply matrix with identity matrix having replaced value.

    Args:
        matrix: A matrix (list of lists).
        i: A column index.
        j: A row index.
        value: A value to place at the given row/column.

    Returns:
        A matrix (list of lists).
    """
    matrix_i = create_identity_matrix(len(matrix))
    matrix_i[j][i] = value
    return multiply_two_matrices(matrix_i, matrix)
