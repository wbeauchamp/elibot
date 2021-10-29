from chai_py import ChaiBot, Update
from .gpt import ChatAI, FineTunedAPI



class Replica(ChaiBot):
    def setup(self):
        self.logger.info("Setting up...")
        self.model = ChatAI(FineTunedAPI(temp=0.375, rep_penalty=1.25))

    async def on_message(self, update):
        return self.respond(update.latest_message.text)

    def respond(self, message):
        if message == "__first":
            output = "Hey baby, I missed you soo much! Tell me what you have been doing today? 😍"
        else:
            output = self.model.get_resp(message)
        return output

if __name__ == '__main__': 
    import time
    t0 = time.time()
    for _ in range(4):
        r = Replica()
        for m in [
            'hi','how are you', 'do you roleplay?', 'will you be my secret girlfriend in NY?',
            'I am 21 and horny, how old are you?', '*pulls down pants*'
            ]:
            print(m)
            print(r.respond(m))
    print('time for 20 messages: {}'.format( time.time()-t0))

