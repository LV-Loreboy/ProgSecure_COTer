import re
from random import choice, random
from string import ascii_letters

def motdepassevalide(motdepasse):
    #le mot de passe doit avoir plus de 6 caractere
    if len(motdepasse) < 6:
        print("Le mot de passe doit être composé de minimum 6 caratères");
        return False
    
    #le mot de passe doit contenir une majuscule
    if not re.search(r'[A-Z]', motdepasse):
        print("Le mot de passe doit contenir au moins une majuscule");
        return False
    
    #le mot de passe doit contenir une minuscule
    if not re.search(r'[a-z]', motdepasse):
        print("Le mot de passe doit contenir au moins une minuscule");
        return False
    
    #le mot de passe doit contenir un chiffre
    if not re.search(r'\d', motdepasse):
        print("Le mot de passe doit contenir au moins un chiffre");
        return False
    
    #le mot de passe doit contenir un symbole
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_-]', motdepasse):
        print("Le mot de passe doit contenir au moins un symbole");
        return False
    
    #Le mot de passe ne doit pas contenir le prenom
    if re.search(re.escape(prenom), motdepasse):
        print("Le mot de passe ne doit pas contenir votre prenom");
        return False
    
    #Le mot de passe ne doit pas contenir le nom
    if re.search(re.escape(nom), motdepasse):
        print("Le mot de passe ne doit pas contenir votre nom");
        return False

    #Le mot de passe est valide
    return True

prenom = input("Entrez votre prenom: ")
nom = input("Entrez votre nom: ")
motdepasse = input("Entrez votre mot de passe: ")
est_valide = motdepassevalide(motdepasse)

if est_valide:
    print("Le mot de passe est valide.")
else:
    print("Le mot de passe n'est pas valide.");
    quit()
    
# -----------------------------------------------------------------
# Le test avec le brute force

# Individu:
    # Un individu n’est rien de plus qu’un résultat. Quand on parle d’un individu en AG, 
    # on parle en réalité d’une instance de la structure de données contenant un résultat, qu’il soit optimum ou non.
    # Dans notre cas, un individu n’est rien d’autre qu’une simple chaîne de caractère.

# Population:
    # Une population n’est rien de plus qu’une collection, un regroupement d’individus.

# Génération:
    # Une génération n’est rien de plus qu’une étape dans l’évolution d’une population. Comme dans la vraie vie.

# Sélection:
    # La phase de sélection est une étape clef dans le fonctionnement des AG. 
    # C’est cette étape qui attribue un score à chaque individu en fonction de son adaptation au problème donné. 
    # Ce score est nommé « fitness » (aptitude pour) et en fonction des scores obtenus par chaque individu de la population, 
    # certains seront conservés pour la génération suivante et d’autres retourneront dans le NEANT.

# Croisement:
    # Le croisement est une étape qui consiste à prendre deux individus différents et de les faire se reproduire pour générer de nouveau individu. 
    # Dans notre cas, le croisement consiste à prendre 50% de la chaîne 1 et 50% de la chaîne 2, pour créer une troisième chaîne de caractères.

# Mutation:
    # La mutation est une étape qui consiste à introduire aléatoire des modifications dans les constituants d’un individu.
    # Dans notre cas, le mutation consiste à modifier un caractère aléatoirement quelque part dans la chaîne de caractères d’un individu. 

# -----------------------------------------------------------------

if est_valide:
    choice = lambda x: x[int(random() * len(x))]
 
 
    # La chance qu'un individu mute (entre 0 et 1)
    CHANCE_DE_MUTATION = 0.1
 
    # La chance qu'un individu ayant le grade le plus HAUT soit retenu pour la prochaine gen (entre 0 et 1)
    POURCENTAGE_DE_HAUTGRADE_RETENU = 0.2
 
    # La chance qu'un individu ayant le grade le plus BAS soit retenu pour la prochaine gen (entre 0 et 1)
    CHANCE_DE_NONGRADE_RETENU = 0.05
 
    POPULATION_ENTIERE = 100
 
    NOMBRE_DE_GENERATIONS_MAX = 100000
 
 
    NOMBRE_DE_HAUTGRADE_RETENU = int(POPULATION_ENTIERE * POURCENTAGE_DE_HAUTGRADE_RETENU)
 
    Longueur_du_motdepasse = len(motdepasse)
 
    Moitie_longueur_motdepasse = Longueur_du_motdepasse // 2
 
    CHARACTERE_VALIDE = ascii_letters + ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ' + ' 0123456789 '
 
    FITNESS_MAX = Longueur_du_motdepasse
    
    LIMITE_BASSE = 3500
    LIMITE_HAUTE = 9500
    LIMITE_SUPER_HAUTE = 18500
 
