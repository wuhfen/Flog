"""add image caption

Revision ID: 3906667d18c9
Revises: 6324574ac773
Create Date: 2020-03-07 22:22:31.203337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3906667d18c9'
down_revision = '6324574ac773'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image_caption', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'image_caption')
    # ### end Alembic commands ###
