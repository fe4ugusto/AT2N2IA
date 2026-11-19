# Trabalho de IA - Detecção de Spam (N2-AT2)

Repositório do trabalho prático de **Inteligência Artificial I (Atividade N2-AT2)** desenvolvido pelo nosso grupo.

### 👥 Integrantes:
- Felipe Augusto
- Pedro André
- Nicolas

---

## 📌 O que é esse projeto?
A gente criou um classificador para detectar se mensagens de SMS são normais (**ham**) ou indesejadas/golpes (**spam**), usando Aprendizado de Máquina Supervisionado.

Comparamos dois algoritmos clássicos sugeridos no edital:
1. **Multinomial Naive Bayes** (vencedor, pegou muito mais spams!)
2. **Regressão Logística**

A base usada foi a **SMS Spam Collection** (do Kaggle e UCI), com mais de 5.100 mensagens limpas e sem repetições.

---

## 🔗 Links da Base de Dados
- **Kaggle:** [https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- **Repositório Oficial UCI:** [https://archive.ics.uci.edu/dataset/228/sms+spam+collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

---

## 📁 Onde estão as coisas:
Tudo do trabalho está organizado dentro da pasta `spam-ml-n2-at2/`:

- 📄 **Relatório em PDF para o AVA:** [`spam-ml-n2-at2/relatorio/relatorio_tecnico.pdf`](./spam-ml-n2-at2/relatorio/relatorio_tecnico.pdf)
- 📓 **Notebook com o código e gráficos:** [`spam-ml-n2-at2/notebooks/deteccao_spam.ipynb`](./spam-ml-n2-at2/notebooks/deteccao_spam.ipynb)
- 📊 **Base de dados (.csv):** [`spam-ml-n2-at2/data/spam.csv`](./spam-ml-n2-at2/data/spam.csv)
- 💻 **Script de teste ao vivo no terminal:** [`spam-ml-n2-at2/demo.py`](./spam-ml-n2-at2/demo.py)
- 📦 **Bibliotecas necessárias:** [`spam-ml-n2-at2/requirements.txt`](./spam-ml-n2-at2/requirements.txt)

---

## 🚀 Como rodar

### Opção 1: Teste rápido no terminal
Basta rodar no terminal:
```bash
python spam-ml-n2-at2/demo.py
```
Ele carrega os modelos, testa mensagens de exemplo e deixa você digitar frases para ver a IA respondendo na hora se é HAM ou SPAM.

### Opção 2: Abrir o Notebook no VS Code ou Google Colab
Abra o arquivo `spam-ml-n2-at2/notebooks/deteccao_spam.ipynb` e rode as células para ver todos os gráficos e matrizes de confusão.
