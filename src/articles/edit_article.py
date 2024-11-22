from flask          import current_app,request,redirect,render_template,url_for
from flask_security import auth_required
from flask_login    import current_user
from wtforms        import Label
from datetime       import datetime
from bleach         import clean,linkify

from .blueprint     import articles_blueprint
from .models        import Article
from .forms         import articleForm

@articles_blueprint.route('/edit',methods = ['GET','POST'])
@auth_required()
def edit_article():
    if request.method == 'POST':
        current_app.logger.info(current_user.username + " is editing " + clean(request.form['title']))
        article_form = articleForm()
        currentDate  = datetime.now()

        article = current_app.database.session.execute(current_app.database.select(Article).filter_by(title=request.args['title'])).scalar_one()

        article.title            = clean(request.form['title'])
        article.content          = linkify(clean(request.form['content'],tags={'br','h1','h2','h3','h4','h5','h6','hr','div'},attributes=['class']))
        article.last_modified    = currentDate.strftime("%Y-%m-%d %H:%M:%S")
        article.last_modified_by = current_user.username
        current_app.database.session.commit()

        current_app.logger.info(clean(request.form['title']) + " edited by " + current_user.username)

        return redirect(url_for('articles.show_articles_view'))
    elif 'title' in request.args.keys():
        article = current_app.database.session.execute(current_app.database.select(Article).filter_by(title=request.args['title'])).scalar_one()

        article_form                     = articleForm()
        article_form.submit.label        = Label(article_form.submit.id,"Edit")
        article_form.title.data          = article.title
        article_form.content.data        = article.content
        article_form.associate_page.data = article.associate_page

        return render_template('editArticle.html',form=article_form,sectionname="Article",next=request.path)
    else:
        article_form               = forms.chooseArticleForm()
        article_form.submit.label  = Label(article_form.submit.id,"Choose")
        articles                   = current_app.database.paginate(current_app.database.select(Article))
        article_form.title.choices = [article.title for article in articles]

        return render_template('chooseArticle.html',form=article_form,sectionname="Article",next=request.path)
