# Roadmap

## Fonctionnalités à ajouter

1. **Tests Unitaires et d'Intégration**
    - Écrire des tests unitaires pour chaque fonction de la classe `RPNCalculator`.
    - Écrire des tests d'intégration pour tous les endpoints de l'API.
    - Utiliser des outils comme `pytest` et `httpx` pour les tests.
2. **Sécurité**
    - Implémenter l'authentification et l'autorisation pour sécuriser les endpoints de l'API.
    - Utiliser OAuth2 ou JWT pour gérer les accès sécurisés.

4. **Persistances des Données**
    - Intégrer une base de données (SQL comme PostgreSQL ou NoSQL comme MongoDB) pour persister les piles de calcul.
    - Utiliser des ORM comme SQLAlchemy pour les bases de données SQL ou Motor pour MongoDB.

5. **Interface Utilisateur (UI)**
    - Développer une interface utilisateur pour la calculatrice RPN en utilisant un framework JavaScript moderne comme React ou Vue.js.
    - Intégrer cette UI avec l'API FastAPI pour offrir une expérience utilisateur complète.

6. **Amélioration des Performances**
    - Optimiser les performances de l'application en identifiant et en éliminant les goulets d'étranglement.
    - Utiliser des outils de profilage pour analyser les performances du code.

7. **Support des Opérations Avancées**
    - Ajouter des opérations mathématiques avancées telles que la puissance, la racine carrée, le logarithme, etc.
    - Implémenter des fonctions de manipulation de piles comme l'inversion de la pile, la duplication des éléments, etc.

8. **Déploiement et CI/CD**
    - Mettre en place une pipeline de CI/CD pour automatiser les tests et le déploiement de l'application.
    - Utiliser des outils comme GitHub Actions, Travis CI, ou Jenkins pour les pipelines de CI/CD.
    - Déployer l'application sur des plateformes cloud comme AWS, Azure, ou Heroku.
    - Créer des conteneurs Docker pour faciliter le déploiement.

9. **Logs et Monitoring**
    - Ajouter des systèmes de logging pour surveiller l'état de l'application et déboguer les problèmes.
    - Intégrer des outils de monitoring pour suivre les performances et la disponibilité de l'application.

10. **Internationalisation et Localisation**
    - Ajouter le support pour plusieurs langues afin de rendre l'application accessible à un public mondial.
    - Utiliser des bibliothèques comme `gettext` pour gérer les traductions.

## Priorités

1. **Court Terme (1-2 semaines)**
    - Écrire des tests unitaires de base.
    - Ajouter une documentation initiale avec des docstrings.
    - Implémenter une base de données pour la persistance des piles.

2. **Moyen Terme (1-2 mois)**
    - Développer une interface utilisateur de base.
    - Implémenter l'authentification et l'autorisation.
    - Ajouter des opérations mathématiques avancées.

3. **Long Terme (3-6 mois)**
    - Optimiser les performances de l'application.
    - Mettre en place une pipeline de CI/CD complète.
    - Déployer l'application sur une plateforme cloud.
    - Ajouter le support pour plusieurs langues.