"""First Migration

Revision ID: 5b8f25a0117d
Revises: 
Create Date: 2020-09-20 19:15:02.446983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b8f25a0117d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email_primary', sa.String(length=1000), nullable=False),
    sa.Column('phone_primary', sa.String(length=1000), nullable=False),
    sa.Column('password', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_primary'),
    sa.UniqueConstraint('phone_primary'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('email_secondary', sa.String(length=1000), nullable=True),
    sa.Column('phone_secondary', sa.String(length=1000), nullable=True),
    sa.Column('region', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=1000), nullable=True),
    sa.Column('state', sa.String(length=1000), nullable=True),
    sa.Column('city', sa.String(length=1000), nullable=True),
    sa.Column('zip_code', sa.String(length=1000), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('person')
    # ### end Alembic commands ###
