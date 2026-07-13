CLIENTE_EJEMPLO = {
    "nombre": "Test",
    "apellido": "Uno",
    "direccion": "Calle Falsa 123",
    "telefono": "600000001",
    "email": "test.uno@ejemplo.com",
    "dni": "00000001A",
}


def test_crear_cliente(client):
    respuesta = client.post("/clientes", json=CLIENTE_EJEMPLO)

    assert respuesta.status_code == 201
    assert respuesta.json()["dni"] == CLIENTE_EJEMPLO["dni"]
    assert respuesta.json()["email"] == CLIENTE_EJEMPLO["email"]


def test_crear_cliente_con_email_duplicado(client):
    client.post("/clientes", json=CLIENTE_EJEMPLO)

    otro_cliente = {**CLIENTE_EJEMPLO, "dni": "00000002B"}
    respuesta = client.post("/clientes", json=otro_cliente)

    assert respuesta.status_code == 409


def test_listar_clientes(client):
    client.post("/clientes", json=CLIENTE_EJEMPLO)

    respuesta = client.get("/clientes")

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 1


def test_obtener_cliente_existente(client):
    client.post("/clientes", json=CLIENTE_EJEMPLO)

    respuesta = client.get(f"/clientes/{CLIENTE_EJEMPLO['dni']}")

    assert respuesta.status_code == 200
    assert respuesta.json()["nombre"] == CLIENTE_EJEMPLO["nombre"]


def test_obtener_cliente_inexistente(client):
    respuesta = client.get("/clientes/99999999Z")

    assert respuesta.status_code == 404


def test_actualizar_cliente(client):
    client.post("/clientes", json=CLIENTE_EJEMPLO)

    respuesta = client.put(
        f"/clientes/{CLIENTE_EJEMPLO['dni']}",
        json={"telefono": "699999999"},
    )

    assert respuesta.status_code == 200
    assert respuesta.json()["telefono"] == "699999999"
    assert respuesta.json()["nombre"] == CLIENTE_EJEMPLO["nombre"]


def test_eliminar_cliente(client):
    client.post("/clientes", json=CLIENTE_EJEMPLO)

    respuesta = client.delete(f"/clientes/{CLIENTE_EJEMPLO['dni']}")
    assert respuesta.status_code == 204

    respuesta_get = client.get(f"/clientes/{CLIENTE_EJEMPLO['dni']}")
    assert respuesta_get.status_code == 404
