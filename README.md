# test_post_tcit
Challenge de desarrollo

# Instalar la versión de python
- python 3.12.4

# Instalar las librerías
- cd backend
- pip install -r requirements.txt

# Inicializar postgres
- docker run --name postsDB -p 5432:5432 -e POSTGRES_PASSWORD=admin123 -d postgres

# Instalar migraciones (opcionales para este proyecto)
- python manage.py migrate

# Iniciar aplicación backend
- python manage.py runserver

# Instalar versión de node
- node v22.8.0

# Instalar librerías
- cd ..
- cd frontend
- npm install

# Iniciar aplicación frontend
- npm run dev

