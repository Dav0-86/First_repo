from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://david:123vbnm987@cluster0.ucesb0b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.ds02
collection = db["cats"]

uri = "mongodb+srv://david:123vbnm987@cluster0.ucesb0b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))



def create_cat(name, age, features):
    cat = {"name": name, "age": age, "features": features}
    inserted_cat = collection.insert_one(cat)
    return inserted_cat.inserted_id



def read_all_cats():
    cats = collection.find()
    return [cat for cat in cats]

def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    return cat



def update_age_by_name(name, new_age):
    collection.update_one({"name": name}, {"$set": {"age": new_age}})

def add_feature_by_name(name, new_feature):
    collection.update_one({"name": name}, {"$push": {"features": new_feature}})



def delete_cat_by_name(name):
    collection.delete_one({"name": name})

def delete_all_cats():
    collection.delete_many({})



if __name__ == "__main__":
    
    cat_id = create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    cat_id = create_cat("Myrik", 13, ["ходить в пісок", "кусається", "чорний"])
    cat_id = create_cat("Busik", 7, ["гуляє весь час", "зібсує взуття", "білий"])

    all_cats = read_all_cats()
    print("Усі коти:")
    for cat in all_cats:
        print(cat)

    correct_cat_name_entered = False
    while not correct_cat_name_entered:
        cat_name = input("Введіть ім'я кота: ")
        cat_info = read_cat_by_name(cat_name)
        if cat_info:
            print("Інформація про кота:")
            print(cat_info)
            correct_cat_name_entered = True
        else:
            print("Кіт з таким ім'ям не знайдений.")

    correct_age_entered = False
    while not correct_age_entered:
        try:
            new_age = int(input("Введіть новий вік кота: "))
            if isinstance(new_age, int):
                update_age_by_name(cat_name, new_age)
                print("Вік кота оновлено.")
                correct_age_entered = True
            else:
                print("Введіть цифрами повних років")
        except ValueError:
            print("Ви ввели не коректні дані, повторіть спробу ще раз")

    while True:
        new_feature = input("Введіть нову характеристику кота: ")
        if new_feature.strip():
            add_feature_by_name(cat_name, new_feature)
            print("Нову характеристику додано.")
            break
        else:
            print("Поле не може бути порожнім. Спробуйте ще раз.")



    # delete_cat_by_name(cat_name)
    # print("Кота видалено.")

    # delete_all_cats()
    # print("Усіх котів видалено.")
