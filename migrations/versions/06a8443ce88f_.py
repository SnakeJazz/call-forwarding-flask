"""empty message

Revision ID: 06a8443ce88f
Revises: 
Create Date: 2017-03-30 10:15:50.340237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06a8443ce88f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('states',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zipcodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zipcode', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('senators',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('senators')
    op.drop_table('zipcodes')
    op.drop_table('states')
    # ### end Alembic commands ###
