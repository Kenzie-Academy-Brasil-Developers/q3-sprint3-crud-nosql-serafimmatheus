import pymongo
from datetime import datetime as dt

client = pymongo.MongoClient("mongodb://localhost:27017/")
kenzie = client["posts"]


def create_id_posts(list):
    lists_id = []
    for i in list:
        lists_id.append(i["id"])

    if lists_id:
        return lists_id[-1] + 1

    return 1


class Post:

    new_date = dt.now()

    def __init__(self, title: str, author: str, tags: list, content: str):
        self.id = create_id_posts(kenzie.posts.find())
        self.created_at = self.new_date.strftime("%d/%m/%Y %H:%M")
        self.updated_at = self.new_date.strftime("%d/%m/%Y %H:%M")
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content


    @staticmethod
    def get_all_posts():
        all_posts = kenzie.posts.find()

        list_finds = []
        for i in all_posts:
            del i["_id"]
            list_finds.append(i)

        return list_finds


    @staticmethod
    def get_one_post_id(id):
        return kenzie.posts.find_one({"id": id})
    

    def created_posts(self):
        kenzie.posts.insert_one(self.__dict__)


    @staticmethod
    def delete_posts(id):
        delete = kenzie.posts.find_one_and_delete({"id": id})
        return delete


    @staticmethod
    def patch_posts(data, id):
        new_date = dt.now()
        data["updated_at"] = new_date.strftime("%d/%m/%Y %H:%M")
        data_patch = kenzie.posts.find_one_and_update({"id": id}, {"$set": data}, return_document=True)
        return data_patch

        