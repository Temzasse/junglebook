"""empty message

Revision ID: ced7454a8c0
Revises: 132c13afed9f
Create Date: 2015-02-08 17:52:13.907553

"""

# revision identifiers, used by Alembic.
revision = 'ced7454a8c0'
down_revision = '132c13afed9f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banana_givers',
    sa.Column('giver_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['giver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], )
    )
    op.drop_table('receivers')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('receivers',
    sa.Column('giver_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('receiver_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['giver_id'], [u'user.id'], name=u'receivers_giver_id_fkey'),
    sa.ForeignKeyConstraint(['receiver_id'], [u'user.id'], name=u'receivers_receiver_id_fkey')
    )
    op.drop_table('banana_givers')
    ### end Alembic commands ###
