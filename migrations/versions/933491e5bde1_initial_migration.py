"""initial migration

Revision ID: 933491e5bde1
Revises: 
Create Date: 2024-11-30 16:40:38.012359

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '933491e5bde1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('activado', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='catalogo'
    )
    op.drop_table('compras')
    op.drop_table('productos')
    op.drop_table('pagos')
    op.drop_table('stock')
    op.drop_table('movimientos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movimientos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('producto_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fecha_transaccion', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('cantidad', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('entrada_salida', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint("entrada_salida = ANY (ARRAY[1, '-1'::integer])", name='movimientos_entrada_salida_check'),
    sa.PrimaryKeyConstraint('id', name='movimientos_pkey')
    )
    op.create_table('stock',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('producto_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cantidad', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='stock_pkey')
    )
    op.create_table('pagos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('producto_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('precio', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('medio_pago', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pagos_pkey')
    )
    op.create_table('productos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('precio', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('activado', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='productos_pkey')
    )
    op.create_table('compras',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('producto_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fecha_compra', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('direccion_envio', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='compras_pkey')
    )
    op.drop_table('productos', schema='catalogo')
    # ### end Alembic commands ###
