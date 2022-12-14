"""empty message

Revision ID: f8716661c577
Revises: 50960334bb52
Create Date: 2022-09-23 13:09:42.200620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8716661c577'
down_revision = '50960334bb52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'name')
    # ### end Alembic commands ###
