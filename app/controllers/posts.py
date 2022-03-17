from app.models.post_class import Post

def create_post(data_post):
    Post.created_posts(data_post)


def get_posts_all():
    return Post.get_all_posts()


def get_posts_id(id):
    data_one_post = Post.get_one_post_id(id)
    del data_one_post["_id"]
    return data_one_post


def att_posts(data, id):
    data_patch = Post.patch_posts(data, id)
    return data_patch


def remove_post_id(id):
    delete = Post.delete_posts(id)
    return delete

