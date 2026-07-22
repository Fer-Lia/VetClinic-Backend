# 🐾 VetClinic — Backend

API REST para la gestión de una clínica veterinaria: clientes, sus mascotas y el equipo de veterinarios que las atiende.

![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-por%20definir-lightgrey)
![Tests](https://img.shields.io/badge/tests-pytest-yellowgreen)

## Tabla de contenidos

- [Características](#-características)
- [Arquitectura](#-arquitectura)
- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Configuración](#-configuración)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Tests](#-tests)
- [Cómo contribuir](#-cómo-contribuir)
- [Roadmap](#-roadmap)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

---

## ✨ Características

- Gestión CRUD de **clientes**, **mascotas** y **veterinarios**.
- Validación de datos de entrada/salida con Pydantic v2.
- Manejo de errores centralizado, con respuestas JSON consistentes.
- Migraciones de base de datos versionadas con Alembic.
- Documentación interactiva automática (Swagger) en `/docs`.
- Tests automatizados con pytest, sobre base de datos en memoria.

## 🏗 Arquitectura

El proyecto sigue una **arquitectura en capas**:

```
Petición HTTP
     │
     ▼
  api/         →  Recibe la petición, valida el JSON de entrada
     │
     ▼
  services/    →  Lógica de negocio
     │
     ▼
  repositories/ →  Acceso a la base de datos
     │
     ▼
  models/      →  Tablas de PostgreSQL (SQLAlchemy)
```

Esta separación permite testear la lógica de negocio sin depender de una base de datos real, y cambiar la forma de acceder a los datos sin tocar las reglas de negocio.

## 📋 Requisitos previos

- [Python 3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/) instalado y corriendo
- [Git](https://git-scm.com/download/win)
- Un cliente para PostgreSQL como [DBeaver](https://dbeaver.io/download/) *(opcional)*

## 🚀 Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL-de-este-repositorio>
   cd vetclinic-backend
   ```

2. Crea y activa el entorno virtual:

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

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno (ver [Configuración](#-configuración)).

5. Crea la base de datos y aplica las migraciones:

   ```sql
   CREATE DATABASE veterinaria_db;
   ```

   ```bash
   alembic upgrade head
   ```

## ▶️ Uso

Arranca el servidor en modo desarrollo:

```bash
fastapi dev app/main.py
```

- API: **http://localhost:8000**
- Documentación interactiva (Swagger): **http://localhost:8000/docs**

Cada entidad expone endpoints CRUD estándar (crear, listar, obtener por id, actualizar, eliminar); la lista completa e interactiva está siempre disponible en `/docs`.

Los errores devuelven una forma consistente:

```json
{ "error": { "type": "not_found", "message": "No se encontró el cliente con id 5" } }
```

## ⚙️ Configuración

Copia el archivo de ejemplo y ajusta los valores con tus datos reales de PostgreSQL:

```bash
copy .env.example .env      # Windows
cp .env.example .env        # macOS / Linux
```

```env
# .env.example
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=tu_contraseña_aqui
DB_NAME=veterinaria_db
```

## 📁 Estructura del proyecto

```text
vetclinic-backend/
├── app/
│   ├── main.py             # Punto de entrada: CORS, rutas, errores
│   ├── core/                # Configuración transversal (settings, excepciones, logging)
│   ├── db/                  # Conexión a base de datos
│   ├── models/               # Tablas (SQLAlchemy)
│   ├── schemas/              # Forma del JSON de entrada/salida (Pydantic)
│   ├── repositories/          # Acceso a datos
│   ├── services/              # Lógica de negocio
│   └── api/                   # Endpoints HTTP
│
├── alembic/                 # Migraciones de base de datos
├── tests/                    # Tests automatizados (pytest)
├── logs/                     # Logs de la aplicación
│
├── requirements.txt
├── .env.example
├── .gitignore
├── ISSUES_BACKLOG.md         # Backlog de desarrollo
├── DECISIONES.md             # Registro de decisiones técnicas
└── README.md
```

## 🧪 Tests

```bash
pytest -v
```

Los tests corren contra una base de datos PostgreSQL separada (`vetclinic_test`, distinta de la de desarrollo), que debe existir antes de ejecutar la suite:

```sql
CREATE DATABASE vetclinic_test;
```

Actualmente cubren el CRUD de Clientes.

## 🤝 Cómo contribuir

1. Crea una rama según el tipo de cambio: `feature/...`, `fix/...` o `chore/...`.
2. Sigue la arquitectura en capas ya establecida (`api` → `services` → `repositories` → `models`).
3. Asegúrate de que `pytest -v` pasa antes de abrir el Pull Request.
4. Abre un Pull Request contra `main` referenciando el issue que resuelve (`Closes #N`). `main` está protegida: no se permite push directo.

Más detalle del backlog y las convenciones de rama en [`ISSUES_BACKLOG.md`](./ISSUES_BACKLOG.md).

## 🗺 Roadmap

- [x] CRUD de Clientes, Mascotas y Veterinarios
- [x] Manejo de errores centralizado
- [x] Migraciones de base de datos con Alembic
- [ ] Autenticación (login + JWT)
- [ ] Gestión de citas/visitas

## 📄 Licencia

[Por definir]

## ✍️ Contacto

**Lia Fernández**

- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [tu-perfil](https://linkedin.com/in/tu-perfil)

Proyecto final desarrollado como parte de [nombre del bootcamp aquí].
