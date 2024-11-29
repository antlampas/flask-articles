from flask          import current_app,request,redirect,render_template,url_for
from flask_security import auth_required
from flask_menu     import MenuNode
from flask_login    import current_user
from wtforms        import Label
from bleach         import clean

from .blueprint     import articles_blueprint
from .forms         import chooseArticleForm
from .models        import Article
from .utilities     import populate_form,remove_article

@articles_blueprint.route('/delete',methods = ['GET','POST'])
@auth_required()
def remove_article_view():
    articleForm = chooseArticleForm()
    articleForm.submit.label = Label(articleForm.submit.id,"Remove")
    if request.method == 'POST':
        current_app.logger.info(current_user.username + " is removing " + clean(request.form['title']))
        remove_article(clean(request.form['title']))
        current_app.logger.info(clean(request.form['title']) + " removed by " + current_user.username)
        return redirect(url_for('articles.show_articles_view'))
    populate_form(articleForm,Article,"title")
    return render_template('deleteArticle.html',form=articleForm,sectionname="Rimuovi Articolo",next=request.path)

MenuNode(".articles").register(text='Remove',external_url=articles_blueprint.url_prefix+"/delete",logged_only=True)
