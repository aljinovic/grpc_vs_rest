from concurrent import futures
from datetime import datetime
import time

import grpc
import users_pb2_grpc

from data import users_reply

REQUESTS = 20000


class UsersServicer(users_pb2_grpc.UsersServicer):
    count = 1
    count_stream = 1

    def get(self, request, context):
        print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] #{self.count}')
        self.count += 1

        return users_reply

    def get_stream(self, request, context):
        print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] #{self.count_stream}')
        self.count_stream += 1

        for i in range(REQUESTS):
            yield users_reply


server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
users_pb2_grpc.add_UsersServicer_to_server(UsersServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()

print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] GRPC Server START')

while True:
    time.sleep(60)
