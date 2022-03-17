from app.routes.posts import posts_route

def init_app(app):
    posts_route(app)

