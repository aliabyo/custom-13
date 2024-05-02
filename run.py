from flask import Flask
from threading import Thread
from highrise import Position
from highrise.__main__ import *
from highrise.__main__ import *
import time
import traceback
import time
from highrise.models import (
    Item,
    Position,
    Reaction,
    SessionMetadata,
    User,
    AnchorPosition,
    CurrencyItem ,
)

class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Alive"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()


class RunBot():
   

  room_id = "65ffe8b0b9d5dbdcab71eaeb"
  bot_token = "695bd3c4fed5124df2aea952ddda526c3a2c0b9410fff68b92e4e9f7269ac490"
  bot_file = "main"
  bot_class = "MyBot"

  def __init__(self) -> None:
    self.definitions = [
        BotDefinition(
            getattr(import_module(self.bot_file), self.bot_class)(),
            self.room_id, self.bot_token)
    ]  # More BotDefinition classes can be added to the definitions list

  def run_loop(self) -> None:
    while True:
      try:
        arun(main(self.definitions))
        
      except Exception as e:
        # Print the full traceback for the exception
        import traceback
        print("Caught an exception:")
        traceback.print_exc()  # This will print the full traceback
        time.sleep(1)
        continue
    

if __name__ == "__main__":
  WebServer().keep_alive()

  RunBot().run_loop()
