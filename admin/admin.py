from sqladmin import ModelView , Admin
from db.model import Post
from main import app
from db.engine import ENGINE

admin = Admin(app=app,engine=ENGINE)

class PostAdmin(ModelView,model=Post):
    column_list = [Post.id,Post.title,Post.category,Post.description]
admin.add_view(PostAdmin)

