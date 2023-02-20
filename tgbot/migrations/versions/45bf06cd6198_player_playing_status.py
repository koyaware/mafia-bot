"""player playing status

Revision ID: 45bf06cd6198
Revises: a461d96707b7
Create Date: 2023-02-20 12:04:58.521956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45bf06cd6198'
down_revision = 'a461d96707b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_members', sa.Column('is_playing', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game_members', 'is_playing')
    # ### end Alembic commands ###
