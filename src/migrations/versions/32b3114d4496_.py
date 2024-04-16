"""empty message

Revision ID: 32b3114d4496
Revises: 18d96f584d7d
Create Date: 2024-04-06 17:01:18.169867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32b3114d4496'
down_revision = '18d96f584d7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('connection', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['user2'], ['email'])
        batch_op.create_foreign_key(None, 'user', ['user1'], ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('connection', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###