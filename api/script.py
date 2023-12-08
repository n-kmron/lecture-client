import xmlrpc.client

def search_book_by_name(models, db, uid, password):
    # Demander à l'utilisateur le nom du livre à rechercher
    book_name = input("Entrez le nom du livre (titre) à rechercher : ")

    # Recherche des livres avec le nom spécifié
    search_domain = [('name', 'ilike', book_name)]
    books = models.execute_kw(db, uid, password,
                              'esi.book', 'search_read', [search_domain])

    # Afficher les résultats de la recherche
    if books:
        print(f"Résultats de la recherche pour '{book_name}':")
        for book in books:
            print(" − ID : ", book.get("id"))
            print(" − Nom : ", book.get("name"))
            print(" − Pages : ", book.get("pages"))
            print(" − Date de création : ", book.get("date_created"))
    else:
        print("Aucun livre trouvé avec le nom '{book_name}'.")

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
