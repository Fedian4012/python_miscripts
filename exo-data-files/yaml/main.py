import yaml
import os


def ligne_separation(caractere):
    print(f"{caractere}" * 30)

def get_file_directory(file_path):
    return os.path.dirname(os.path.abspath(file_path))


exec_dir = get_file_directory(__file__)

with open(f"{exec_dir}/data.yml", "r") as input:
    data = yaml.safe_load(input)

nom = data['profile']['username']
age = data['profile']['age']
last_post = data['profile']['posts'][-1]

ligne_separation("-")

print(f"Nom : {nom}")
print(f"Âge : {age}")

ligne_separation("-")

print("Dernier post : ")
print(f"  ID : {last_post['post_id']}")
print(f"  Date : {last_post['date']}")
print(f"  Contenu : \"{last_post['content']}\"")
print(f"  Nombre de likes : {last_post['likes']}")

ligne_separation("-")

new_post = {
    'post_id': 'P1003',
    'date': '2025-03-08',
    'content': 'Everybody in this country should learn to program a computer, because it teaches you how to think.',
    'likes': '33'
}

data['profile']['posts'].append(new_post)

with open(f"{exec_dir}/result.yml", "w") as output:
    yaml.dump(data, output)
print("Nouveau post enregistré avec succès !")
ligne_separation("-")
