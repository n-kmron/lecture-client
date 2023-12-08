import xmlrpc.client
import sys

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
try:
    common = xmlrpc.client.ServerProxy(
        '{}/xmlrpc/2/common'.format(url))
    print("Version : ", common.version())
except Exception as e:
    print(f"Erreur lors de la récupération de la version d'ODOO : {e}")
    sys.exit(1)

# Connexion de l’utilisateur
try:
    uid = common.authenticate(db, username, password, {})
except Exception as e:
    print(f"Erreur lors de la connexion de l'utilisateur : {e}")
    sys.exit(1)

# Référence à model.Models
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

while True:
    # Vérification des droits d’accès
    has_right = models.execute_kw(db, uid, password,
                                  'esi.book', 'check_access_rights',
                                  ['read'], {'raise_exception': False})
    print("Droit de lecture sur le esi.book : ", has_right)

    # Recherche d'un livre par nom
    search_book_by_name(models, db, uid, password)

    # Demander à l'utilisateur s'il souhaite effectuer une nouvelle recherche
    user_input = input("Voulez-vous effectuer une autre recherche ? (Oui/Non): ").lower()
    if user_input != 'oui':
        break

# https://www.odoo.com/documentation/14.0/fr/developer/reference/external_api.html
