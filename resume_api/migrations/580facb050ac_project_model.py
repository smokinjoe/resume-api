"""project model

Revision ID: 580facb050ac
Revises: f0df9ce1fbe8
Create Date: 2018-02-16 23:02:45.866358

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '580facb050ac'
down_revision = 'f0df9ce1fbe8'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link_title', sa.Unicode(length=255), nullable=False))
        batch_op.add_column(sa.Column('link_url', sa.Unicode(length=255), nullable=False))
        batch_op.add_column(sa.Column('title', sa.Unicode(length=255), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('title')
        batch_op.drop_column('link_url')
        batch_op.drop_column('link_title')

    # ### end Alembic commands ###
