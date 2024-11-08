import os

# Remplacer par vos valeurs réelles de "bad" et "good" commits
bad_commit_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"  # Remplacer par le commit contenant le bug
good_commit_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"  # Remplacer par un commit stable

# Commencer le bisect
os.system(f"git bisect start {bad_commit_hash} {good_commit_hash}")

# Spécifier la commande pour tester si un commit contient le bug
# Ici, on utilise `python manage.py test` pour exécuter les tests Django
# Assurez-vous que cette commande renvoie 0 pour les commits bons et 1 pour les commits mauvais
result = os.system("git bisect run python manage.py test")
if result == 0:
    print("Le commit défectueux a été trouvé.")
else:
    print("Erreur lors de l'exécution de git bisect.")

# Terminer le bisect après avoir trouvé le commit coupable
os.system("git bisect reset")
