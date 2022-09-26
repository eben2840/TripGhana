"""empty message

Revision ID: fdc5c030b1fb
Revises: f8716661c577
Create Date: 2022-09-26 16:06:28.308532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdc5c030b1fb'
down_revision = 'f8716661c577'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('budget', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'course', ['name'])
    op.create_unique_constraint(None, 'course', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'course', type_='unique')
    op.drop_constraint(None, 'course', type_='unique')
    op.drop_column('course', 'budget')
    # ### end Alembic commands ###
