"""empty message

Revision ID: f184ce821e83
Revises: f2c83043d645
Create Date: 2019-09-08 18:39:42.817794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f184ce821e83'
down_revision = 'f2c83043d645'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    # ### end Alembic commands ###
