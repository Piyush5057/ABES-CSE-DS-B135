import numpy as np
def get_matrix(prompt):
    print(f"\nEnter values for {prompt}:(comma seperated rows,space seperated elements)")
    rows=input().strip().strip(',')
    matrix=[list(map(float,row.strip().split())) for row in rows]
    return np.array(matrix)

def main():
    A=get_matrix("Matrix A")
    B=get_matrix("Matrix B")

    print("\nMatrix A:\n", A)
    print("Matrix B:\n", B)

    # Addition
    try:
        print("\nAddition:\n", A + B)
    except ValueError:
        print("Addition failed: Matrices must be the same shape.")

    #subtraction
    try:
        print("\nSubtraction:\n",A-B)
    except ValueError:
        print("Subtraction failed: Matrices must be the same shape.")
    
    #Multiplicatiion
    try:
        print("\nMultiplication:\n",np.dot(A,B))
    except ValueError:
        print("Multiplication failed: Matrices must be the same shape.")
    
    # Transpose
    print("\nTranspose of A:\n", A.T)
    print("Transpose of B:\n", B.T)

    # Inverse
    try:
        print("\nInverse of A:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("Inverse of A failed: Matrix is singular or not square.")

    try:
        print("\nInverse of B:\n", np.linalg.inv(B))
    except np.linalg.LinAlgError:
        print("Inverse of B failed: Matrix is singular or not square.")

    # Element-wise division
    try:
        print("\nElement-wise Division (A / B):\n", np.divide(A, B))
    except ValueError:
        print("Division failed: Matrices must be the same shape.")

if __name__ == "__main__":
    main()