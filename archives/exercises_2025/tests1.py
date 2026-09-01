from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime.fake_provider import FakeYorktownV2
import numpy as np

def test_xor(XOR):
    # Test XOR gate outputs using assert statements
    expected_outputs = {
        ('0', '0'): '0',
        ('0', '1'): '1',
        ('1', '0'): '1',
        ('1', '1'): '0'
    }
    for inp1 in ['0', '1']:
        for inp2 in ['0', '1']:
            _, output = XOR(inp1, inp2)
            assert output == expected_outputs[(inp1, inp2)], f"❌ XOR({inp1}, {inp2}) = {output}, expected {expected_outputs[(inp1, inp2)]}"
    print("✅ All XOR gate tests passed.")

def test_and(AND):
    # Test AND gate outputs using assert statements
    expected_outputs = {
        ('0', '0'): '0',
        ('0', '1'): '0',
        ('1', '0'): '0',
        ('1', '1'): '1'
    }
    for inp1 in ['0', '1']:
        for inp2 in ['0', '1']:
            _, output = AND(inp1, inp2)
            assert output == expected_outputs[(inp1, inp2)], f"❌ AND({inp1}, {inp2}) = {output}, expected {expected_outputs[(inp1, inp2)]}"
    print("✅ All AND gate tests passed.")

def test_nand(NAND):
    # Test NAND gate outputs using assert statements
    expected_outputs = {
        ('0', '0'): '1',
        ('0', '1'): '1',
        ('1', '0'): '1',
        ('1', '1'): '0'
    }
    for inp1 in ['0', '1']:
        for inp2 in ['0', '1']:
            _, output = NAND(inp1, inp2)
            assert output == expected_outputs[(inp1, inp2)], f"❌ NAND({inp1}, {inp2}) = {output}, expected {expected_outputs[(inp1, inp2)]}"
    print("✅ All NAND gate tests passed.")


def test_or(OR):
    # Test OR gate outputs using assert statements
    expected_outputs = {
        ('0', '0'): '0',
        ('0', '1'): '1',
        ('1', '0'): '1',
        ('1', '1'): '1'
    }
    for inp1 in ['0', '1']:
        for inp2 in ['0', '1']:
            _, output = OR(inp1, inp2)
            assert output == expected_outputs[(inp1, inp2)], f"❌ OR({inp1}, {inp2}) = {output}, expected {expected_outputs[(inp1, inp2)]}"
    print("✅ All OR gate tests passed.")

def test_compilation(layout):

    backend = FakeYorktownV2()

    def AND(inp1, inp2, backend, layout):
        
        qc = QuantumCircuit(3, 1) 
        qc.reset(range(3))
        
        if inp1=='1':
            qc.x(0)
        if inp2=='1':
            qc.x(1)
            
        qc.barrier()
        qc.ccx(0, 1, 2) 
        qc.barrier()
        qc.measure(2, 0) 
    
        qc_trans = transpile(qc, backend, initial_layout=layout, optimization_level=3)
        
        return qc_trans
    
    for input1 in ['0','1']:
        for input2 in ['0','1']:
            qc_trans1 = AND(input1, input2, backend, layout)
            num_gates = qc_trans1.num_nonlocal_gates()
                    
            print('For input '+input1+input2)
            assert num_gates==6, f"❌ Toffoli transpiled to {num_gates} two qubit gates rather than 6."
    print("✅ Ideal transpilation acheived.")

def test_alt(
        find_orthogonal_state,
        find_mutually_unbiased_basis_plus,
        find_mutually_unbiased_basis_minus
):
    ket_0 = np.array([[1], [0]], dtype=complex)
    ket_1 = np.array([[0], [1]], dtype=complex)

    # (a) Test for orthogonality
    theta = np.pi / 4
    ket_zero_bar = np.cos(theta) * ket_0 + np.sin(theta) * ket_1
    ket_one_bar = find_orthogonal_state(ket_zero_bar, theta)

    # Check if the inner product is close to zero
    inner_product_orthogonal = np.vdot(ket_zero_bar, ket_one_bar)
    assert np.isclose(inner_product_orthogonal, 0), "❌ Test (a) failed: The states |ψ0⟩ and |ψ1⟩ are not orthogonal."
    print("✅ Test (a) passed: |ψ0⟩ and |ψ1⟩ are orthogonal.")

    # (b) Test for mutually unbiased bases
    ket_plus_bar = find_mutually_unbiased_basis_plus(ket_zero_bar, ket_one_bar)
    ket_minus_bar = find_mutually_unbiased_basis_minus(ket_zero_bar, ket_one_bar)

    # Check orthogonality of the MUB states
    inner_product_mub = np.vdot(ket_plus_bar, ket_minus_bar)
    assert np.isclose(inner_product_mub, 0), "❌ Test (b) failed: The states |ψ+⟩ and |ψ-⟩ are not orthogonal."

    # Check the unbiased condition
    inner_product_plus_zero = np.abs(np.vdot(ket_plus_bar, ket_zero_bar))**2
    inner_product_plus_one = np.abs(np.vdot(ket_plus_bar, ket_one_bar))**2
    inner_product_minus_zero = np.abs(np.vdot(ket_minus_bar, ket_zero_bar))**2
    inner_product_minus_one = np.abs(np.vdot(ket_minus_bar, ket_one_bar))**2

    assert np.isclose(inner_product_plus_zero, 0.5), "❌ Test (b) failed: The bases are not mutually unbiased for |<ψ+|ψ0>|^2."
    assert np.isclose(inner_product_plus_one, 0.5), "❌ Test (b) failed: The bases are not mutually unbiased for |<ψ+|ψ1>|^2."
    assert np.isclose(inner_product_minus_zero, 0.5), "❌ Test (b) failed: The bases are not mutually unbiased for |<ψ-|ψ0>|^2."
    assert np.isclose(inner_product_minus_one, 0.5), "❌ Test (b) failed: The bases are not mutually unbiased for |<ψ-|ψ1>|^2."

    print("✅ Test (b) passed: The bases are mutually unbiased.")

    print("\nCongratulations! All tests passed!")

