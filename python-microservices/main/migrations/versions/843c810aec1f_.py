"""empty message

Revision ID: 843c810aec1f
Revises: 
Create Date: 2020-12-08 08:40:37.736465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '843c810aec1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_user')
    op.drop_table('product')
    # ### end Alembic commands ###