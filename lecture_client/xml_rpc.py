import xmlrpc.client

URL = "http://localhost:8069"
DB = "dev01"
COMMON = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
MODELS = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))


def connect(username, password):
    try:
        uid = COMMON.authenticate(DB, username, password, {})
        print(f"Connexion réussie avec l'uid {uid}")
        return uid
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return False


def check_access_rights(uid, password):
    try:
        return MODELS.execute_kw(DB, uid, password,
                                 'esi.book', 'check_access_rights',
                                 ['read'], {'raise_exception': False})

    except Exception as e:
        print(f"Erreur lors de la vérification des droits d'accès : {e}")
        return False


def search_book_by_name(uid, password, book_name):
    try:
        search_domain = [('name', 'ilike', book_name)]
        return MODELS.execute_kw(DB, uid, password, 'esi.book', 'search_read', [search_domain])
    except Exception as e:
        print(f"Erreur lors de la recherche du livre : {e}")
        return None


def like(uid, password, book_id):
    try:
        return MODELS.execute_kw(DB, uid, password, 'esi.book', 'toggle_like_book', [book_id])
    except Exception as e:
        print(f"Erreur lors de la recherche du livre : {e}")
        return None


def get_users_names_by_ids(uid, password, user_ids):
    try:
        users = MODELS.execute_kw(DB, uid, password, 'res.users', 'read', [user_ids], {'fields': ['name']})
        return [user['name'] for user in users]
    except Exception as e:
        print(f"Error retrieving user names: {e}")
        return []


def get_partner_names_by_ids(uid, password, partner_ids):
    try:
        # Fetch the partner records based on their IDs
        partners = MODELS.execute_kw(DB, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['name']})
        # Extract and return the names from the records
        return [partner['name'] for partner in partners]
    except Exception as e:
        print(f"Error retrieving partner names: {e}")
        return []