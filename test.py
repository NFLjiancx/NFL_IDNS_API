from NFL_idns_api import NflIdnsLoader


class NflIdnsClient(NflIdnsLoader):
    def respondMsg(self, msg):
        if self.isinited:
            if msg == "test":
                self.sendText("nflIdnsApi Program written by NFL_jiancx.")


useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
NFL_client = NflIdnsClient("NFL_Bot_test", "idns_cn", "CN", -1, useragent)
NFL_client.start()

