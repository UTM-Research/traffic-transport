import matplotlib.pyplot as plt
def shape(Positive,Negative,Neutral):
    energy=[]
    energy.append(Positive)
    energy.append(Negative)
    energy.append(Neutral)
    plt.style.use('ggplot')
    x = ['Positive', 'Negative', 'Neutral']
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, energy, color='green')
    plt.xlabel("Sentiment polarity")
    plt.ylabel("Sentiment score")
    plt.title("Students feedback on Teachers")
    plt.xticks(x_pos, x)
    plt.show()