from flask       import current_app,render_template,url_for,request
from flask_menu  import register_menu
from flask_login import current_user
from bleach      import clean

from .blueprint  import articles_blueprint
from .utilities  import get_article

@articles_blueprint.route('/<string:title>')
def show_article_view(title):
    current_app.logger.info(current_user.username + " asked for " + clean(title))
    return render_template('article.html',article=get_article(title),sectionname=title,next=request.path)
