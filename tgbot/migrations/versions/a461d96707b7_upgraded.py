"""upgraded

Revision ID: a461d96707b7
Revises: 0ce6bb23753e
Create Date: 2023-02-20 11:02:20.794831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a461d96707b7'
down_revision = '0ce6bb23753e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_members', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('game_members_owner_fkey', 'game_members', type_='foreignkey')
    op.create_foreign_key(None, 'game_members', 'users', ['user_id'], ['tg_id'])
    op.drop_column('game_members', 'owner')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_members', sa.Column('owner', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'game_members', type_='foreignkey')
    op.create_foreign_key('game_members_owner_fkey', 'game_members', 'users', ['owner'], ['tg_id'])
    op.drop_column('game_members', 'user_id')
    # ### end Alembic commands ###
