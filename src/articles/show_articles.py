from flask      import current_app,render_template,url_for,request
from flask_menu import register_menu

from .blueprint import articles_blueprint
from .utilities import get_articles

@articles_blueprint.route('/articles')
@register_menu(articles_blueprint,'.articles','Articoli',order=1)
def show_articles_view():
    return render_template('articles.html',articles=get_articles(),sectionname="Articoli",next=request.path)
