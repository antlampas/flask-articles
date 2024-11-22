from flask      import current_app,render_template,url_for,request
from flask_menu import current_menu

from .blueprint import articles_blueprint
from .utilities import get_articles

@articles_blueprint.route('/articles')
def show_articles_view():
    return render_template('articles.html',articles=get_articles(),sectionname="Articoli",next=request.path)

current_menu.register(show_articles_view,'Articoli',order=1)
