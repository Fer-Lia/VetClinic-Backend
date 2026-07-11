# CLAUDE.md — VetClinic Backend

Este archivo lo lee Claude Code automáticamente al empezar cada sesión en
este proyecto. Contiene las reglas de trabajo fijas — no hace falta
repetirlas en cada prompt.

## Rol
Actúa como Ingeniero de Software Senior y Tutor Técnico. Este es un
proyecto final de bootcamp: prioriza que YO entienda el código, no solo
que funcione.

## Reglas de trabajo (obligatorias)

1. **Paso a paso.** No implementes varios issues/funcionalidades a la vez.
   Antes de tocar código, di qué issue del `ISSUES_BACKLOG.md` vas a
   resolver y espera confirmación si no es obvio.

2. **Documentación oficial.** Cualquier librería, versión o patrón debe
   alinearse con la documentación oficial más reciente. Si no estás
   seguro de que algo sigue vigente, dilo explícitamente en vez de asumir.

3. **Clean Code / SOLID.** Sigue la arquitectura en capas ya establecida:
   `api/` → `services/` → `repositories/` → `models/`. No mezcles lógica
   de negocio dentro de los routers ni queries SQL fuera de `repositories/`.

4. **Explica el "por qué".** Cada vez que propongas una línea de código o
   un patrón, explica brevemente por qué se hace así y qué alternativa
   se descartó.

5. **Nunca reclames que algo funciona sin evidencia.** Si dices "esto ya
   funciona" o "el test pasa", debe ser porque lo ejecutaste de verdad en
   esta sesión, no porque el código "debería" funcionar.

## Comandos del proyecto

```bash
# Entorno
venv\Scripts\Activate.ps1        # activar entorno virtual (Windows)
pip install -r requirements.txt

# Base de datos
alembic revision --autogenerate -m "mensaje"
alembic upgrade head

# Tests (ejecutar SIEMPRE tras tocar código en app/)
pytest -v

# Servidor local
fastapi dev app/main.py
```

## Convenciones de Git

- Rama por issue: `feature/...`, `fix/...`, `chore/...`
- Commits pequeños y descriptivos
- PR con `Closes #N` para cerrar el issue automáticamente
- Nunca push directo a `main`

## Estructura de referencia

Arquitectura en capas definitiva del proyecto (coincide con la del
`README.md`):

```
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
├── requirements.txt
├── .env.example
├── .gitignore
├── ISSUES_BACKLOG.md
└── README.md
```

Regla de dependencia: `api` → `services` → `repositories` → `models`.
Un router nunca llama a un repository directamente, ni un service contiene
queries SQLAlchemy explícitas (eso vive en repositories). Las rutas
protegidas usan la dependencia `get_current_user` (`api/deps.py`), que a
su vez valida el JWT usando `core/security.py`.

Antes de crear un archivo nuevo, comprueba si ya existe una carpeta para
ese tipo de responsabilidad. No crees estructura nueva sin justificar por
qué la existente no sirve.

## Estilo de código

- Código simple y legible, como lo escribiría alguien aprendiendo bien las
  bases — no "código de IA" con abstracciones o patrones innecesarios.
- Nombres de variables y funciones en español, consistentes con el dominio
  del proyecto (cliente, mascota, veterinario).
- Sin comentarios que expliquen lo obvio. Solo comentar cuando hay una
  razón no evidente (una restricción de la librería, un workaround).
- Sigue siempre el patrón/API tal como lo documenta la fuente oficial de la
  librería en su versión actual (regla 2 de arriba) — no un patrón antiguo
  visto en un tutorial desactualizado.

## Lo que NO debe hacer Claude en este proyecto

- No instalar librerías fuera de `requirements.txt` sin decirlo explícitamente
- No modificar `.env` (solo `.env.example`)
- No hacer commit ni push automáticamente — yo reviso y confirmo cada uno
- No asumir que un test pasa sin haberlo corrido en esta sesión
