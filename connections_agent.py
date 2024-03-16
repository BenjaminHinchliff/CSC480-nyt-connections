import sys
import time
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from k_means_constrained import KMeansConstrained
from sklearn.metrics.pairwise import euclidean_distances

def user_input():
    valid = False
    user_number = 0
    while not valid:
        print("Choose a connections game (Enter a number from 1 to 228): ", end='')
        try:
            user_str = int(input())
            user_number = int(user_str)
            if 1 <= int(user_str) <= 228:
                user_number = int(user_str)
                valid = True
            else:
                print("Invalid input")
        except:
            print("Invalid input")
    return user_number

def create_word2vec_model():
    print(f"Creating Model")
    word2vec_path = 'GoogleNews-vectors-negative300.bin' # 3 GB file (not included in repo)
    w2v_model = KeyedVectors.load_word2vec_format(word2vec_path, binary=True)
    return w2v_model

def choose_connections_games(game_num=0):
    df = pd.read_csv('connections.csv', names=['word0', 'word1', 'word2', 'word3', 'clue'], keep_default_na=False).iloc[1:]
    df = df[['word0', 'word1', 'word2', 'word3']]
    words_list = df.stack().tolist()
    words_list = [s.lower() for s in words_list]
    game = words_list[game_num*16:game_num*16+16]
    return game

def create_embeddings(w2v_model, game):
    print(f"Creating Embeddings")
    embeddings = []
    for i, word in enumerate(game):
        if word in w2v_model:
            embeddings.append(w2v_model[word])
        else:
            embeddings.append([0 for _ in range(300)])

    np_embeddings = []
    for embedded_word in embeddings:
        np_embeddings.append(np.array(embedded_word))
    
    return np_embeddings


def kmeans_clustering(X, game, num_clusters=4):
    kmeans_cluster = KMeansConstrained(n_clusters=num_clusters, size_min=4, size_max=4)
    cluster_labels = kmeans_cluster.fit_predict(X)

    clusters = {}
    for i, word in enumerate(game):
        cluster_label = cluster_labels[i]
        if cluster_label not in clusters:
            clusters[cluster_label] = []
        clusters[cluster_label].append(word)
    clusters = dict(sorted(clusters.items()))

    return kmeans_cluster, clusters

def find_best_group(kmeans_cluster):
    cluster_centers = kmeans_cluster.cluster_centers_
    inter_cluster_distances = euclidean_distances(cluster_centers)
    avg_inter_cluster_distance = inter_cluster_distances.mean(axis=1)
    best_cluster_index = avg_inter_cluster_distance.argmin()
    return best_cluster_index

def evaluate_group(best_group, game):
    for i in range(0, len(game), 4):
        correct_group = game[i:i+4]
        if best_group == correct_group:
            print("Correct Grouping\n")
            return True
    print("Incorrect Grouping\n")
    return False

def playing_connections(connection_game, word_embeddings, play_all = False):
    print("Agent Playing ...\n")
    attempts = 4
    winner = False
    already_attempted = {}
    while attempts > 0 and not winner:
        print(f"{attempts} Attempts Remaining")
        print(f"Words Remaining: {connection_game}")
        if not play_all:
            time.sleep(4)

        kmeans_cluster, clusters = kmeans_clustering(word_embeddings, connection_game, num_clusters=len(connection_game)//4)
        best_group_number = find_best_group(kmeans_cluster)
        best_group = clusters[best_group_number]
        print(f"Choosing: {best_group}")
        
        if frozenset(best_group) in already_attempted:
            if already_attempted[frozenset(best_group)] > 5:
                print(f"Attempted Too Many Times: Game Over")
                break
            print(f"Attemped {already_attempted[frozenset(best_group)]} Time(s) Already\n")
            already_attempted[frozenset(best_group)] += 1
            continue
        else:
            already_attempted[frozenset(best_group)] = 1

        if evaluate_group(best_group, connection_game):
            index = 0
            for i in range(0, len(connection_game), 4):
                if best_group[0] in connection_game[i:i+4]:
                    index = i
                    break
            if len(connection_game) >= 4 or len(word_embeddings) >= 4:
                del connection_game[index:index+4]
                del word_embeddings[index:index+4]
        else:
            attempts -= 1

        if len(connection_game) == 0 and len(word_embeddings) == 0:
            winner = True
        
    if winner:
        print("Agent Wins!\n")
    else:
        print("Agent Loses\n")

    return (16-len(connection_game))//4

def play_all():
    w2v_model = create_word2vec_model()
    total_games, wins = 0, 0
    for i in range(228):
        connection_game = choose_connections_games(game_num=i)
        word_embeddings = create_embeddings(w2v_model, connection_game)
        groups_correct = playing_connections(connection_game, word_embeddings, play_all=True)
        if groups_correct == 4:
            wins += 1
        total_games += 1

    print("\n\n\n\n\n\n")
    print(f"Total Games Played: {total_games}")
    print(f"Winning Percentage: {wins/total_games}")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'all':
        play_all()
    else:
        user_number = user_input()
        connection_game = choose_connections_games(game_num=user_number-1)
        print(f"Connections Game {user_number}: {connection_game}")
        w2v_model = create_word2vec_model()
        word_embeddings = create_embeddings(w2v_model, connection_game)
        print(f"{playing_connections(connection_game, word_embeddings)} Correct Group(s) Found\n")

    