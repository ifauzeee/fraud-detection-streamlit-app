# === BAGIAN 1: Impor Library ===
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, confusion_matrix
import joblib
print("✅ Library berhasil diimpor.")

# === BAGIAN 2: Pengumpulan dan Pra-pemrosesan Data ===
try:
    data = pd.read_csv('creditcard.csv')
    print("✅ Dataset 'creditcard.csv' berhasil dimuat.")
except FileNotFoundError:
    print("❌ ERROR: File 'creditcard.csv' tidak ditemukan. Pastikan file ada di folder yang sama dengan skrip ini.")
    exit()

# Normalisasi kolom 'Amount' dan 'Time'
scaler = StandardScaler()
data['NormalizedAmount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
data['NormalizedTime'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))
data = data.drop(['Time', 'Amount'], axis=1)

# Pisahkan fitur (X) dan target (y)
X = data.drop(['Class'], axis=1)
y = data['Class']

# Bagi data menjadi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print("✅ Pra-pemrosesan dan pembagian data selesai.")

# === BAGIAN 3: Pelatihan dan Evaluasi Model ===
print("\nMemulai proses pelatihan model...")

# Atasi ketidakseimbangan data dengan SMOTE
print("Mengaplikasikan SMOTE pada data latih...")
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
print("SMOTE selesai.")

# Latih model Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
print("Melatih model Random Forest...")
model.fit(X_train_resampled, y_train_resampled)
print("✅ Model berhasil dilatih.")

# Evaluasi model
print("\nMengevaluasi model pada data uji...")
y_pred = model.predict(X_test)

print("\nLaporan Klasifikasi:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Simpan model yang sudah dilatih
joblib.dump(model, 'fraud_detection_model.pkl')
print("\n✅ Model berhasil disimpan sebagai 'fraud_detection_model.pkl'.")