def test_paulis(
        I,
        X,
        Y,
        Z,
        test_square_to_identity,
        test_anticommutation,
        test_product_relation,
        get_eigenvalues_and_eigenvectors,
        ):
    
    I = np.array([
        [1, 0],
        [0, 1]
        ])  # Identity matrix

    paulis = {'X': X, 'Y': Y, 'Z': Z, 'I':I}
    assert all(p is not None for p in [X, Y, Z, I]), "❌ FAIL: At least one matrix is not defined."

    # (a)
    for i in paulis:
        assert np.allclose(test_square_to_identity(paulis[i]) , I), "❌ FAIL (a): Your function did not correctly verify that all Pauli matrices square to the identity."
    print("✅ PASS (a): Your function `test_square_to_identity` works correctly.")

    # (b)
    for i in ['X', 'Y', 'Z']:
        for j in ['X', 'Y', 'Z']:
            if i!=j:
                assert np.allclose(paulis[i]@paulis[j],test_anticommutation(paulis[i],paulis[j])), "❌ FAIL (b): Your function did not correctly verify the anticommutation relations."
    print("✅ PASS (b): Your function `test_anticommutation` works correctly.")

    # (c)
    assert np.allclose(np.array(test_product_relation()), np.array([X@Y,Y@Z,Z@X])), "❌ FAIL (c): Your function did not correctly verify the Pauli product relations."
    print("✅ PASS (c): Your function `test_product_relation` works correctly.")

    # (d)
    eigenvalues, eigenvectors = get_eigenvalues_and_eigenvectors()
    assert isinstance(eigenvalues, dict) and isinstance(eigenvectors, dict), "❌ FAIL (d): Function must return two dictionaries."
    assert all(k in eigenvalues for k in ['X', 'Y', 'Z']), "❌ FAIL (d): Eigenvalues dictionary is missing keys."
    assert all(k in eigenvectors for k in ['X', 'Y', 'Z']), "❌ FAIL (d): Eigenvectors dictionary is missing keys."

    print("✅ PASS (d): Your function `get_eigenvalues_and_eigenvectors` has the correct return type and keys.")

    for name in ['X', 'Y', 'Z']:
        # Check eigenvalues
        e_vals = eigenvalues[name]
        assert np.allclose(sorted(np.real(e_vals)), [-1, 1]), f"❌ FAIL (d): Eigenvalues for {name} are incorrect. Expected [-1, 1]."
        
        # Check eigenvector equation: P * v = lambda * v
        p_matrix = paulis[name]
        e_vecs = eigenvectors[name]
        for i in range(len(e_vals)):
            lambda_val = e_vals[i]
            v_vec = e_vecs[:, i].reshape(2, 1)
            assert np.allclose(p_matrix @ v_vec, lambda_val * v_vec), f"❌ FAIL (d): Eigenvector equation Pv=λv does not hold for {name}."

    print("✅ PASS (d): Eigenvalues and eigenvectors are correct for all Pauli matrices.")

    print("\nCongratulations! All tests passed!")

def test_hadamard(
        H,
        get_hadamard_eigen_system,
        test_hadamard_squares_to_identity,
        test_hadamard_pauli_transformation
):

    print("--- Running Verification ---")

    I = np.array([
    [1, 0],
    [0, 1]
    ])  

    # Check that matrices are defined before proceeding
    assert H is not None, "❌ FAIL: H matrix is not defined."

    # (a)
    eigen_system = get_hadamard_eigen_system()
    assert isinstance(eigen_system, tuple) and len(eigen_system) == 2, "❌ FAIL (a): Function must return a tuple of (eigenvalues, eigenvectors)."
    eigenvalues, eigenvectors = eigen_system

    # Check eigenvalues are correct (+1 and -1)
    assert np.allclose(sorted(np.real(eigenvalues)), [-1, 1]), f"❌ FAIL (a): Eigenvalues for H are incorrect. Expected [-1, 1]."

    # Check eigenvector equation H * v = lambda * v
    for i in range(len(eigenvalues)):
        lambda_val = eigenvalues[i]
        v_vec = eigenvectors[:, i].reshape(2, 1)
        assert np.allclose(H @ v_vec, lambda_val * v_vec), f"❌ FAIL (a): Eigenvector equation Hv=λv does not hold."

    print("✅ PASS (a): Your function `get_hadamard_eigen_system` works correctly.")

    # (b)
    assert np.allclose(test_hadamard_squares_to_identity() , I), "❌ FAIL (b): Your function did not correctly verify that H^2 = I."
    print("✅ PASS (b): Your function `test_hadamard_squares_to_identity` works correctly.")
    answers = ["Z", "-Y", "X"]
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    I = np.array([[1,0],[0,1]])
    Z = np.array([[1,0],[0,-1]])

    # (c)
    things =        [ '1. H X H†',
        '2. H Y H†',
        '3. H Z H†']

    for i,val in enumerate(test_hadamard_pauli_transformation()):
        assert val == answers[i], f"❌ FAIL (c): Your function did not correctly verify the Hadamard-Pauli transformation {things[i]}."
    print("✅ PASS (c): Your answers are correct.")


    print("\nCongratulations! All tests passed!")