Backtest d'une stratégie de moyennes mobiles en Python sur données boursières (yfinance)
# Trading SMA Backtest

## Présentation

Ce projet consiste à développer un outil de backtest en Python permettant d’évaluer une stratégie de trading basée sur le croisement de moyennes mobiles (SMA 20 / SMA 50).
L’objectif est de comparer cette stratégie à une approche passive de type "Buy & Hold" sur l’action Apple (AAPL).

## Démarche

- Récupération de données boursières via yfinance
- Calcul des moyennes mobiles (20 jours / 50 jours)
- Génération de signaux d’achat et de vente
- Simulation d’une stratégie d’investissement
- Comparaison avec une stratégie passive

## Résultats

Le backtest montre que :
- La stratégie SMA génère de nombreux signaux (achats/ventes)
- Elle permet parfois d’éviter certaines baisses
- Mais elle sous-performe globalement une stratégie Buy & Hold sur la période étudiée

Il met en évidence les limites des indicateurs techniques simples.

## Technologies utilisées

- Python
- pandas
- matplotlib
- yfinance

## Lancer le projet

python backtest.py
