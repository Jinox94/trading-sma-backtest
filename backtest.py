import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def main():
    ticker = "AAPL"
    start = "2018-01-01"

    # Télécharger les données
    df = yf.download(ticker, start=start, auto_adjust=True, progress=False)
    df = df[["Close"]].rename(columns={"Close": "price"}).dropna()

    # Moyennes mobiles
    df["SMA_20"] = df["price"].rolling(20).mean()
    df["SMA_50"] = df["price"].rolling(50).mean()

    # Signal : 1 si SMA 20 > SMA 50, sinon 0
    df["Signal"] = 0
    df.loc[df["SMA_20"] > df["SMA_50"], "Signal"] = 1

    # Position : on prend le signal de la veille
    df["Position"] = df["Signal"].shift(1).fillna(0)

    # Détection des achats / ventes
    df["Trade"] = df["Position"].diff()

    achats = df[df["Trade"] == 1]
    ventes = df[df["Trade"] == -1]

    # Rendement journalier de l'action
    df["Rendement_Action"] = df["price"].pct_change().fillna(0)

    # Rendement de la stratégie
    df["Rendement_Strategie"] = df["Position"] * df["Rendement_Action"]

    # Performance cumulée
    df["Capital_Action"] = (1 + df["Rendement_Action"]).cumprod()
    df["Capital_Strategie"] = (1 + df["Rendement_Strategie"]).cumprod()

    # Résultats finaux
    perf_action = (df["Capital_Action"].iloc[-1] - 1) * 100
    perf_strat = (df["Capital_Strategie"].iloc[-1] - 1) * 100

    print("Performance finale Buy & Hold : {:.2f}%".format(perf_action))
    print("Performance finale Stratégie SMA : {:.2f}%".format(perf_strat))
    print("Nombre d'achats :", len(achats))
    print("Nombre de ventes :", len(ventes))

    # Graphique 1 : prix + moyennes mobiles + signaux
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df["price"], label="Prix")
    plt.plot(df.index, df["SMA_20"], label="SMA 20")
    plt.plot(df.index, df["SMA_50"], label="SMA 50")

    plt.scatter(achats.index, achats["price"],
                label="Achat",
                marker="^",
                s=180,
                color="green",
                edgecolors="black")

    plt.scatter(ventes.index, ventes["price"],
                label="Vente",
                marker="v",
                s=180,
                color="red",
                edgecolors="black")

    plt.title("Stratégie Moyennes Mobiles - AAPL")
    plt.xlabel("Date")
    plt.ylabel("Prix")
    plt.legend()
    plt.grid()
    plt.show()

    # Graphique 2 : comparaison des performances
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df["Capital_Action"], label="Buy & Hold")
    plt.plot(df.index, df["Capital_Strategie"], label="Stratégie SMA")

    plt.title("Comparaison des performances")
    plt.xlabel("Date")
    plt.ylabel("Capital cumulé")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()