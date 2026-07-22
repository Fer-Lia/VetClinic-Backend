"""agregar email a veterinarios

Revision ID: dd9e4080c703
Revises: d451e1f4ae2a
Create Date: 2026-07-21 12:11:40.072843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd9e4080c703'
down_revision: Union[str, None] = 'd451e1f4ae2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('veterinarios', sa.Column('email', sa.String(length=150), nullable=True))

    # Backfill: los veterinarios ya existentes no tienen email todavía.
    # Se les asigna uno ficticio único (dni@example.com) para poder
    # aplicar unique + NOT NULL sin romper filas actuales. Se usa
    # example.com (dominio reservado por RFC 2606 para pruebas) porque
    # email-validator rechaza TLDs de uso especial como .local.
    veterinarios = sa.table(
        'veterinarios',
        sa.column('dni', sa.String),
        sa.column('email', sa.String),
    )
    connection = op.get_bind()
    connection.execute(
        veterinarios.update()
        .where(veterinarios.c.email.is_(None))
        .values(email=sa.func.concat(veterinarios.c.dni, '@example.com'))
    )

    op.alter_column('veterinarios', 'email', nullable=False)
    op.create_index(op.f('ix_veterinarios_email'), 'veterinarios', ['email'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_veterinarios_email'), table_name='veterinarios')
    op.drop_column('veterinarios', 'email')
