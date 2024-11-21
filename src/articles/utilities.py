from flask      import current_app
from .blueprint import articles_blueprint
from .models    import Article

def get_articles():
    articles = current_app.database.session.execute(current_app.database.select(Article)).scalars()
    return articles

def get_article(title=None):
    article = current_app.database.one_or_404(current_app.database.select(Article).filter_by(title=title))
    return article

def populate_form(form,model,field):
    items = current_app.database.paginate(current_app.database.select(model))
    getattr(form,field).choices = [getattr(item,field) for item in items]
    return form

def remove_article(title):
    article       = Article()
    article.title = title
    Article.query.filter_by(title=article.title).delete()
    current_app.database.session.commit()

def assigned_article(page):
    articles = current_app.database.session.execute(current_app.database.select(Article)).scalars()
    for article in articles:
        if article.associate_page == page:
            return article.title,article.content
    return "",""
