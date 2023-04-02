"""Init

Revision ID: cee7a9b37ea4
Revises: 
Create Date: 2023-04-02 23:03:07.298591

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cee7a9b37ea4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('fullname', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    # ### end Alembic commands ###