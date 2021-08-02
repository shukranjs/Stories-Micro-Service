"""empty message

Revision ID: 54880faee668
Revises: 
Create Date: 2021-04-14 15:34:14.656590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54880faee668'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=254), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('date_joined', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('bio', sa.TEXT(), nullable=True),
    sa.Column('image', sa.String(length=500), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=120), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('short_description', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_tag_relation',
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_tag_relation')
    op.drop_table('recipe')
    op.drop_table('user')
    op.drop_table('tag')
    op.drop_table('category')
    # ### end Alembic commands ###