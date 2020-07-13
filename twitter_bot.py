import random
import tweepy
from time import sleep

api_key = 'YOUR API KEY HERE'
api_secret = 'YOUR API SECRET HERE'
access_token = 'YOUR ACCESS TOKEN HERE'
access_secret = 'YOUR ACCESS SECRET HERE'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def read_last_seen_id():
    with open('last_seen_id.txt', 'r') as f:
        return int(f.read().strip())


def store_last_seen_id(last_id):
    with open('last_seen_id.txt', 'w') as f:
        f.write(str(last_id))


# insert the pick-up lines here
pickup_lines = ['o que eu sinto por vc deve ser motorista, porque passageiro não é rsrs',
                'aposto um beijo que vc me da um fora rs',
                'se tu gosta de açaí se disponibiliza açaí cmg? rsrs',
                'se peidasse num berrante vinha boi até do matogrosso kk',
                'você n é trypanosoma cruzi mas mexe com o meu coração rs',
                'se eu esbarrar numa mesa cheia de docinhos o beijinho rola? kk',
                'me chama de sofá e perde o controle cmg rsrs',
                'eu sei que as coisas não tão fáceis pra vc mas eu to rsrs',
                'q perfume é esse q vc passa e fica com cheiro de amor da minha vida? rs',
                'vi seu nome na margarina ontem, tava escrito “Delícia” rsrs',
                'meu nome é mt grande, melhor vc me chamar de amor kk',
                'a lingua portuguesa é mt complicada eu prefiro a sua rsrs',
                'não confunda ser educado com dar em cima de vc, eu n sou educado kk',
                'ouvi dizer que o bife n gosta de vc, pq o bife é contra filé kkkk',
                'meu médico disse q eu to com ausência de vitamina vc rsrs',
                'saudade do que a gente n viveu ainda rsrs',
                'bom dia razão da minha libido kk',
                'tem um hotel que eu queria muito conhecer esse ano, hotels lábios rs',
                'minha cama perguntou se vc não quer dormir com a gente hj rsrs',
                'não entender matematica ok, mas não entender a química que rola entre nós aí é demais',
                'troquei de operadora agora meu plano é te beijar kk',
                'não quer namorar cmg tudo bem, te faço no the sims e boto a gente pra fazer oba oba kkkk',
                'vou denunciar teus tweets como spam pq to spamtado com tua beleza kk',
                'achei que só a Nestlé fazia tentação mas pelo jeito sua mãe tbm kkkk',
                'vc já cometeu tantos erros na vida, que q custa eu ser mais um? rs',
                'conhece aquela dupla de palhaços? O patati e o passa zap rsrs',
                'bora ver aquele filme juntos, o curioso caso de beijaminha boca rsrs',
                'tô nem sabendo quando é teu aniversário mas tá de parabéns viu rs',
                'vc ta achando q vou correr atrás de vc???? Kkkkkkkk vai com calma pfv  tenho asma',
                'ah pronto, precisa de um bot pra perceber nasceram um pro outro agora',
                'me chama de natal que eu te mostro o que é noite feliz rsrs',
                'olha.. pra virar bombom só falta valsa pq sonho vc já é rsrs']

while True:
    user_id = read_last_seen_id()
    user_mentions = api.mentions_timeline(user_id, tweet_mode='extended')
    try:
        store_last_seen_id(user_mentions[len(user_mentions) - 1].id)
    except IndexError:
        pass
    for mention in user_mentions:
        while True:
            print(f"Found: {mention.full_text} {mention.id}\n")
            try:
                api.update_status(f"@{mention.user.screen_name} "
                                  f"{pickup_lines[random.randint(0, len(pickup_lines) - 1)]}",
                                  mention.id)
            except tweepy.TweepError as error:
                print("Error. Trying again...")
                print(error)
                continue
            else:
                print("Replied.\n")
                break
        sleep(10)
    sleep(20)
