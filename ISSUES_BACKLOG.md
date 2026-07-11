# ISSUES_BACKLOG.md — VetClinic Backend

Backlog de issues del proyecto, ordenado por prioridad de ejecución. Cada
issue se resuelve en su propia rama (`feature/...`, `fix/...`, `chore/...`)
y se cierra vía PR con `Closes #N`. Un issue = una rama = un PR. No se
mezclan varios issues en el mismo cambio.

---

## Épica 1: Fundación del proyecto

### #1 — chore: estructura base del proyecto y configuración
**Rama:** `chore/estructura-base`

- Crear estructura de carpetas `app/{config,db,models,schemas,api,services,repositories}`
- `requirements.txt` con dependencias fijadas (FastAPI, Uvicorn, SQLAlchemy, psycopg2-binary, Pydantic, Pydantic Settings, Alembic, python-dotenv, email-validator)
- `app/config/settings.py` con Pydantic Settings leyendo `.env`
- `.env.example` (sin credenciales reales) y `.gitignore` (incluye `.env`, `venv/`, `__pycache__/`)
- `app/db/database.py`: engine, `SessionLocal`, `Base` declarativa
- `app/main.py`: instancia FastAPI mínima, healthcheck `GET /`

**Criterio de aceptación:** `fastapi dev app/main.py` levanta el servidor y `/docs` responde.

---

### #2 — chore: configurar Alembic
**Rama:** `chore/alembic-setup`

- `alembic init alembic`
- Configurar `alembic/env.py` para leer `DB_*` desde `app/config/settings.py` y usar `Base.metadata` como target
- Primera migración vacía de verificación

**Criterio de aceptación:** `alembic upgrade head` conecta contra `veterinaria_db` sin errores.

**Depende de:** #1

---

## Épica 2: Entidad Cliente

### #3 — feat: modelo y schema de Cliente
**Rama:** `feature/cliente-modelo`

- `app/models/cliente.py`: tabla `clientes` (dni como PK, nombre, email único, teléfono)
- `app/schemas/cliente.py`: `ClienteCreate`, `ClienteUpdate`, `ClienteOut` (Pydantic, valida email con `email-validator`)
- Migración Alembic generada con `--autogenerate`

**Criterio de aceptación:** la tabla existe en PostgreSQL tras `alembic upgrade head`.

**Depende de:** #2

### #4 — feat: repository de Cliente
**Rama:** `feature/cliente-repository`

- `app/repositories/cliente.py`: funciones CRUD contra la BD (crear, obtener por dni, listar, actualizar, eliminar) usando la sesión de SQLAlchemy. Sin lógica de negocio aquí.

**Depende de:** #3

### #5 — feat: service de Cliente
**Rama:** `feature/cliente-service`

- `app/services/cliente.py`: reglas de negocio (ej. no permitir email duplicado), llama al repository, lanza excepciones controladas (`HTTPException` o excepción propia) si algo no es válido.

**Depende de:** #4

### #6 — feat: endpoints CRUD de Cliente
**Rama:** `feature/cliente-api`

- `app/api/cliente.py`: `POST/GET/GET{dni}/PUT/DELETE /clientes`, delega todo al service
- Manejo de errores: 404 si no existe, 409 si email duplicado
- Registrar el router en `main.py`

**Criterio de aceptación:** probar los 5 endpoints desde `/docs` con datos reales.

**Depende de:** #5

### #7 — test: tests de Cliente
**Rama:** `feature/cliente-tests`

- Tests con `pytest` (patrón AAA) cubriendo: creación válida, email duplicado, actualización, borrado, cliente no encontrado

**Depende de:** #6

---

## Épica 3: Entidad Mascota

### #8 — feat: modelo y schema de Mascota
**Rama:** `feature/mascota-modelo`

- `app/models/mascota.py`: tabla `mascotas` con FK `dni_cliente` → `clientes.dni`
- `app/schemas/mascota.py`: `MascotaCreate`, `MascotaUpdate`, `MascotaOut`
- Migración Alembic

**Depende de:** #3

### #9 — feat: repository de Mascota
**Rama:** `feature/mascota-repository`

**Depende de:** #8

### #10 — feat: service de Mascota
**Rama:** `feature/mascota-service`

- Validar que `dni_cliente` exista antes de crear la mascota (llama al service/repository de Cliente)

**Depende de:** #9

### #11 — feat: endpoints CRUD de Mascota
**Rama:** `feature/mascota-api`

- Incluir `GET /clientes/{dni}/mascotas` para listar mascotas de un cliente

**Depende de:** #10

### #12 — test: tests de Mascota
**Rama:** `feature/mascota-tests`

- Incluir caso: crear mascota con `dni_cliente` inexistente → error controlado, no 500

**Depende de:** #11

---

## Épica 4: Entidad Veterinario

### #13 — feat: modelo y schema de Veterinario
**Rama:** `feature/veterinario-modelo`

**Depende de:** #2

### #14 — feat: repository de Veterinario
**Rama:** `feature/veterinario-repository`

**Depende de:** #13

### #15 — feat: service de Veterinario
**Rama:** `feature/veterinario-service`

**Depende de:** #14

### #16 — feat: endpoints CRUD de Veterinario
**Rama:** `feature/veterinario-api`

**Depende de:** #15

### #17 — test: tests de Veterinario
**Rama:** `feature/veterinario-tests`

**Depende de:** #16

---

## Épica 5: Calidad transversal

### #18 — chore: manejo global de errores
**Rama:** `chore/error-handling`

- Exception handlers globales en `main.py` (`IntegrityError` de SQLAlchemy → 409, `NoResultFound` → 404, genérico → 500 con mensaje amigable)
- Nunca exponer el traceback ni el detalle técnico de la BD al cliente de la API

**Depende de:** #6, #11, #16

### #19 — chore: logging
**Rama:** `chore/logging`

- Configurar `logging` estándar de Python: nivel `INFO` en desarrollo, formato con timestamp
- Log de cada error capturado por los exception handlers (`ERROR`) y arranque del servidor (`INFO`)

**Depende de:** #18

### #20 — docs: README final y colección de pruebas
**Rama:** `chore/docs-finales`

- Revisar que el README refleje la estructura real del proyecto
- Añadir sección de cómo correr los tests
- (Opcional) colección de Postman/Thunder Client exportada en `/docs`

**Depende de:** #17, #19

---

## Convención de estado

Marca aquí el progreso según se van cerrando los PRs:

- [ ] #1  [ ] #2  [ ] #3  [ ] #4  [ ] #5  [ ] #6  [ ] #7
- [ ] #8  [ ] #9  [ ] #10 [ ] #11 [ ] #12
- [ ] #13 [ ] #14 [ ] #15 [ ] #16 [ ] #17
- [ ] #18 [ ] #19 [ ] #20
