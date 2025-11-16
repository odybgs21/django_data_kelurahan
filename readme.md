# Aplikasi Data Warga Kelurahan

Aplikasi sederhana untuk mengelola data warga menggunakan **Django REST Framework** sebagai backend dan **HTML + JavaScript** sebagai frontend.  
Fitur utama mencakup menampilkan daftar warga serta menambah data warga melalui form.

---

## 🚀 Teknologi yang Digunakan

### Backend
- Python 3
- Django
- Django REST Framework
- django-filter

### Frontend
- HTML
- Vanilla JavaScript (Fetch API)

# 📦 Instalasi Backend

Ikuti langkah berikut untuk menjalankan backend secara lokal.

---

## 1️⃣ Clone Repository
git clone https://github.com/username/nama-repo.git

## 2️⃣ Buat Virtual Environment
python -m venv venv

## 3️⃣ Aktifkan:
Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate

## 4️⃣ Instalasi Django
pip install django

## 5️⃣ Instalasi  Requirements
Pastikan file requirements.txt ada, lalu jalankan:

pip install -r requirements.txt

## 6️⃣ Jalankan Migrasi Database
python manage.py migrate

Jika kamu memiliki model tambahan, jalankan:

python manage.py makemigrations
python manage.py migrate

## 7️⃣ Buat Superuser (Opsional)
Jika ingin akses Django Admin:

python manage.py createsuperuser

## 8️⃣ Jalankan Server
python manage.py runserver

Backend akan berjalan di:

http://127.0.0.1:8000/


Endpoint API warga:

http://127.0.0.1:8000/api/warga/

## Repo Frontend
frontendnya ada disini yaa https://github.com/odybgs21/frontend_django_kelurahan.git

## 📘 Dokumentasi API

API dilengkapi dengan dokumentasi otomatis menggunakan drf-spectacular.

Schema (YAML):
http://127.0.0.1:8000/api/schema/

Swagger UI:
http://127.0.0.1:8000/api/schema/swagger-ui/

Redoc:
http://127.0.0.1:8000/api/schema/redoc/

## 🤝 Kontribusi
Pull Requests sangat diterima.
Buat branch baru sebelum mengajukan PR.

## 📄 Lisensi
MIT License.