"""type annotation

Revision ID: 2a4cf43c1e8d
Revises: 1273c337bb94
Create Date: 2023-05-07 01:20:04.511244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a4cf43c1e8d'
down_revision = '1273c337bb94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # with op.batch_alter_table('characters', schema=None) as batch_op:
    #     batch_op.add_column(sa.Column('titles', sa.ARRAY(sa.String(length=64)), nullable=True))
    #     batch_op.add_column(sa.Column('aliases', sa.ARRAY(sa.String(length=64)), nullable=True))
    #     batch_op.add_column(sa.Column('playedBy', sa.ARRAY(sa.String(length=64)), nullable=True))

    """
    add the following columns to the characters table:
    titles: Mapped[list[str]] = db.Column(db.JSON)
    aliases: Mapped[list[str]] = db.Column(db.JSON)
    playedBy: Mapped[list[str]] = db.Column(db.JSON)
    """
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('titles', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('aliases', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('playedBy', sa.JSON(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_column('playedBy')
        batch_op.drop_column('aliases')
        batch_op.drop_column('titles')

    # ### end Alembic commands ###