"""empty message

Revision ID: 048b288ee8a9
Revises: e1c3407a6bd3
Create Date: 2023-04-09 00:01:18.580696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '048b288ee8a9'
down_revision = 'e1c3407a6bd3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
