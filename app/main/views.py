from . import main
from flask import render_template, request, current_app
from ..models import Article, ArticleType, article_types

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.create_time.desc()).paginate(
            page, per_page=current_app.config['ARTICLES_PER_PAGE'],
            error_out=False)
    articles = pagination.items
    return render_template('index.html', ArticleType=ArticleType, article_types=article_types,
                           articles=articles, pagination=pagination, endpoint='.index')


@main.route('/article-detials/<int:id>')
def articleDetails(id):
    article = Article.query.get_or_404(id)
    return render_template('article_detials.html', ArticleType=ArticleType,
                           article_types=article_types, article=article)


@main.route('/article-types/<int:id>/')
def articleTypes(id):
    page = request.args.get('page', 1, type=int)
    pagination = ArticleType.query.get_or_404(id).articles.order_by(
            Article.create_time.desc()).paginate(
            page, per_page=current_app.config['ARTICLES_PER_PAGE'],
            error_out=False)
    articles = pagination.items
    return render_template('index.html', ArticleType=ArticleType, article_types=article_types,
                           articles=articles, pagination=pagination, endpoint='.articleTypes', id=id)