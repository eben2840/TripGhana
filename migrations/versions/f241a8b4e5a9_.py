"""empty message

Revision ID: f241a8b4e5a9
Revises: 20436a436c5e
Create Date: 2022-10-23 13:43:56.772212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f241a8b4e5a9'
down_revision = '20436a436c5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('src',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('srcname', sa.String(), nullable=True),
    sa.Column('srcnumb', sa.String(), nullable=True),
    sa.Column('Hoodie', sa.String(), nullable=True),
    sa.Column('sweat', sa.String(), nullable=True),
    sa.Column('bag', sa.String(), nullable=True),
    sa.Column('shirt', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'course', ['email'])
    op.drop_column('course', 'name')
    op.drop_column('item', 'incase')
    op.drop_column('item', 'image_file')
    op.drop_column('item', 'des')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('des', sa.VARCHAR(), nullable=True))
    op.add_column('item', sa.Column('image_file', sa.VARCHAR(), nullable=True))
    op.add_column('item', sa.Column('incase', sa.VARCHAR(), nullable=True))
    op.add_column('course', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'course', type_='unique')
    op.drop_table('src')
    # ### end Alembic commands ###