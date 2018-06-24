"""empty message

Revision ID: 8d5bfb2f5742
Revises: 
Create Date: 2018-06-24 11:52:21.583745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d5bfb2f5742'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channel',
    sa.Column('channel_id', sa.Integer(), nullable=False),
    sa.Column('channel_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('channel_id')
    )
    op.create_table('citizenstate',
    sa.Column('cs_id', sa.Integer(), nullable=False),
    sa.Column('cs_state_name', sa.String(length=100), nullable=False),
    sa.Column('cs_state_desc', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('cs_id')
    )
    op.create_table('csrstate',
    sa.Column('csr_state_id', sa.Integer(), nullable=False),
    sa.Column('csr_state_name', sa.String(length=50), nullable=False),
    sa.Column('csr_state_desc', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('csr_state_id')
    )
    op.create_table('metadata',
    sa.Column('metadata_id', sa.Integer(), nullable=False),
    sa.Column('meta_text', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('metadata_id')
    )
    op.create_table('periodstate',
    sa.Column('ps_id', sa.Integer(), nullable=False),
    sa.Column('ps_name', sa.String(length=100), nullable=False),
    sa.Column('ps_desc', sa.String(length=1000), nullable=False),
    sa.Column('ps_number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('ps_id')
    )
    op.create_table('permission',
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.Column('permission_code', sa.String(length=100), nullable=False),
    sa.Column('permission_desc', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('permission_id')
    )
    op.create_table('role',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('role_code', sa.String(length=100), nullable=True),
    sa.Column('role_desc', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('service',
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('service_code', sa.String(length=50), nullable=False),
    sa.Column('service_name', sa.String(length=500), nullable=False),
    sa.Column('service_desc', sa.String(length=2000), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.Column('prefix', sa.String(length=10), nullable=False),
    sa.Column('display_dashboard_ind', sa.Integer(), nullable=False),
    sa.Column('actual_service_ind', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['service.service_id'], ),
    sa.PrimaryKeyConstraint('service_id')
    )
    op.create_table('smartboard',
    sa.Column('sb_id', sa.Integer(), nullable=False),
    sa.Column('sb_type', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('sb_id')
    )
    op.create_table('srstate',
    sa.Column('sr_state_id', sa.Integer(), nullable=False),
    sa.Column('sr_code', sa.String(length=100), nullable=False),
    sa.Column('sr_state_desc', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('sr_state_id')
    )
    op.create_table('office',
    sa.Column('office_id', sa.Integer(), nullable=False),
    sa.Column('office_name', sa.String(length=100), nullable=True),
    sa.Column('office_number', sa.Integer(), nullable=True),
    sa.Column('sb_id', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['sb_id'], ['smartboard.sb_id'], ),
    sa.PrimaryKeyConstraint('office_id')
    )
    op.create_table('role_permission',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permission.permission_id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.role_id'], ),
    sa.PrimaryKeyConstraint('role_id', 'permission_id')
    )
    op.create_table('service_metadata',
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('metadata_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['metadata_id'], ['metadata.metadata_id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.service_id'], ),
    sa.PrimaryKeyConstraint('service_id', 'metadata_id')
    )
    op.create_table('citizen',
    sa.Column('citizen_id', sa.Integer(), nullable=False),
    sa.Column('office_id', sa.Integer(), nullable=False),
    sa.Column('ticket_number', sa.String(length=50), nullable=False),
    sa.Column('citizen_name', sa.String(length=150), nullable=True),
    sa.Column('citizen_comments', sa.String(length=1000), nullable=True),
    sa.Column('qt_xn_citizen_ind', sa.Integer(), nullable=False),
    sa.Column('cs_id', sa.BigInteger(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['cs_id'], ['citizenstate.cs_id'], ),
    sa.ForeignKeyConstraint(['office_id'], ['office.office_id'], ),
    sa.PrimaryKeyConstraint('citizen_id')
    )
    op.create_table('csr',
    sa.Column('csr_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('office_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('qt_xn_csr_ind', sa.Integer(), nullable=False),
    sa.Column('receptionist_ind', sa.Integer(), nullable=False),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.Column('csr_state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['csr_state_id'], ['csrstate.csr_state_id'], ),
    sa.ForeignKeyConstraint(['office_id'], ['office.office_id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.role_id'], ),
    sa.PrimaryKeyConstraint('csr_id')
    )
    op.create_table('office_service',
    sa.Column('office_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['office_id'], ['office.office_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['service_id'], ['service.service_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('office_id', 'service_id')
    )
    op.create_table('servicereq',
    sa.Column('sr_id', sa.Integer(), nullable=False),
    sa.Column('citizen_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('sr_state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['citizen_id'], ['citizen.citizen_id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.service_id'], ),
    sa.ForeignKeyConstraint(['sr_state_id'], ['srstate.sr_state_id'], ),
    sa.PrimaryKeyConstraint('sr_id')
    )
    op.create_table('period',
    sa.Column('period_id', sa.Integer(), nullable=False),
    sa.Column('sr_id', sa.Integer(), nullable=False),
    sa.Column('csr_id', sa.Integer(), nullable=False),
    sa.Column('reception_csr_ind', sa.Integer(), nullable=False),
    sa.Column('channel_id', sa.Integer(), nullable=False),
    sa.Column('ps_id', sa.Integer(), nullable=False),
    sa.Column('time_start', sa.DateTime(), nullable=False),
    sa.Column('time_end', sa.DateTime(), nullable=True),
    sa.Column('accurate_time_ind', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['channel_id'], ['channel.channel_id'], ),
    sa.ForeignKeyConstraint(['csr_id'], ['csr.csr_id'], ),
    sa.ForeignKeyConstraint(['ps_id'], ['periodstate.ps_id'], ),
    sa.ForeignKeyConstraint(['sr_id'], ['servicereq.sr_id'], ),
    sa.PrimaryKeyConstraint('period_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('period')
    op.drop_table('servicereq')
    op.drop_table('office_service')
    op.drop_table('csr')
    op.drop_table('citizen')
    op.drop_table('service_metadata')
    op.drop_table('role_permission')
    op.drop_table('office')
    op.drop_table('srstate')
    op.drop_table('smartboard')
    op.drop_table('service')
    op.drop_table('role')
    op.drop_table('permission')
    op.drop_table('periodstate')
    op.drop_table('metadata')
    op.drop_table('csrstate')
    op.drop_table('citizenstate')
    op.drop_table('channel')
    # ### end Alembic commands ###
