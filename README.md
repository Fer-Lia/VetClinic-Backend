# 🐾 VetClinic — Backend

API REST para la gestión integral de una clínica veterinaria: administración de clientes, sus mascotas, y el equipo de veterinarios que las atiende.

Este backend expone todos los datos y la lógica de negocio necesarios para que un frontend (web o móvil) permita a un administrador gestionar la clínica de forma segura, con autenticación por token y validación de datos en cada paso.

Desarrollado siguiendo una arquitectura en capas, con control de versiones basado en Issues/User Stories y Pull Requests, y buenas prácticas de la industria (validación, manejo de errores centralizado, tests automatizados y migraciones de base de datos).

---

## 📋 Índice

- [Descripción del proyecto](#-descripción-del-proyecto)
- [Tecnologías y herramientas](#-tecnologías-y-herramientas)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Guía de instalación](#-guía-de-instalación)
- [Uso de la API](#-uso-de-la-api)
- [Tests](#-tests)
- [Flujo de trabajo (Git)](#-flujo-de-trabajo-git)
- [Autora](#-autora)

---

## 📖 Descripción del proyecto

VetClinic centraliza tres áreas de gestión de una clínica veterinaria:

- **Clientes**: dueños de mascotas, sus datos de contacto y su historial de visitas.
- **Mascotas**: cada animal, su especie, raza, edad, estado de salud y a qué cliente pertenece.
- **Veterinarios**: el equipo médico, su especialidad y disponibilidad.

Todo el acceso a los datos requiere autenticación (login con email y
contraseña, protegido por JWT), y cada operación de creación/edición pasa
por validaciones estrictas antes de llegar a la base de datos.

### Arquitectura

El proyecto sigue una **arquitectura en capas** (evolución moderna del
patrón MVC para APIs REST sin interfaz gráfica propia), separando
responsabilidades:

```
Petición HTTP
     │
     ▼
  api/v1/        →  Recibe la petición, valida el JWT (Controlador)
     │
     ▼
  services/       →  Lógica de negocio, reglas de validación (Modelo/lógica)
     │
     ▼
  repositories/   →  Acceso puro a la base de datos (consultas)
     │
     ▼
  models/         →  Tablas de PostgreSQL (SQLAlchemy)
```

Esta separación permite testear la lógica de negocio (`services/`) sin
depender de una base de datos real, y cambiar la forma de acceder a los
datos sin tocar las reglas de negocio.

---

## 🛠 Tecnologías y herramientas

### Lenguaje y framework
- **Python 3.14**
- **[FastAPI](https://fastapi.tiangolo.com/)** — framework web asíncrono, con validación y documentación automática
- **[Uvicorn](https://www.uvicorn.org/)** — servidor ASGI que ejecuta la aplicación

### Base de datos
- **PostgreSQL** — motor de base de datos relacional
- **[SQLAlchemy 2.0](https://www.sqlalchemy.org/)** — ORM (mapea las tablas a clases de Python)
- **[Alembic](https://alembic.sqlalchemy.org/)** — control de versiones del esquema de base de datos (migraciones)
- **psycopg2** — driver de conexión Python ↔ PostgreSQL

### Validación y configuración
- **[Pydantic v2](https://docs.pydantic.dev/)** — validación de datos de entrada/salida
- **pydantic-settings** — carga tipada de variables de entorno

### Autenticación y seguridad
- **[python-jose](https://github.com/mpdavis/python-jose)** — creación y verificación de tokens JWT
- **[bcrypt](https://github.com/pyca/bcrypt)** — hashing seguro de contraseñas

### Testing
- **[pytest](https://docs.pytest.org/)** — framework de tests
- **httpx** — cliente HTTP usado por el TestClient de FastAPI

### Herramientas de desarrollo
- **Visual Studio Code** — editor
- **Git + GitHub** — control de versiones
- **GitHub Projects** — tablero Kanban, vinculado a Issues
- **DBeaver** *(opcional)* — cliente visual para PostgreSQL

---

## 📁 Estructura del proyecto

```text
vetclinic-backend/
├── app/
│   ├── main.py                    # Punto de entrada: CORS, rutas, errores
│   │
│   ├── core/                      # Configuración transversal
│   │   ├── config.py                # Settings (variables de entorno)
│   │   ├── security.py              # Hashing de contraseñas + JWT
│   │   ├── exceptions.py            # Excepciones propias del dominio
│   │   └── exception_handlers.py    # Traduce excepciones a JSON consistente
│   │
│   ├── db/                        # Conexión a base de datos
│   │   ├── base_class.py            # Base declarativa de SQLAlchemy
│   │   ├── base.py                  # Importa todos los modelos (para Alembic)
│   │   └── session.py               # Engine, SessionLocal, get_db()
│   │
│   ├── models/                    # Tablas (SQLAlchemy)
│   │   ├── cliente.py
│   │   ├── mascota.py
│   │   ├── veterinario.py
│   │   └── usuario.py               # Usuario admin, para el login
│   │
│   ├── schemas/                   # Forma del JSON de entrada/salida (Pydantic)
│   │   ├── cliente.py
│   │   ├── mascota.py
│   │   ├── veterinario.py
│   │   └── token.py                 # Login, JWT
│   │
│   ├── repositories/              # Acceso puro a datos (queries SQLAlchemy)
│   │   ├── cliente.py
│   │   ├── mascota.py
│   │   ├── veterinario.py
│   │   └── usuario.py
│   │
│   ├── services/                  # Lógica de negocio
│   │   ├── cliente.py
│   │   ├── mascota.py
│   │   ├── veterinario.py
│   │   └── auth.py
│   │
│   └── api/                       # Endpoints HTTP
│       ├── deps.py                  # Dependencia get_current_user (protege rutas)
│       └── v1/
│           ├── router.py            # Agrupa todos los sub-routers
│           ├── auth.py
│           ├── cliente.py
│           ├── mascota.py
│           └── veterinario.py
│
├── alembic/                       # Migraciones de base de datos
│   ├── env.py
│   └── versions/
├── alembic.ini
│
├── scripts/
│   └── seed_data.py                # Carga de datos de ejemplo
│
├── tests/                         # Tests automatizados (pytest)
│   ├── conftest.py                  # Fixtures compartidas (BD en memoria)
│   ├── test_auth.py
│   ├── test_clientes.py
│   ├── test_mascotas.py
│   └── test_veterinarios.py
│
├── requirements.txt                # Dependencias del proyecto
├── .env.example                    # Plantilla de variables de entorno
├── .gitignore
├── ISSUES_BACKLOG.md                # Backlog de desarrollo (User Stories)
├── GITHUB_ISSUES.md                 # Issues listas para copiar a GitHub
└── README.md
```

---

## 🚀 Guía de instalación

### Requisitos previos

- [Python 3.14](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/) instalado y corriendo
- [Git](https://git-scm.com/download/win)
- Un cliente para PostgreSQL como [DBeaver](https://dbeaver.io/download/) *(opcional, para inspeccionar la BD visualmente)*

### 1. Clonar el repositorio

```bash
git clone <URL-de-este-repositorio>
cd vetclinic-backend
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**
```powershell
py -m venv venv
venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
copy .env.example .env      # Windows
cp .env.example .env        # macOS / Linux
```

Edita `.env` con tus datos reales de PostgreSQL y genera una clave secreta:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Pega el resultado en `SECRET_KEY=` dentro de `.env`.

### 5. Crear la base de datos

Desde `psql`, DBeaver o pgAdmin:

```sql
CREATE DATABASE vetclinic_db;
```

*(el nombre debe coincidir con `POSTGRES_DB` en tu `.env`)*

### 6. Aplicar las migraciones

```bash
alembic revision --autogenerate -m "tablas iniciales"
alembic upgrade head
```

### 7. (Opcional) Cargar datos de ejemplo

```bash
python -m scripts.seed_data
```

Crea 6 clientes con sus mascotas, 4 veterinarios y un usuario de prueba:
- **email:** `admin@vetclinic.com`
- **password:** `admin123`

### 8. Arrancar el servidor

```bash
fastapi dev app/main.py
```

- API: **http://localhost:8000**
- Documentación interactiva (Swagger): **http://localhost:8000/docs**

---

## 📡 Uso de la API

### Autenticación

```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "admin@vetclinic.com",
  "password": "admin123"
}
```

Respuesta:
```json
{ "access_token": "eyJhbGciOi...", "token_type": "bearer" }
```

Este token se envía en cada petición posterior:
```http
Authorization: Bearer eyJhbGciOi...
```

### Endpoints principales

| Método | Ruta                       | Descripción                | Auth |
|--------|----------------------------|------------------------------|------|
| POST   | `/api/v1/auth/login`       | Login, devuelve JWT          | No   |
| GET    | `/api/v1/clientes/`        | Listar clientes              | Sí   |
| POST   | `/api/v1/clientes/`        | Crear cliente                | Sí   |
| PUT    | `/api/v1/clientes/{id}`    | Actualizar cliente            | Sí   |
| DELETE | `/api/v1/clientes/{id}`    | Eliminar cliente              | Sí   |
| GET    | `/api/v1/mascotas/`        | Listar mascotas (con dueño)  | Sí   |
| POST   | `/api/v1/mascotas/`        | Crear mascota                | Sí   |
| PUT    | `/api/v1/mascotas/{id}`    | Actualizar mascota            | Sí   |
| DELETE | `/api/v1/mascotas/{id}`    | Eliminar mascota              | Sí   |
| GET    | `/api/v1/veterinarios/`    | Listar veterinarios          | Sí   |
| POST   | `/api/v1/veterinarios/`    | Crear veterinario             | Sí   |
| PUT    | `/api/v1/veterinarios/{id}`| Actualizar veterinario        | Sí   |
| DELETE | `/api/v1/veterinarios/{id}`| Eliminar veterinario          | Sí   |

Lista completa e interactiva siempre disponible en `/docs`.

### Formato de errores

Todos los errores devuelven la misma forma, para que el frontend los trate de manera uniforme:

```json
{ "error": { "type": "not_found", "message": "No se encontró el cliente con id 5" } }
```

Errores de validación de formulario (422) incluyen el campo exacto:

```json
{ "error": { "type": "validation_error", "fields": { "email": "value is not a valid email address" } } }
```

---

## 🧪 Tests

```bash
pytest -v
```

Los tests corren contra una base de datos SQLite en memoria (no tocan tu PostgreSQL real) y cubren:
- Login (credenciales correctas e incorrectas)
- CRUD de Clientes, Mascotas y Veterinarios
- Protección de endpoints (rechazo sin token válido)
- Reglas de negocio (email duplicado, referencias inexistentes)

---

## 🔀 Flujo de trabajo (Git)

- `main` está protegida: todo cambio pasa por un Pull Request, nunca push directo.
- Una rama por funcionalidad, nombrada según su tipo:
  - `feature/nombre-funcionalidad` — funcionalidad nueva
  - `fix/nombre-del-bug` — corrección de errores
  - `chore/nombre-tarea` — tareas de infraestructura sin lógica de negocio
- Cada Pull Request referencia el Issue que resuelve (`Closes #N`), lo que mueve automáticamente la tarjeta en el tablero de GitHub Projects a "Done" al mergear.
- El desarrollo se organiza en Issues/User Stories, documentadas en [`ISSUES_BACKLOG.md`](./ISSUES_BACKLOG.md).

---

## ✍️ Autora

**Lia Fernández**

- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [tu-perfil](https://linkedin.com/in/tu-perfil)

Proyecto final desarrollado como parte de [nombre del bootcamp aquí].
