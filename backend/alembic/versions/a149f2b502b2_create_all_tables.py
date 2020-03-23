"""Create all tables.

Revision ID: a149f2b502b2
Revises: 
Create Date: 2020-01-13 09:32:55.461786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a149f2b502b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('survey_current_location', sa.String(), nullable=True),
    sa.Column('survey_normal_location', sa.String(), nullable=True),
    sa.Column('survey_normal_location_other', sa.String(), nullable=True),
    sa.Column('survey_location_performance', sa.String(), nullable=True),
    sa.Column('survey_applications', sa.String(), nullable=True),
    sa.Column('survey_other_software', sa.String(), nullable=True),
    sa.Column('survey_isp', sa.String(), nullable=True),
    sa.Column('survey_subscribe_download', sa.String(), nullable=True),
    sa.Column('survey_subscribe_upload', sa.String(), nullable=True),
    sa.Column('survey_bundle', sa.String(), nullable=True),
    sa.Column('survey_current_cost', sa.String(), nullable=True),
    sa.Column('survey_partner_org', sa.String(), nullable=True),
    sa.Column('actual_download', sa.Numeric(), nullable=True),
    sa.Column('actual_upload', sa.Numeric(), nullable=True),
    sa.Column('min_rtt', sa.Numeric(), nullable=True),
    sa.Column('latitude', sa.Numeric(), nullable=True),
    sa.Column('longitude', sa.Numeric(), nullable=True),
    sa.Column('bigquery_key', sa.String(), nullable=True),
    sa.Column('client_ip', sa.String(), nullable=True),
    sa.Column('client_city', sa.String(), nullable=True),
    sa.Column('client_region', sa.String(), nullable=True),
    sa.Column('client_country', sa.String(), nullable=True),
    sa.Column('client_ipinfo_loc', sa.String(), nullable=True),
    sa.Column('client_asn', sa.String(), nullable=True),
    sa.Column('client_zipcode', sa.String(), nullable=True),
    sa.Column('client_timezone', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_submission_id'), 'submission', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_submission_survey_phone'), table_name='submission')
    op.drop_index(op.f('ix_submission_survey_email'), table_name='submission')
    op.drop_index(op.f('ix_submission_id'), table_name='submission')
    op.drop_table('submission')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
