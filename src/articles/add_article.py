from flask          import current_app,request,redirect,render_template,url_for
from flask_menu     import current_menu
from flask_security import auth_required
from flask_login    import current_user
from datetime       import datetime
from bleach         import clean,linkify
from wtforms        import Label

from .blueprint     import articles_blueprint

from .models        import Article
from .forms         import articleForm

@articles_blueprint.route('/add',methods = ['GET','POST'])
@auth_required()
def add_article_view():
    article_form = articleForm()
    article_form.submit.label = Label(article_form.submit.id,"Add")
    if request.method == 'POST':
        current_app.logger.info(current_user.username + " sent a new article")
        currentDate              = datetime.now()
        article                  = Article()
        article.title            = clean(request.form['title'])
        article.content          = linkify(clean(request.form['content'],tags={'br','h1','h2','h3','h4','h5','h6','hr','div'},attributes=['class']))
        article.author           = current_user.username
        article.last_modified_by = current_user.username
        article.created          = currentDate.strftime("%Y-%m-%d %H:%M:%S")
        article.last_modified    = currentDate.strftime("%Y-%m-%d %H:%M:%S")
        article.associate_page   = clean(request.form['associate_page'])

        current_app.database.session.add(article)
        current_app.database.session.commit()

        current_app.logger.info("New article posted by " + current_user.username)

        return redirect(url_for('articles.show_articles_view'))
    return render_template('addArticle.html',form=article_form,sectionname="Nuovo articolo",next=request.path)

current_menu.submenu(".articles.add").register(text='Add',external_url=articles_blueprint.url_prefix+"/add",logged_only=True)
