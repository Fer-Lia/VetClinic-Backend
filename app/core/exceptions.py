class ClienteNoEncontrado(Exception):
    def __init__(self, dni: str):
        self.dni = dni
        super().__init__(f"No existe un cliente con dni {dni}")


class EmailDuplicado(Exception):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"Ya existe un cliente con el email {email}")


class MascotaNoEncontrada(Exception):
    def __init__(self, id_mascota: int):
        self.id_mascota = id_mascota
        super().__init__(f"No existe una mascota con id {id_mascota}")
