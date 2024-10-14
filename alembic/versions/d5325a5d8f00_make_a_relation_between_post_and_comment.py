"""make a relation between post and comment

Revision ID: d5325a5d8f00
Revises: 0108361775f0
Create Date: 2024-10-14 14:18:25.009066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5325a5d8f00'
down_revision: Union[str, None] = '0108361775f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('post_id', sa.Uuid(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('posts', 'category',
               existing_type=sa.VARCHAR(length=8),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'category',
               existing_type=sa.VARCHAR(length=8),
               nullable=True)
    op.drop_table('comments')
    # ### end Alembic commands ###
