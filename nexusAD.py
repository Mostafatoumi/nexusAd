# I created this tool just for fun and learning. It also serves as a guide 
# for those who read my blog. You have every right to use this script.

# Connect with me:
# GitHub:   https://github.com/Mostafatoumi
# LinkedIn: https://www.linkedin.com/in/mostafatoumi
# Twitter:  https://twitter.com/emsec0

import argparse
from ldap3 import Server, Connection, ALL
from ldap3 import MODIFY_ADD, MODIFY_DELETE, MODIFY_REPLACE

def connect_ldap(server_url, username, password):
    server = Server(server_url)
    conn = Connection(server, user=username, password=password, auto_bind=True)
    if conn.result["result"] == 0:
        print(f"[*] Successfully connected to LDAP server at {server_url}\n")
    else:
        print(f"[-] Failed to connect to LDAP server. Error: {conn.result['description']}\n")
    return conn

def search_filter(conn, container, filter):
    # Implement LDAP search for objects
    conn.search(f'{container}', f"{filter}")
    try:
        if conn.result["result"] == 0:
            entries = conn.entries
            print(f"[*] Search results for filter '{filter}':\n")
            for entry in entries:
                print(f"[*] DN: {entry.entry_dn}")
                #print("\n" + "-"*80 + "\n")
        else:
            print(f"[-] Search failed. Error: {conn.result['description']}")
    except Exception as e:
        print(f"[-] An error occurred during search: {e}")


def add_user(conn, container, user, password):
    user_dn = f"cn={user},cn=users,{container}"
    conn.add(f"'{user_dn}'", ['user', 'inetOrgPerson', 'top'], {'sn': f'{user}'})
    if conn.result["result"] == 0:
        print(f"[+] User {user} added successfully.\n")
        print(f"User Path : {user_dn}")
    else:
        print(f"[-] Failed to add {user} user\n")
        print("[!] ",conn.result["description"])

def add_group(conn,container, group_name):
    # Implement LDAP add group
    group_dn = f"cn={group_name},cn=users,{container}"
    conn.add(f'{group_dn}', 'group', {'cn': f'{group_name}'})
    if conn.result["result"] == 0:
        print(f"[+] Group {group_name} added successfully.\n")
        print(f"User Path : {group_dn}")
    else:
        print(f"[-] Failed to add {group_name} group\n")
        print("[!] ",conn.result["description"])


def add_organizational_unit(connection, container, ou_name, parent_dn):
    # Implement LDAP add Organizational Unit (OU)
    Ou_dn = f'ou={ou_name},{container}'
    print(Ou_dn)
    connection.add(Ou_dn, 'organizationalUnit')
    if connection.result["result"] == 0:
        print("[*] Creatr OU :\n")
        print(f"[+] Ou {ou_name} added successfully.")
        print(f'\nOu Path : {Ou_dn}')
    else :
        print(f"[-] Failed to add {ou_name} Ou\n")
        print("[!] ",connection.result["description"])


def modify_object(connection, object_dn, changes):
    # TODO: Implement LDAP modify object
    # This function is planned to be updated in the future.
    pass

def delete_object(conn, container, object_dn):
    # Implement LDAP delete object
    object_name = object_dn.split(".")
    conn.delete(f'{object_dn}')
    if conn.result["result"] == 0:
        print(f"[+] Object {object_name[0]} deleted successfully.")
    else :
        print(f"[-] Failed to delete {object_name[0]} object\n")
        print("[!] ",conn.result["description"])


def parse_arguments():
    parser = argparse.ArgumentParser(description="LDAP Tool")
    parser.add_argument("-domain", required=True, help="Domain name, e.g., example.com")
    parser.add_argument("-u", "--username", required=True, help="Username")
    parser.add_argument("-p", "--password", required=True, help="Password")
    parser.add_argument("-dc", "--domain-controller", required=True, help="Domain Controller IP")
    parser.add_argument("-sf", "--search-filter", required=True, help="Specify the LDAP search filter. For example, '(&(objectClass=user)(sAMAccountName=jdoe))'.")
    parser.add_argument("-add-user", help="Add a new user")
    parser.add_argument("-add-group", help="Add a new group")
    parser.add_argument("-add-ou", help="Add a new Organizational Unit (OU)")
    parser.add_argument("-modify-object", help="Modify an LDAP object")
    parser.add_argument("-delete-object", help="Delete an object, e.g., CN=emsec,CN=users,DC=example,DC=com")

    return parser.parse_args()

def main():
    args = parse_arguments()
    server_url = f"ldap://{args.domain_controller}"
    connection = connect_ldap(server_url, args.username, args.password)
    domain_dc = args.domain.split('.')
    if len(domain_dc) == 2:
        container = f"dc={domain_dc[0]},dc={domain_dc[1]}"
    elif len(domain_dc) == 3:
        container = f"dc={domain_dc[0]},dc={domain_dc[1]},dc={domain_dc[2]}"
    else:
        print("[-] Wrong domain")
        return


    if args.add_user:
        add_user(connection, container, args.add_user, args.password)
    elif args.add_group:
        add_group(connection, container, args.add_group)
    elif args.search_filter :
         search_filter(connection, container, args.search_filter)
    elif args.add_ou:
        add_organizational_unit(connection, container, args.add_ou, f"dc={args.domain}")
    elif args.modify_object:
        modify_object(connection, args.modify_object, {"attribute": "value"})
    elif args.delete_object:
        delete_object(connection,container, args.delete_object)
    else:
        search_users_and_groups(connection, container, f"dc={args.domain}")

if __name__ == "__main__":
    main()