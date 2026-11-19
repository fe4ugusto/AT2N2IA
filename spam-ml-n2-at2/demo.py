import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

print("=" * 65)
print("  INICIALIZANDO OS ALGORITMOS DE DETECÇÃO DE SPAM (IA)")
print("=" * 65)

# 1. Carregar base de dados
caminho = "data/spam.csv" if os.path.exists("data/spam.csv") else "spam-ml-n2-at2/data/spam.csv"
df = pd.read_csv(caminho, encoding="latin-1")[["v1", "v2"]].rename(columns={"v1": "label", "v2": "text"})
df = df.dropna(subset=["label", "text"]).drop_duplicates(subset=["text"]).copy()
df["target"] = df["label"].map({"ham": 0, "spam": 1})

print(f"Base carregada com sucesso! Total de mensagens: {len(df)}")
print("Treinando Multinomial Naive Bayes e Regressão Logística...")

# 2. Divisão e TF-IDF
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["target"], test_size=0.2, random_state=42, stratify=df["target"])
vectorizer = TfidfVectorizer(lowercase=True, stop_words="english", max_features=5000, ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(X_train)

# 3. Treinar modelos
nb = MultinomialNB(alpha=0.5).fit(X_train_tfidf, y_train)
lr = LogisticRegression(max_iter=1000, random_state=42).fit(X_train_tfidf, y_train)

print(" Modelos treinados e prontos para teste!\n")

def classificar(texto):
    vetor = vectorizer.transform([texto])
    
    pred_nb = nb.predict(vetor)[0]
    prob_nb = nb.predict_proba(vetor)[0][pred_nb] * 100
    res_nb = "🚨 SPAM (Suspeito)" if pred_nb == 1 else "✅ HAM (Mensagem Legítima)"
    
    pred_lr = lr.predict(vetor)[0]
    prob_lr = lr.predict_proba(vetor)[0][pred_lr] * 100
    res_lr = "🚨 SPAM (Suspeito)" if pred_lr == 1 else "✅ HAM (Mensagem Legítima)"
    
    print("-" * 65)
    print(f"Mensagem: \"{texto}\"")
    print(f"-> Multinomial Naive Bayes : {res_nb} [Confiança: {prob_nb:.1f}%]")
    print(f"-> Regressão Logística    : {res_lr} [Confiança: {prob_lr:.1f}%]")
    print("-" * 65)

# Testes automáticos demonstrativos
exemplos = [
    "Hey friend, are we still having pizza tonight?",
    "CONGRATULATIONS! You won a $1000 Walmart Gift Card! Click here to claim now!",
    "Can you email me the homework assignment before 5pm?",
    "URGENT: Your bank account is locked. Text YES to 88202 to unlock immediately."
]

print(">>> TESTANDO EXEMPLOS AUTOMÁTICOS:\n")
for ex in exemplos:
    classificar(ex)

print("\n" + "=" * 65)
print("Você pode testar qualquer mensagem nova agora!")
print("(Digite uma mensagem em inglês ou pressione ENTER sem nada para sair)")
print("=" * 65)

try:
    while True:
        entrada = input("\nDigite uma frase para testar: ").strip()
        if not entrada:
            print("Encerrando demonstração. Até mais!")
            break
        classificar(entrada)
except (KeyboardInterrupt, EOFError):
    print("\nEncerrando demonstração.")
