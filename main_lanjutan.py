# === BAGIAN 1: Impor Library Lengkap ===
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, confusion_matrix
import warnings

# Mengabaikan warning untuk tampilan output yang lebih bersih
warnings.filterwarnings('ignore')
print("✅ Library berhasil diimpor.")

# === BAGIAN 2: Pengumpulan dan Pra-pemrosesan Data (Sama seperti sebelumnya) ===
try:
    data = pd.read_csv('creditcard.csv')
    print("✅ Dataset 'creditcard.csv' berhasil dimuat.")
except FileNotFoundError:
    print("❌ ERROR: File 'creditcard.csv' tidak ditemukan.")
    exit()

# Normalisasi
scaler = StandardScaler()
data['NormalizedAmount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
data['NormalizedTime'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))
data = data.drop(['Time', 'Amount'], axis=1)

# Pemisahan data
X = data.drop(['Class'], axis=1)
y = data['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
print("✅ Pra-pemrosesan dan pembagian data selesai.")

# Terapkan SMOTE pada data latih
print("Mengaplikasikan SMOTE pada data latih...")
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
print("SMOTE selesai.")

# === BAGIAN 3: Peningkatan Model - Perbandingan, Tuning, dan Validasi ===

# 1. Definisikan model-model yang akan diuji
models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
}

# 2. Definisikan parameter grid untuk tuning (hanya untuk model kompleks)
# Catatan: Grid ini dibuat kecil agar proses tidak terlalu lama.
# Dalam proyek nyata, Anda bisa menambahkan lebih banyak pilihan parameter.
params = {
    "Random Forest": {
        'n_estimators': [100, 150],
        'max_depth': [8, 12],
    },
    "XGBoost": {
        'n_estimators': [100, 150],
        'max_depth': [5, 7],
        'learning_rate': [0.1, 0.2]
    }
}

# 3. Siapkan strategi Validasi Silang (Cross-Validation)
# StratifiedKFold penting untuk data tidak seimbang
skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

# 4. Iterasi, latih, dan evaluasi setiap model
best_models = {}

for name, model in models.items():
    print(f"\n{'='*30}")
    print(f"Memproses Model: {name}")
    print(f"{'='*30}")
    
    # Jika model ada di dalam parameter grid, lakukan GridSearchCV
    if name in params:
        # GridSearchCV akan secara otomatis melakukan cross-validation
        # Scoring='recall' karena kita ingin memaksimalkan deteksi penipuan (kelas 1)
        grid_search = GridSearchCV(model, params[name], cv=skf, scoring='recall', n_jobs=-1, verbose=1)
        print("Memulai Hyperparameter Tuning dengan GridSearchCV...")
        grid_search.fit(X_train_resampled, y_train_resampled)
        
        print(f"\nParameter terbaik ditemukan untuk {name}: {grid_search.best_params_}")
        best_estimator = grid_search.best_estimator_
    else:
        # Untuk model sederhana seperti Logistic Regression, latih langsung
        print("Melatih model...")
        best_estimator = model.fit(X_train_resampled, y_train_resampled)

    # Evaluasi dengan data uji
    print(f"\nHasil Evaluasi untuk {name}:")
    y_pred = best_estimator.predict(X_test)
    
    print("\nLaporan Klasifikasi:")
    print(classification_report(y_test, y_pred))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Simpan model terbaik
    best_models[name] = best_estimator
    model_filename = f"best_{name.lower().replace(' ', '_')}_model.pkl"
    joblib.dump(best_estimator, model_filename)
    print(f"✅ Model terbaik untuk {name} disimpan sebagai '{model_filename}'")

print(f"\n{'='*30}")
print("Semua model telah selesai diproses.")
print(f"{'='*30}")