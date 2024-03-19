Team Members: Aarav Sharma, Benjamin Hinchliff, Nathan Ip, Brian Bivinetto

Acknowledgement:
- Cal Poly CSC 480 Project
- Professor/Instructor: Rodrigo Canaan

External Sources:
- K-means Constrained: 
    - https://joshlk.github.io/k-means-constrained/
    - https://github.com/joshlk/k-means-constrained
- GLoVE
    - https://nlp.stanford.edu/projects/glove/
    - https://github.com/stanfordnlp/GloVe
- Word2Vec
    - https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html
    - https://towardsdatascience.com/introduction-to-word-embedding-and-word2vec-652d0c2060fa

Dependencies:
- Installation: `pip3 install -r requirements.txt`
- Primary Dependencies
    - numpy
    - pandas
    - sklearn
    - k_means_constrained
    - gensim
    - matplotlib
    - jupyter

Running Code:
- To choose and play one game: `python3 connections_agent.py`
    - Agent plays the Connections game and either wins or loses
    - Agent usually wins when playing Connections Game #41 
    - Agent usually loses when playing Connections Game #1
- To play all games: `python3 connections_agent.py all`
    - Agent plays all the Connections games
    - Results: Total number of games played and win rate is shown at the end

Notebooks:
- `glove.ipynb`
    - Uses GloVe for word embeddings
- `word2vec.ipynb`
    - Uses Word2Vec for word embeddings

Results/Visualizations
- Results in the visualization folder
- Running the corresponding notebook will create these visualizations of the results
- `word2vec.ipynb`
    - word2vec-cluster-visualization
    - word2vec-group-accuracies
    - word2vec-silhouette-scores
    - word2vec-summary-statistics
- `glove.ipynb`
    - glove-cluster-visualization
    - glove-group-accuracies
    - glove-silhouette-scores
    - glove-summary-statistics
- Running the agent (in the running code section) will allow you to play the Connections games

Files Needed:
- Connections Game Files:
    - `connection-archive.txt` (Raw text format of all Connections games)
    - `connections.csv` (CSV format of all Connections games)
- Pre-trained Embedding Files (Not in GitHub Repo - Too Large)
    - Word2Vec File
        - (Impossible to automate)
        - `GoogleNew-vectors-negative300.bin` (pre-trained Google News corpus embedding model containing 3 million 300-dimension English word vectors)
        - Link: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g
    - GloVe File
        - `./get-glove.sh`
        - `glove.840B.300d.txt`
        - Link: https://huggingface.co/stanfordnlp/glove/resolve/main/glove.840B.300d.zip
