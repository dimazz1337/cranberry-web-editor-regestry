import grpc_src.pr_file_pb2 as file_pb2
import grpc_src.pr_file_pb2_grpc as pb2_grpc
import grpc


def run():
    with grpc.insecure_channel("193.149.180.36:81") as channel:
        stub = pb2_grpc.EditorRegistryStub(channel)

        user_data = {
            "id": 100,
            "uid": "1000",
            "snils": "5452454",
            "name": "EEEEE",
            "surname": "uid",
            "patronymic": "uid",
            "birthday": "2001-09-19",
            "current_category": "3",
            "date_end_category": "2024-09-19",
            "last_change": "2023-09-19",
        }


        request = file_pb2.RequestEditAddRowRegistry(
            token="",
            info=file_pb2.Info(
                id=user_data["id"],
                uid=user_data["uid"],
                snils=user_data["snils"],
                name=user_data["name"],
                surname=user_data["surname"],
                patronymic=user_data["patronymic"],
                birthday=user_data["birthday"],
                category=user_data["current_category"],
                dateEnd=user_data["date_end_category"],
                last_change=user_data["last_change"]
            )
        )

        stub.AddRowRegistry(request)

run()