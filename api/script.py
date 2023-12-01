import xmlrpc.client

# Paramètres de connexion
url = "http://localhost:8069"
db = "dev01"
# Demander à l'utilisateur de se connecter avec son compte ODOO (pas la db)
username = input("Username: ")
password = input("Password: ")

# Récupération de la version d’ODOO installée
common = xmlrpc.client.ServerProxy(
    '{}/xmlrpc/2/common'.format(url))
print("Version : ", common.version())

# Connexion de l’utilisateur
uid = common.authenticate(db, username, password, {})

# Référence à model.Models
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Vérification des droits d’accès
hasRight = models.execute_kw(db, uid, password,
                             'esi.book', 'check_access_rights',
                             ['read'], {'raise_exception': False})
print("Droit de lecture sur le esi.book : ", hasRight)

books = models.execute_kw(db, uid, password,
                          'esi.book', 'search_read', [[]])

print("Nombre de livres actuellement : ", len(books))

id_created = models.execute_kw(db, uid, password,
                               'esi.book', 'create',
                               [{'name': 'Le livre API', 'description': "Test appel RPC pour un livre"}])
print("Nouveau livre créé via l'API avec l'id : ", id_created)

books = models.execute_kw(db, uid, password,
                          'esi.book', 'search_read', [[]])

for book in books:
    print(" − ID : ", book.get("id"))
    print(" − Nom : ", book.get("name"))
    print(" − Pages : ", book.get("pages"))
    print(" − Date : ", book.get("date_created"))

models.execute_kw(db, uid, password,
                  'esi.book', 'unlink', [[id_created]])
print("Livre supprimé via l'API avec l'id : ", id_created)


#https://www.odoo.com/documentation/14.0/fr/developer/reference/external_api.html
#se connecter alternativement avec la clé d'API