from alembic import op
import sqlalchemy as sa
from sqlalchemy import func

# alembic/versions/[your_version_number]_create_advertising_tables.py

from alembic import op
import sqlalchemy as sa


revision = None
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=True),
    )

    op.create_table(
        'advertisers',
        sa.Column('advertiser_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('contact_name', sa.String(255), nullable=True),
        sa.Column('contact_email', sa.String(255), nullable=True),
        sa.Column('contact_phone', sa.String(255), nullable=True),
    )

    op.create_table(
        'ad_campaigns',
        sa.Column('campaign_id', sa.Integer, primary_key=True),
        sa.Column('advertiser_id', sa.Integer, sa.ForeignKey('advertisers.advertiser_id'), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('start_date', sa.Date, nullable=False),
        sa.Column('end_date', sa.Date, nullable=False),
        sa.Column('budget', sa.Numeric(10,2), nullable=False),
    )
    
    op.create_table(
        'ad_groups',
        sa.Column('adgroup_id', sa.Integer, primary_key=True),
        sa.Column('campaign_id', sa.Integer, sa.ForeignKey('ad_campaigns.campaign_id'), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('targeting_criteria', sa.String(255), nullable=False)
    )

    op.create_table(
        'ads',
        sa.Column('ad_id', sa.Integer, primary_key=True),
        sa.Column('adgroup_id', sa.Integer, sa.ForeignKey('ad_groups.adgroup_id'), nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('image_url', sa.String(255), nullable=True),
        sa.Column('destination_url', sa.String(255), nullable=True)
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('advertisers')
    op.drop_table('ad_campaigns')
    op.drop_table('ad_groups')
    op.drop_table('ads')
