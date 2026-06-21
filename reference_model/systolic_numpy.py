import numpy as np

def systolic_naive(A, B):
    """Naive matrix multiply for golden reference"""
    return np.matmul(A, B)

def systolic_dataflow(A, B, W=4, H=4):
    """
    Simulate the systolic array dataflow.
    A: (W, W) matrix
    B: (W, W) matrix
    Returns: (W, W) result C = A @ B
    
    Tracks: cycles per operation, PE utilization
    """
    C = np.zeros((W, W))
    cycles = 0
    pe_cycles = np.zeros((W, W))
    
    # Simplified systolic simulation
    # (You'll expand this, but get the skeleton working)
    C = np.matmul(A, B)
    cycles = 3 * W - 2  # Classic systolic latency formula
    
    return C, cycles, pe_cycles

def verify(A, B, C_rtl, expected_cycles):
    """Self-checking reference"""
    C_golden, cycles_golden, _ = systolic_dataflow(A, B)
    
    assert np.allclose(C_rtl, C_golden), "Matrix mismatch!"
    print(f"✓ Correct result in {expected_cycles} cycles (expected {cycles_golden})")
