import pandas as pd

clientes = pd.read_csv("data/clientes.csv")

print ("# 1. Estructura del archivo")
print(f"Dimensiones: {clientes.shape[0]} filas × {clientes.shape[1]} columnas")
print()
print("Primeras filas:")
print(clientes.to_string(index=False))
print()

print ("# 2. Tipos inferidos (dtype) — la pista que da el lenguaje")
print("Tipos inferidos (dtype):")
print(clientes.dtypes)
print()

print("# 3. Valores únicos — ¿cuántas categorías hay y cuáles son?") 

print("Valores únicos por columna:")
for columna in clientes.columns:
    unicos = clientes[columna].unique()
    print(f"- {columna} ({len(unicos)} únicos): {list(unicos)}")
print()

print("# 4. Declarar el orden de las variables ordinales")

cat_educacion = pd.CategoricalDtype(
    categories=['Primaria', 'Secundaria', 'Universidad', 'Posgrado'], 
    ordered=True
)
clientes['nivel_educacion'] = clientes['nivel_educacion'].astype(cat_educacion)
print(f"Comprobación nivel_educacion min (debe ser Primaria): {clientes['nivel_educacion'].min()}")

# Declaramos el orden jerárquico para satisfaccion (escala 1 a 5)
cat_satisfaccion = pd.CategoricalDtype(
    categories=[1, 2, 3, 4, 5], 
    ordered=True
)
clientes['satisfaccion'] = clientes['satisfaccion'].astype(cat_satisfaccion)
print(f"Comprobación satisfaccion min: {clientes['satisfaccion'].min()}")

# Prueba de control de errores (Typo / Valores faltantes)
# Si escribiéramos mal "Postgrado" con 't', pandas generaría valores NaN que podemos contar con .isna().sum()
print(f"Valores faltantes (NaN) tras coerción: {clientes[['nivel_educacion', 'satisfaccion']].isna().sum().to_dict()}")
print()


print("# 5. Resumen de la clasificación (para el informe)")

clasificacion = {
    "cliente_id": "Cualitativa Nominal",
    "edad": "Cuantitativa de Razón",
    "numero_hijos": "Cuantitativa de Razón (Discreta)",
    "genero": "Cualitativa Nominal",
    "nivel_educacion": "Cualitativa Ordinal",
    "ciudad": "Cualitativa Nominal",
    "ingresos_mensuales": "Cuantitativa de Razón",
    "satisfaccion": "Cualitativa Ordinal",
}

print("Resumen de la clasificación (para el informe):")
for variable, tipo in clasificacion.items():
    print(f"  {variable:20s} {tipo}")
