import h2o
from h2o.estimators import H2ORandomForestEstimator

# Iniciar H2O
h2o.init()

# Cargar el archivo de datos
df_h2o = h2o.import_file('Friday-WorkingHours-Afternoon-DDos_cleaned.csv')

# Definir las columnas (features) y la columna objetivo (Label)
x = df_h2o.columns
y = 'Label'

# Verifica que 'Label' esté en la lista de columnas antes de removerla
if y in x:
    x.remove(y)
else:
    print(f"La columna objetivo '{y}' no está presente en el conjunto de datos.")

# Asegurarse de que las características importantes estén en el conjunto de datos
important_features = ["Flow Duration", "Total Fwd Packets", "Fwd Packet Length Mean", "Flow Bytes/s"]
df_h2o[y] = df_h2o[y].asfactor()

# Divide los datos en conjuntos de entrenamiento y prueba
train, test = df_h2o.split_frame(ratios=[0.8], seed=1234)

# Entrenar un modelo de Random Forest solo con las características más importantes
model = H2ORandomForestEstimator(ntrees=50, max_depth=20, seed=1234)
model.train(x=important_features, y=y, training_frame=train)

# Mostrar la importancia de las características
print("Feature Importance:")
print(model.varimp(use_pandas=True))

# Guardar el modelo entrenado
model_path = h2o.save_model(model=model, path="/Users/carolinalara/PycharmProjects/LoadBalancer/models", force=True)
print("Model saved to:", model_path)

# Cerrar la sesión de H2O
h2o.cluster().shutdown()
