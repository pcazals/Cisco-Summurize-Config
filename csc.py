import tabulate

def lire_configuration(fichier):
    with open(fichier, 'r') as f:
        contenu = f.read()
    return contenu

def extraire_interfaces(contenu):
    interfaces = {}
    lignes = contenu.splitlines()
    interface_nom = None
    for ligne in lignes:
        if ligne.startswith('interface'):
            interface_nom = ligne.split()[1]
            interfaces[interface_nom] = []
        elif interface_nom and ligne.strip():
            interfaces[interface_nom].append(ligne.strip())
    return interfaces

def regrouper_interfaces(interfaces):
    config_group = {}
    for interface, config in interfaces.items():
        config_tuple = tuple(config)  # Convertit la liste en tuple pour la rendre hashable
        if config_tuple not in config_group:
            config_group[config_tuple] = []
        config_group[config_tuple].append(interface)
    return config_group

def afficher_groupes(config_group):
    table = []
    for config, group in config_group.items():
        # Ajouter une ligne pour chaque groupe d'interfaces
        table.append(["\n".join(group), "\n".join(config)])
    # Utiliser tabulate pour afficher le tableau
    print(tabulate.tabulate(table, headers=['Interfaces', 'Configuration'], tablefmt='grid'))

def main():
    chemin_fichier = 'TDL.txt'  # Adaptez ce chemin au fichier de configuration réel
    contenu = lire_configuration(chemin_fichier)
    interfaces = extraire_interfaces(contenu)
    groupes = regrouper_interfaces(interfaces)
    afficher_groupes(groupes)

if __name__ == '__main__':
    main()
