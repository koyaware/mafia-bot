"""'initial'

Revision ID: e096793a063c
Revises: 
Create Date: 2023-02-20 09:35:47.563225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e096793a063c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('tg_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('tg_id')
    )
    op.create_table('room',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.tg_id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('game_members',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.tg_id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_members')
    op.drop_table('room')
    op.drop_table('users')
    # ### end Alembic commands ###