import joblib
import pandas as pd

model = joblib.load("C:/Users/USER/Downloads/projek_machine_learning_fadli/model/model_prediksi_harga.pkl")

X = pd.DataFrame([[100, 3, 2]], columns=['LuasRumah', 'KamarTidur', 'KamarMandi'])

prediksi = model.predict(X)
print("Hasil prediksi:", prediksi)
