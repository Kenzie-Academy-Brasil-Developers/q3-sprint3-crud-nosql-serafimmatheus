from http import HTTPStatus
from flask import request, jsonify
from app.models.post_class import Post
from app.controllers import posts

def posts_route(app):
    @app.get("/posts")
    def get_posts():
        return jsonify(posts.get_posts_all())

    @app.get("/posts/<id>")
    def get_one_post(id):
        try:
            one_post_id = posts.get_posts_id(int(id))
        except (UnboundLocalError, TypeError):
            return {"error": f"id {id} not found"}, HTTPStatus.NOT_FOUND
        return one_post_id

    
    @app.post("/posts")
    def posts_created():
        data = request.get_json()

        try:
            data_post = Post(**data)
            posts.create_post(data_post)
        except TypeError:
            return {"error": "Check as POST keys"}, HTTPStatus.BAD_REQUEST

        del data_post.__dict__["_id"]

        return data_post.__dict__, HTTPStatus.CREATED

    @app.patch("/posts/<id>")
    def patch_posts(id):
        data = request.get_json()
        data_patch = posts.att_posts(data, int(id))

        if data_patch:
            del data_patch["_id"]
            return data_patch, HTTPStatus.OK
        
        return {"error": f"id {id} not found" }, HTTPStatus.NOT_FOUND



    @app.delete("/posts/<id>")
    def delete_posts_id(id):
        delete = posts.remove_post_id(int(id))
        if delete:
            del delete["_id"]
            return delete, HTTPStatus.OK
        
        return {"error": f"id {id} not found" }, HTTPStatus.NOT_FOUND
