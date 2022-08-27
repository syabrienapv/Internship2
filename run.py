from main import app

if __name__ == "__main__":
    app.run(debug=True)

from main import prediksi_knn

x = prediksi_knn.knn_models(2)
print(x)