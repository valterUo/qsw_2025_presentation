import numpy as np
import matplotlib.pyplot as plt
import pennylane as qml

def visualize_density_matrix(density_matrix, n_qubits):
    
    rho = density_matrix.data if hasattr(density_matrix, 'data') else density_matrix
    
    # Generate state labels
    states = [format(i, f'0{n_qubits}b') for i in range(2**n_qubits)]
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 16))
    
    # Real part
    im1 = ax1.imshow(np.real(rho), cmap='RdBu_r', vmin=-np.max(np.abs(rho)), vmax=np.max(np.abs(rho)))
    ax1.set_title('Real Part', fontsize=14)
    ax1.set_xticks(range(len(states)))
    ax1.set_yticks(range(len(states)))
    ax1.set_xticklabels(states, rotation=45, ha='right')
    ax1.set_yticklabels(states)
    plt.colorbar(im1, ax=ax1)
    
    # Imaginary part
    im2 = ax2.imshow(np.imag(rho), cmap='RdBu_r', vmin=-np.max(np.abs(rho)), vmax=np.max(np.abs(rho)))
    ax2.set_title('Imaginary Part', fontsize=14)
    ax2.set_xticks(range(len(states)))
    ax2.set_yticks(range(len(states)))
    ax2.set_xticklabels(states, rotation=45, ha='right')
    ax2.set_yticklabels(states)
    plt.colorbar(im2, ax=ax2)
    
    # Absolute value
    im3 = ax3.imshow(np.abs(rho), cmap='viridis', vmin=0, vmax=np.max(np.abs(rho)))
    ax3.set_title('Absolute Value', fontsize=14)
    ax3.set_xticks(range(len(states)))
    ax3.set_yticks(range(len(states)))
    ax3.set_xticklabels(states, rotation=45, ha='right')
    ax3.set_yticklabels(states)
    plt.colorbar(im3, ax=ax3)
    
    # Diagonal elements (populations)
    diagonal = np.diag(rho).real
    ax4.bar(range(len(diagonal)), diagonal)
    ax4.set_title('Diagonal Elements (Populations)', fontsize=14)
    ax4.set_xlabel('State')
    ax4.set_ylabel('Population')
    ax4.set_xticks(range(len(states)))
    ax4.set_xticklabels(states, rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()

def controlled_circuit1(target_qubits, coeff = 2.0):
    #qml.RZ(coeff, wires=target_qubits[0])
    qml.PauliZ(wires=target_qubits[0])


def controlled_circuit2(coeff = 1.0):
    # (0.5) [I0 I1 Z2]
    qml.RZ(coeff, wires=8)
    #qml.S(wires=8)
    
    # (0.5) [I0 Z1 Z2]
    qml.CNOT(wires=[8, 7])
    qml.RZ(coeff, wires=7)
    #qml.S(wires=7)
    qml.CNOT(wires=[8, 7])
    
    # (0.5) [Z0 I1 Z2]
    qml.CNOT(wires=[8, 6])
    qml.RZ(coeff, wires=6)
    #qml.S(wires=6)
    qml.CNOT(wires=[8, 6])
    
    # (-0.5) [Z0 Z1 Z2]
    qml.CNOT(wires=[8, 7])
    qml.CNOT(wires=[7, 6])
    qml.RZ(-coeff, wires=6)
    qml.CNOT(wires=[7, 6])
    qml.CNOT(wires=[8, 7])
    
    

def controlled_circuit3(coeff = 1.0):
    qml.Hadamard(wires=6)
    qml.Hadamard(wires=8)
    
    qml.RZ(coeff, wires=6)
    #qml.S(wires=6)
    
    qml.CNOT(wires=[8, 6])
    qml.RZ(coeff, wires=6)
    #qml.S(wires=6)
    qml.CNOT(wires=[8, 6])
    
    qml.CNOT(wires=[7, 6])
    qml.RZ(coeff, wires=6)
    #qml.S(wires=6)
    qml.CNOT(wires=[7, 6])
    
    qml.CNOT(wires=[8, 7])
    qml.CNOT(wires=[7, 6])
    qml.RZ(-coeff, wires=6)
    qml.CNOT(wires=[7, 6])
    qml.CNOT(wires=[8, 7])
    
    qml.Hadamard(wires=6)
    qml.Hadamard(wires=8)
    
def controlled_circuit4(coeff = 1.0):
    qml.Hadamard(wires=7)
    qml.Hadamard(wires=8)
    
    qml.RZ(coeff, wires=7)
    #qml.S(wires=7)
    
    qml.CNOT(wires=[8, 7])
    qml.RZ(coeff, wires=7)
    #qml.S(wires=7)
    qml.CNOT(wires=[8, 7])
    
    qml.CNOT(wires=[7, 6])
    qml.RZ(coeff, wires=6)
    #qml.S(wires=6)
    qml.CNOT(wires=[7, 6])
    
    qml.CNOT(wires=[8, 7])
    qml.CNOT(wires=[7, 6])
    qml.RZ(-coeff, wires=6)
    qml.CNOT(wires=[7, 6])
    qml.CNOT(wires=[8, 7])
    
    qml.Hadamard(wires=7)
    qml.Hadamard(wires=8)
    
def controlled_circuit5(coeff = 2.0):
    qml.Hadamard(wires=8)
    qml.RZ(coeff, wires=8)
    #qml.PauliZ(wires=8)
    qml.Hadamard(wires=8)