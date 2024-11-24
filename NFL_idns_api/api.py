import websocket
import threading
import time
import json


class NflIdnsLoader:
    msgText = ""
    userName = ""
    isinited = False

    def __init__(self, name, group, country, lastMessageId, userAgent):
        self.ws = None
        self.name = name
        self.group = group
        self.country = country
        self.lastMessageId = lastMessageId
        self.userAgent = userAgent

    def __processMessage(self, Message: str):
        msgData = json.loads(Message)
        if msgData["type"] == "message":
            self.userName = msgData["message"]["name"]
            self.msgText = msgData["message"]["text"]
            self.msgProperties = msgData["message"]["type"]
            if self.msgProperties == "received":
                self.respondMsg(self.msgText)
            print(f"{self.userName}: {self.msgText}")
        elif msgData["type"] == "command":
            self.__detectStatus(msgData)

    def __detectStatus(self, cmdData: dict):
        if cmdData["name"] == "initFinished":
            self.isinited = True

    def __on_message(self, ws, message):
        self.__processMessage(message)

    def __on_error(self, ws, error):
        print("Error:", error)

    def __on_close(self, ws, close_status_code, close_msg):
        print("Closed connection with status code:", close_status_code, "and message:", close_msg)

    def __on_open(self, ws):
        def run(*args):
            data_to_send = {
                "name": self.name,
                "type": "init",
                "group": self.group,
                "country": self.country,
                "lastMessageId": self.lastMessageId,
                "userAgent": self.userAgent
            }
            ws.send(json.dumps(data_to_send))

        threading.Thread(target=run, daemon=True).start()

    def respondMsg(self, msg: str):
        pass

    def sendText(self, msgText: str):
        def run():
            msg_data = {
                "type": "message",
                "group": self.group,
                "name": self.name,
                "text": msgText,
                "date": time.time()
            }
            self.ws.send(json.dumps(msg_data))

        threading.Thread(target=run, daemon=True).start()

    def start(self):
        url = "wss://idnschat.com/ws"
        self.ws = websocket.WebSocketApp(url=url,
                                         on_open=self.__on_open,
                                         on_message=self.__on_message,
                                         on_error=self.__on_error,
                                         on_close=self.__on_close)
        self.ws.run_forever(ping_interval=10, ping_timeout=5)
