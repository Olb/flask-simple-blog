"""empty message

Revision ID: 1859e0bc33ec
Revises: f184ce821e83
Create Date: 2019-09-08 18:42:18.694658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1859e0bc33ec'
down_revision = 'f184ce821e83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
