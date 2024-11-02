class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.pontuacao = 0

    def next_question(self):
        questao_atual = self.question_list[self.question_number]
        self.question_number += 1
        resposta = input(f"Q.{self.question_number}: {questao_atual.text}(V ou F)?: ")
        self.check_resposta(resposta, questao_atual.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_resposta(self, answer, questao_correta):
        if answer.upper() == questao_correta:
            self.pontuacao += 1
            print("Resposta correta")
        else:
            print("Erro")
        print(f"A resposta correta era {questao_correta}")
        print(f"Sua pontuação atual {self.pontuacao}/{self.question_number}\n")