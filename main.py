# Autor: Juan Esteban Astaiza Fuenmayor
# Profesor: Ana María Tamayo
# Descripción: Este script implementa operaciones de conjuntos (unión, intersección, diferencia, diferencia simétrica, subconjunto y superconjunto)
# y utiliza diagramas de Venn para visualizar los resultados.
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
# Función para calcular la unión de varios conjuntos
def union(*sets):
    result = sets[0].copy()
    for set in sets[1:]:
        for element in set:
            if element not in result:
                result.append(element)
    return result

# Función para calcular la intersección de varios conjuntos
def intersección(*sets):
    result = sets[0].copy()
    for set in sets[1:]:
        temp = []
        for element in result:
            if element in set:
                temp.append(element)
        result = temp
    return result

# Función para calcular la diferencia de varios conjuntos
def diferencia(*sets):
    result = sets[0].copy()
    for set in sets[1:]:
        temp = []
        for element in result:
            if element not in set:
                temp.append(element)
        result = temp
    return result

# Función para calcular la diferencia simétrica de varios conjuntos
def diferencia_simetrica(*sets):
    result = []
    for set in sets:
        for element in set:
            if element not in result:
                result.append(element)
    temp = result.copy()
    for element in temp:
        count = 0
        for set in sets:
            if element in set:
                count += 1
        if count > 1:
            result.remove(element)
    return result

# Función para verificar si un conjunto es subconjunto de otro
def subconjunto(*sets):
    for i in range(len(sets) - 1):
        for element in sets[i]:
            if element not in sets[i+1]:
                return False
    return True

# Función para verificar si un conjunto es superconjunto de otro
def superconjunto(*sets):
    for i in range(len(sets) - 1):
        for element in sets[i+1]:
            if element not in sets[i]:
                return False
    return True

# Librerías de visualización


# Función para visualizar conjuntos con diagramas de Venn
def visualize_sets(setA, setB, setC=None):
    """
    Visualiza los conjuntos usando un diagrama de Venn.
    - Si hay dos conjuntos (setA, setB), se muestra un diagrama de Venn 2.
    - Si hay tres conjuntos (setA, setB, setC), se muestra un diagrama de Venn 3.
    """
    if setC is None:
        venn2([set(setA), set(setB)], set_labels=('Set A', 'Set B'))
    else:
        venn3([set(setA), set(setB), set(setC)], set_labels=('Set A', 'Set B', 'Set C'))
    plt.show()

# Bloque principal
if __name__ == "__main__":
    # Definición de los conjuntos de ejemplo
    setA = [1, 2, 3]
    setB = [4, 5, 6]
    setC = [1, 4, 2]
    setD = [1, 2, 3, 4, 5]

    # Unión de conjuntos
    print(f"Unión: {union(setA, setB, setC)}")
    visualize_sets(setA, setB, setC)  # Visualización de la unión con 3 conjuntos

    # Intersección de conjuntos
    print(f"Intersección: {intersección(setA, setC, setD)}")
    visualize_sets(setA, setC)  # Visualización de la intersección con 2 conjuntos

    # Diferencia de conjuntos
    print(f"Diferencia: {diferencia(setA, setB, setC)}")
    visualize_sets(setA, setB)  # Visualización de la diferencia con 2 conjuntos

    # Diferencia simétrica de conjuntos
    print(f"Diferencia Simétrica: {diferencia_simetrica(setA, setB, setC)}")
    visualize_sets(setA, setB, setC)  # Visualización de la diferencia simétrica con 3 conjuntos

    # Verificación de subconjunto
    print(f"Subconjunto: {subconjunto(setA, setD)}")
    visualize_sets(setA, setD)  # Visualización de subconjunto con 2 conjuntos

    # Verificación de superconjunto
    print(f"Superconjunto: {superconjunto(setD, setA)}")
    visualize_sets(setD, setA)  # Visualización de superconjunto con 2 conjuntos