# ----- AG Code
 
    def donne_char_alea():
        """ Retourne un character alea venant de la liste des characteres valide. """
        return choice(CHARACTERE_VALIDE)
     
 
    def donne_individu_alea():
        """ Crée un nouveau individu. """
        return [donne_char_alea() for _ in range(Longueur_du_motdepasse)]
 
 
    def donne_population_alea():
        """ Create a new random population, made of `POPULATION_ENTIERE` individu. """
        return [donne_individu_alea() for _ in range(POPULATION_ENTIERE)]
 
 
    def donne_fitness_par_individu(individu):
        """ Attribut le fitness a un individu donné. """
        fitness = 0
        for c, expected_c in zip(individu, motdepasse):
            if c == expected_c:
                fitness += 1
        return fitness
 
 
    def grade_moyen_de_la_pop(population):
        """ Retourne le fitness de tous les individu de la pop. """
        total = 0
        for individu in population:
            total += donne_fitness_par_individu(individu)
        return total / POPULATION_ENTIERE
 
 
    def grade_population(population):
        """ Grade la pop, et redonne une liste des individu avec leur fitness, trier du plus au moins grader. """
        individu_grade = []
        for individu in population:
            individu_grade.append((individu, donne_fitness_par_individu(individu)))
        return sorted(individu_grade, key=lambda x: x[1], reverse=True)
 
 
    def fait_evoluer_la_pop(population):
        """ Fait evoluer la propulation pour la prochaine gen. """
 
        # Trie les individu selon leur grade (meilleur en premier), Le grade moyen et la solution (si existe)
        population_nouvelement_grade = grade_population(population)
        grade_moyen = 0
        solution = []
        population_grade = []
        for individu, fitness in population_nouvelement_grade:
            grade_moyen += fitness
            population_grade.append(individu)
            if fitness == FITNESS_MAX:
                solution.append(individu)
        grade_moyen /= POPULATION_ENTIERE
 
        # Termine le scipt quand la solution ets trouver
        if solution:
            return population, grade_moyen, solution    
 
        # Separe les individu les plus haut grade
        parents = population_grade[:NOMBRE_DE_HAUTGRADE_RETENU]

        # Ajoute des individu de maniere alea pour ajouter de la diversiter
        for individu in population_grade[NOMBRE_DE_HAUTGRADE_RETENU:]:
            if random() < CHANCE_DE_NONGRADE_RETENU:
                parents.append(individu)
 
        # Fait muter quelques individu
        for individu in parents:
            if random() < CHANCE_DE_MUTATION:
                partie_a_modifier = int(random() * Longueur_du_motdepasse)
                individu[partie_a_modifier] = donne_char_alea()
 
        # Melange les "parents" pour faire des "Descandants"
        parents_len = len(parents)
        len_voulu = POPULATION_ENTIERE - parents_len
        Descendants = []
        while len(Descendants) < len_voulu:
            pere = choice(parents)
            mere = choice(parents)
            if True: #pere != mere:
                Enfant = pere[:Moitie_longueur_motdepasse] + mere[Moitie_longueur_motdepasse:]
                Descendants.append(Enfant)
 
        # Annonce que la prochaine gen est prete
        parents.extend(Descendants)
        return parents, grade_moyen, solution
 
 
# ----- LE CODE
 
    def main():
        """ Fonction principale. """
 
        # Crée une population et leur atribut des grades de depart
        population = donne_population_alea()
        grade_moyen = grade_moyen_de_la_pop(population)
        print('Grade de départ: %.2f' % grade_moyen, '/ %d' % FITNESS_MAX)
 
        # Fait evoluer la population
        i = 0
        solution = None
        log_avg = []
        while not solution and i < NOMBRE_DE_GENERATIONS_MAX:
            population, grade_moyen, solution = fait_evoluer_la_pop(population)
            if i & 255 == 255:
                print('Grade actuel: %.2f' % grade_moyen, '/ %d' % FITNESS_MAX, '(%d générations)' % i)
            if i & 31 == 31:
                log_avg.append(grade_moyen)
            i += 1
        
        import pygal
        line_chart = pygal.Line(show_dots=False, show_legend=True)
        line_chart.title = f'Tentative de brut force du mot de passe'
        line_chart.x_title = 'Générations'
        line_chart.y_title = 'Distance de la réponse'
        line_chart.add('Fitness', log_avg)
        line_chart.render_to_file('MDP_BFtest.svg')
     
        # Donne les stats de fin
        grade_moyen = grade_moyen_de_la_pop(population)
        print('Grade de fin: %.2f' % grade_moyen, '/ %d' % FITNESS_MAX)
        
        if i <= LIMITE_BASSE:
            print("-[Votre mot de passe n'est pas acceptable]-")
        
        if i > LIMITE_BASSE and i < LIMITE_HAUTE:
            print("-[Votre mot de passe est moyen]-")
   
        if i >= LIMITE_HAUTE and i < LIMITE_SUPER_HAUTE:
            print("-[Votre mot de passe est bien]-")
        
        if i >= LIMITE_SUPER_HAUTE:
            print("-[Votre mot de passe est divin (ou buger)]-")

 
        # Donne la solution dans l'invite de commande
        if solution:
            print('Solution trouvée (%d fois) apres %d générations.' % (len(solution), i))
        else:
            print('Pas de solutions apres %d générations.' % i)
            print('- La derniere pop fut:')
            for number, individu in enumerate(population):
                print(number, '->',  ''.join(individu))
 
 
    if __name__ == '__main__':
        main()