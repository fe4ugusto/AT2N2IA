# Trabalho de IA - Detecção de Spam (N2-AT2)

Trabalho prático da matéria **Inteligência Artificial I (N2-AT2)** feito para classificar mensagens de SMS e detectar spam usando Machine Learning.

**Alunos / Integrantes:**
- Felipe Augusto
- Pedro André
- Nicolas

---

## 🔗 Links da Base de Dados Utilizada
A base de dados pode ser acessada e baixada diretamente em qualquer um dos links abaixo:
- **Kaggle:** [https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- **Repositório Oficial UCI Machine Learning:** [https://archive.ics.uci.edu/dataset/228/sms+spam+collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

---

## 📁 Estrutura das Pastas

```
spam-ml-n2-at2/
├── data/
│   └── spam.csv                 # Base de dados (5.169 mensagens limpas - regra de +4.000 atendida)
├── notebooks/
│   └── deteccao_spam.ipynb      # Notebook com código, gráficos e teste prático
├── relatorio/
│   └── relatorio_tecnico.pdf    # Relatório em PDF com todos os links e análises para o AVA
├── demo.py                      # Script para rodar e testar mensagens ao vivo no terminal
├── requirements.txt             # Bibliotecas necessárias
└── README.md                    # Este arquivo com instruções e links
```

---

## 📌 Resumo da Atividade

| Item do Trabalho | Como foi feito | Detalhe |
| :--- | :---: | :--- |
| **Problema escolhido** | Detecção de Spam | Classificação binária de texto (ham vs. spam) |
| **Base com mais de 4.000 registros** | Sim (5.169 válidos) | Base SMS Spam Collection (Kaggle/UCI) com `assert >= 4000` |
| **Links da Base** | Inclusos | Links do Kaggle e UCI colocados no relatório, notebook e README |
| **Análise dos dados (EDA)** | Sim | Gráficos de quantidade de mensagens e tamanho em caracteres |
| **Pré-processamento** | Sim | Limpeza de duplicatas, 0/1 para classes, split 80/20 e TF-IDF |
| **2 Algoritmos implementados** | Naive Bayes e Regressão Logística | Ambos recomendados no edital da disciplina |
| **Avaliação comparativa** | Sim | Acurácia, Precisão, Recall, F1-Score e Matrizes de confusão |
| **Relatório em PDF** | Sim | Com todas as seções pedidas pelo professor e links da base |
| **Demonstração prática** | Sim | Célula no final do notebook e script `demo.py` para testar ao vivo |

---

## 🏆 Resultados Obtidos

| Algoritmo | Acurácia | Precisão (Spam) | Recall (Spam) | F1-Score (Spam) | F1-Score (Macro) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Multinomial Naive Bayes** | **97,58%** | **99,07%** | **81,68%** | **89,54%** | **94,09%** |
| **Regressão Logística** | 95,74% | 98,88% | 67,18% | 80,00% | 88,81% |

- **Falsos positivos:** Apenas **1 erro** em 903 mensagens normais (99% de precisão nos dois).
- **Quem foi melhor:** O **Multinomial Naive Bayes** venceu com folga no Recall (pegou 107 spams contra 88 da Regressão Logística, ou seja, 19 spams a mais), fechando com **F1-Score de 89,54%**.

---

## 💻 Como Rodar

### Opção 1: Demonstração Rápida no Terminal
```powershell
.venv\Scripts\python.exe demo.py
```

### Opção 2: No VS Code (Jupyter Notebook)
Abra o arquivo `notebooks/deteccao_spam.ipynb`, selecione o kernel `.venv` e execute as células.

### Opção 3: No Google Colab
1. Abra o [Google Colab](https://colab.research.google.com/).
2. Faça upload do notebook `notebooks/deteccao_spam.ipynb`.
3. Faça upload do arquivo `data/spam.csv`.
4. Clique em **Ambiente de execução** > **Executar tudo**.
