"""empty message

Revision ID: d4fb62e1bace
Revises: f0916def4c1c
Create Date: 2019-03-06 17:48:45.688515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4fb62e1bace'
down_revision = 'f0916def4c1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolios', sa.Column('name', sa.String(length=256), nullable=True))
    op.create_index(op.f('ix_portfolios_name'), 'portfolios', ['name'], unique=True)
    op.drop_index('ix_portfolios_portfolio_name', table_name='portfolios')
    op.drop_column('portfolios', 'portfolio_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolios', sa.Column('portfolio_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.create_index('ix_portfolios_portfolio_name', 'portfolios', ['portfolio_name'], unique=False)
    op.drop_index(op.f('ix_portfolios_name'), table_name='portfolios')
    op.drop_column('portfolios', 'name')
    # ### end Alembic commands ###
