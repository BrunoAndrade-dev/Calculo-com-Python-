import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da Barra
L = 2.0      # Comprimento barra
EA = 1.0     # Rigidez Axial (E * A). Assumimos 1 para simplificar.

# Condição de Contorno 
P = 10.0     # (último nó)
N_ELEM = 2
N_NODES = N_ELEM + 1

print(f"Resolvendo a barra com {N_ELEM} elementos ({N_NODES} nós).\n")
# Coordenadas dos Nós
# Gera n_nodes igualmente espaçados entre 0 e L
node_coordinates = np.linspace(0, L, N_NODES)
print("Coordenadas dos Nós (x_i):", node_coordinates)

h = L / N_ELEM #Compirmento de cada elemento
print(f"Comprimento de cada elemento (h): {h}\n")

# Mapeamento de Elementos para Nós 
# Lista de pares de nós que definem cada elemento
connectivity = [(i, i + 1) for i in range(N_ELEM)]
# Inicialização da Matriz de Rigidez Global (K) e do Vetor de Força (F)
K_global = np.zeros((N_NODES, N_NODES))
F_global = np.zeros(N_NODES)

# Aplicamos a força P no último nó (índice N_NODES - 1)
F_global[N_NODES - 1] = P

#Montagem
for elem_index in range(N_ELEM):

    K_local = (EA / h) * np.array([[ 1, -1], [-1,  1]])
    node1_global_idx = connectivity[elem_index][0]
    node2_global_idx = connectivity[elem_index][1]
    K_global[node1_global_idx:node2_global_idx+1, node1_global_idx:node2_global_idx+1] += K_local

print("Matriz de Rigidez Global [K]:")
print(K_global)
print("\nVetor de Força Global {F}:")
print(F_global)

fixed_node_index = 0
fixed_displacement = 0.0

# Resolvendo pelo método de eliminação
unknown_dofs = np.delete(np.arange(N_NODES), fixed_node_index)

# Matriz de Rigidez Reduzida [K_red]
K_red = K_global[np.ix_(unknown_dofs, unknown_dofs)]

# Vetor de Força Reduzido {F_red}
F_red = F_global[unknown_dofs]

print("\n--- Sistema Reduzido após BC (Eliminação) ---")
print("Matriz [K_red]:")
print(K_red)
print("\nVetor {F_red}:")
print(F_red)


# Solução do Sistema
U_red = np.linalg.solve(K_red, F_red)
U_global = np.zeros(N_NODES)
U_global[fixed_node_index] = fixed_displacement # U_1 = 0
U_global[unknown_dofs] = U_red

print("\n--- Solução do Sistema ---")
print("Deslocamentos Nodais {U}:")
print(U_global)

x_plot = []
u_plot = []

for e in range(N_ELEM):
    # Coordenadas do elemento
    x_e = node_coordinates[e:e+2]
    # Deslocamentos nodais do elemento
    u_e = U_global[e:e+2]
    
    # Interpolação linear: adiciona os pontos inicial e final do elemento
    x_plot.extend(x_e)
    u_plot.extend(u_e)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, u_plot, 'b-', label='Deslocamento (u(x))')
plt.plot(node_coordinates, U_global, 'ro', label='Deslocamentos Nodais (U_i)')
plt.title(f'Deslocamento da Barra 1D (MEF com {N_ELEM} Elementos)')
plt.xlabel('Posição $x$')
plt.ylabel('Deslocamento $u(x)$')
plt.grid(True, linestyle='--')
plt.legend()
plt.show()

# Resposta Final do problema
# Para n_elem=2, o deslocamento máximo em x=L é U_3 = 20.0
# Se n_elem=3, o deslocamento máximo seria U_4 = 20.0 (o resultado é convergente e exato neste caso).
print(f"\nDeslocamento máximo na extremidade livre (x={L}): U_max = {U_global[-1]:.2f}")