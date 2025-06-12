import matplotlib.pyplot as plt
import pandas as pd

# Supón que tienes una lista de dicts con los resultados
# results = [{'Algoritmo': 'GA_V1', 'Combinacion': 'archivo_1_visual', 'Alumno': 'Juan', '%Nivel1': 50, ...}, ...]

df = pd.DataFrame(results)

# Agrupa por algoritmo y combinación, promediando los porcentajes
df_grouped = df.groupby(['Algoritmo', 'Combinacion']).mean(numeric_only=True).reset_index()

for algoritmo in df_grouped['Algoritmo'].unique():
    df_alg = df_grouped[df_grouped['Algoritmo'] == algoritmo]
    df_alg.set_index('Combinacion')[['%Nivel1', '%Nivel2', '%Nivel3']].plot(
        kind='bar', stacked=True, figsize=(12,6)
    )
    plt.title(f'Porcentaje de materiales asignados por nivel - {algoritmo}')
    plt.ylabel('% de materiales')
    plt.xlabel('Combinación')
    plt.legend(title='Nivel')
    plt.tight_layout()
    plt.show()

    df_alg.set_index('Combinacion')[['%Video', '%PDF', '%Audio', '%Presentación']].plot(
        kind='bar', stacked=True, figsize=(12,6)
    )
    plt.title(f'Porcentaje de materiales asignados por tipo - {algoritmo}')
    plt.ylabel('% de materiales')
    plt.xlabel('Combinación')
    plt.legend(title='Tipo')
    plt.tight_layout()
    plt.show()