"""empty message

Revision ID: e6f8ee059484
Revises: 80868384a4cf
Create Date: 2020-11-13 23:19:37.544627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6f8ee059484'
down_revision = '80868384a4cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('author', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'author')
    # ### end Alembic commands ###
