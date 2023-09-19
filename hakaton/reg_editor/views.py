from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
import grpc_src.pr_file_pb2 as pb2
import grpc_src.pr_file_pb2_grpc as pb2_grpc
import grpc


def index(request):
    return render(request, 'reg_editor/index.html')


def add_user(request):
    return render(request, 'reg_editor/modal_add_user.html')


def edit_user(request):
    return render(request, 'reg_editor/modal_edit_user.html')


def panel_re_editor(request):
    with grpc.insecure_channel("193.149.180.36:80") as channel:
        stub = pb2_grpc.EditorRegistryStub(channel)

        response = stub.GetNRowsRegistry(pb2.RequestGetNRowsRegistry(token="", fromN=0, toN=1000000))

        users_data = []
        for i in response.info:
            user_db = {
                "id": i.id,
                "uid": i.uid,
                "snils": i.snils,
                "name": i.name,
                "surname": i.surname,
                "patronymic": i.patronymic,
                "birthday": i.birthday,
                "current_category": i.category,
                "date_end_category": i.dateEnd,
                "last_change": i.last_change
            }
            users_data.append(user_db)

        paginator = Paginator(users_data, 20)

        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

    return render(request, 'reg_editor/panel_re_editor.html', {'page': page})



def add_button_click(request):
    print('Response: OK-add')
    return HttpResponse('Response: OK-add')


def save_button_click(request):
    print('Response: OK-save')
    return HttpResponse('Response: OK-save')

def del_button_click(request):
    print('Response: OK-del')
    return HttpResponse('Response: OK-del')

def edit_button_click(request):
    print('Response: OK-edit')
    return HttpResponse('Response: OK-edit')

def search_button_click(request):
    print('Response: OK-search')
    return HttpResponse('Response: OK-search')


def profile(request):
    return render(request, 'reg_editor/panel_account.html')

