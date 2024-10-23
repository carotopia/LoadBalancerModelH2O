from flask import Flask, request, jsonify
import h2o
import json
import pandas as pd

app = Flask(__name__)

# Inicializa H2O
h2o.init()

# Cargar el modelo de H2O que ya has entrenado y guardado
h2o_model = h2o.load_model('/Users/carolinalara/PycharmProjects/LoadBalancer/models/GBM_model_python_1729125548374_1')

# Lista de columnas esperadas (renombradas para cumplir con las reglas de H2O)
expected_columns = ["Flow_Duration", "Total_Fwd_Packets", "Fwd_Packet_Length_Mean", "Flow_Bytes_per_s"]


# Función para realizar la predicción utilizando el modelo de H2O
def predict_with_h2o(packet_data):
    # Ajustar los nombres de las columnas para que coincidan con los del modelo entrenado
    processed_data = {
        "Flow Duration": [packet_data.get("Flow Duration", 0)],
        "Total Fwd Packets": [packet_data.get("Total Fwd Packets", 0)],
        "Fwd Packet Length Mean": [packet_data.get("Fwd Packet Length Mean", 0)],
        "Flow Bytes/s": [packet_data.get("Flow Bytes/s", 0)]
    }

    # Crear un DataFrame de Pandas a partir de los datos procesados
    processed_data_df = pd.DataFrame.from_dict(processed_data)

    # Convertir los datos del paquete en un H2OFrame
    h2o_frame = h2o.H2OFrame(processed_data_df)

    # Imprimir las columnas del H2OFrame para verificar si están correctas
    print(f"Columnas en el H2OFrame: {h2o_frame.columns}")

    # Realizar la predicción
    try:
        prediction = h2o_model.predict(h2o_frame)
    except Exception as e:
        print(f"Error al predecir: {e}")
        raise e

    # Extraer el valor de la predicción

    result = prediction.as_data_frame(use_pandas=True, use_multi_thread=True)
    result_to_dict = pd.DataFrame.to_dict(result)

    return result_to_dict


# Ruta de la API para realizar predicciones
@app.route('/predict', methods=['POST'])
def predict_route():
    # Recibir los datos del paquete desde el cuerpo de la solicitud (en formato JSON)
    packet_data = request.json
    print(packet_data)

    if not packet_data:
        return jsonify({'error': 'Se necesitan los datos del paquete'}), 400

    # Imprimir los datos que recibimos para ver si están correctos
    print(f"Datos recibidos: {packet_data}")

    # Llamar a la función de predicción
    try:
        score = predict_with_h2o(packet_data)
        print(score)
        return jsonify({'score': score})
    except Exception as e:
        print(f"Error en la predicción: {e}")
        return jsonify({'error': str(e)}), 500


# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
