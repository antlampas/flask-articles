from flask      import current_app,render_template,url_for,request
from flask_menu import MenuNode

from .blueprint import articles_blueprint
from .utilities import get_articles

@articles_blueprint.route('/articles')
def show_articles_view():
    return render_template('articles.html',articles=get_articles(),sectionname="Articoli",next=request.path)

current_app.menu.root().submenu(".articles").register(text='Articles',order=1,external_url=articles_blueprint.url_prefix+"/articles")
