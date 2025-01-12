#On po uruchomieniu opróżnia kolejkę zadań jakie zrobił job
#Odpytanie w redisie stacji czyliw  CMD polecenie: lrange temps:STACJA001 0 -1

from pkginfo.commandline import Simple
from redis import Redis
from rq.timeouts import BaseDeathPenalty
from rq import Queue, SimpleWorker

#To nadpisujemy timeouty bo na windowsie nie działa. na linuxie nie byłoby potrzeby
class DummyDeathPenalty(BaseDeathPenalty):
    def setup_death_penalty(self):
        pass

    def cancel_death_penalty(self):
        pass



if __name__ == "__main__":
    redis_conn = Redis()

    queue = Queue('weather_station', connection=redis_conn)
    worker = SimpleWorker([queue], connection=redis_conn)

    #To jest zastępstwo dla windowca
    worker.death_penalty_class = DummyDeathPenalty

    worker.work()