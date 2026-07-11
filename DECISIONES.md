# DECISIONES.md — VetClinic Backend

Bitácora de decisiones técnicas del proyecto. Cada vez que se introduce
una librería, patrón o estructura nueva, se registra aquí: **qué es**,
**por qué se eligió** y **qué alternativa se descartó**. Sirve para poder
explicar el proyecto en una entrevista o defensa sin tener que recordarlo
todo de memoria.

---

## Python 3.13 en vez de 3.14

**Qué es:** la versión de Python usada para el entorno virtual (`venv`)
del proyecto.

**Por qué se eligió:** Python 3.14 es una versión demasiado reciente.
`pydantic-core` (dependencia de Pydantic, escrita en Rust usando el
puente PyO3) falla al instalarse en 3.14 porque PyO3 0.22.6 solo da
soporte oficial hasta Python 3.13. Al no encontrar wheel precompilado,
pip intenta compilar desde código fuente y el propio compilador de Rust
rechaza continuar con este mensaje:

```
error: the configured Python interpreter version (3.14) is newer than
PyO3's maximum supported version (3.13)
```

**Cómo se detectó:** se instaló `pydantic-core` de forma aislada y
funcionó (pip encontró un wheel ya publicado para 3.14), pero al
resolver todas las dependencias juntas desde `requirements.txt`, pip
bajó a una versión distinta de `pydantic-core` que sí requería compilar.

**Alternativa descartada:** fijar una versión concreta de `pydantic-core`
en `requirements.txt` para forzar a pip a usar la que sí tenía wheel.
Se descartó porque es frágil (depende de que ese wheel siga publicado) y
no resuelve el problema de fondo con otras futuras dependencias en Rust/C.

**Solución aplicada:** recrear el entorno virtual con Python 3.13
(`py -3.13 -m venv venv`), versión con soporte maduro y probado en todo
el ecosistema de FastAPI/SQLAlchemy/Pydantic.
