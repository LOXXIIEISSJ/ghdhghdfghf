"""empty message

Revision ID: b45942373176
Revises: 3b178783a880
Create Date: 2022-12-31 18:46:53.982020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b45942373176'
down_revision = '3b178783a880'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comment', 'comment', ['reply_to_comment'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    # ### end Alembic commands ###
