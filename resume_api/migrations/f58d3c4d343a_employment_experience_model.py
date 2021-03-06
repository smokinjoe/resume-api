"""employment_experience model

Revision ID: f58d3c4d343a
Revises: d49725ce8f3b
Create Date: 2018-02-22 03:58:57.108283

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f58d3c4d343a'
down_revision = 'd49725ce8f3b'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employment_experience',
    sa.Column('company_name', sa.Unicode(length=127), nullable=False),
    sa.Column('company_role', sa.Unicode(length=255), nullable=False),
    sa.Column('date_start', sa.Unicode(length=127), nullable=False),
    sa.Column('date_end', sa.Unicode(length=127), nullable=False),
    sa.Column('responsibilities', sa.PickleType(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employment_experience')
    # ### end Alembic commands ###
